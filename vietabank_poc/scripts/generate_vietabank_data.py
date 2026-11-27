#!/usr/bin/env python3
"""
Generate a realistic 100-customer VietABank Customer 360 POC dataset
for Oracle AI Data Platform (AIDP) — matching the exact schema of the
reference DATA_MOOKUP_AIDP/sql_tables/ plus 4 operational agent tables.

Outputs:
  - data/csv/*.csv          (12 UTF-8 CSV files ready to upload into AIDP)
  - data/sql/*.sql          (12 PostgreSQL-compatible SQL dumps)
  - data/vietabank_c360.db  (Unified SQLite DB for local testing & verification)

Golden Demo Scenarios embedded:
  1. CIF 200001 — Nguyễn Minh Quân (NBA: ATM Card Retained -> Suppress NBO -> Service Recovery -> Resume after Resolved + 48h cooling-off)
  2. CIF 200002 — Trần Ngọc Lan Anh (NBO + RAG + Human-in-the-Loop Lead: Priority customer, term deposit maturing in 10 days, no credit card, clean record -> VietABank Visa Platinum + Priority Deposit Renewal)
  3. Plus CIF 200003 — Phạm Đức Hải (Already RESOLVED ATM card incident > 48h ago -> Ready for follow-up call & NBO reactivation, proving the AFTER state!)
"""

import csv
import os
import random
import sqlite3
from datetime import date, timedelta

SEED = 20261127
random.seed(SEED)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_DIR = os.path.join(BASE_DIR, "data", "csv")
SQL_DIR = os.path.join(BASE_DIR, "data", "sql")
DB_PATH = os.path.join(BASE_DIR, "data", "vietabank_c360.db")

os.makedirs(CSV_DIR, exist_ok=True)
os.makedirs(SQL_DIR, exist_ok=True)

DATA_DATE = date(2026, 11, 27)

BRANCHES = [
    ("HN01", "Sở Giao dịch Hà Nội - HN01", "MIEN_BAC", "D01", "PF001", "RM Nguyễn Thu Hà"),
    ("HN02", "CN Cầu Giấy - HN02", "MIEN_BAC", "D02", "PF002", "RM Lê Quang Minh"),
    ("HCM01", "Sở Giao dịch TP.HCM - HCM01", "MIEN_NAM", "D03", "PF003", "RM Võ Hoàng Yến"),
    ("HCM02", "CN Quận 3 - HCM02", "MIEN_NAM", "D04", "PF004", "RM Trần Quốc Bảo"),
    ("DN01", "CN Đà Nẵng - DN01", "MIEN_TRUNG", "D05", "PF005", "RM Phan Thảo Vy"),
    ("CT01", "CN Cần Thơ - CT01", "MIEN_NAM", "D05", "PF006", "RM Huỳnh Tấn Phát"),
]

LAST_NAMES = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Huỳnh", "Phan", "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Trịnh"]
MALE_MIDDLE = ["Minh", "Đức", "Quang", "Hoàng", "Xuân", "Tuấn", "Văn", "Hữu", "Bá", "Gia", "Thành", "Công"]
MALE_FIRST = ["Quân", "Hải", "Nam", "Long", "Khoa", "Sơn", "Đạt", "Phong", "Tuấn", "Thắng", "Hùng", "Dũng", "Khánh", "Việt", "Kiên", "Tùng"]
FEMALE_MIDDLE = ["Ngọc", "Thu", "Thị", "Mai", "Lan", "Phương", "Thanh", "Diệu", "Kim", "Bích", "Khánh", "Hoài"]
FEMALE_FIRST = ["Anh", "Chi", "Hương", "Linh", "Trang", "Phương", "Yến", "Quỳnh", "Oanh", "Thảo", "Ngân", "Vy", "Hà", "Tâm", "Nhi", "My"]

DEPOSIT_PRODUCTS = [
    ("Tiết kiệm Trực tuyến VietABank", 5.4, 6.0),
    ("Tiết kiệm Truyền thống tại quầy", 5.0, 5.6),
    ("Tiền gửi Có kỳ hạn Linh hoạt", 4.6, 5.2),
    ("Chứng chỉ tiền gửi VietABank", 5.8, 6.4),
    ("Tiết kiệm Tích lũy An Gia", 5.1, 5.7),
]

LOAN_PRODUCTS = [
    ("Vay mua nhà / sửa chữa nhà ở", 8.5, 10.5),
    ("Vay mua xe ô tô KHCN", 9.0, 11.2),
    ("Vay sản xuất kinh doanh KHCN", 8.8, 10.8),
    ("Vay tiêu dùng có tài sản bảo đảm", 9.5, 11.8),
    ("Vay thấu chi tài khoản lương", 10.5, 12.5),
    ("Vay cầm cố sổ tiết kiệm VietABank", 7.2, 8.5),
]

CARD_TYPES = [
    ("VietABank Debit Nội địa Chuẩn", 0, "DEBIT"),
    ("VietABank Debit Nội địa Vàng", 0, "DEBIT"),
    ("VietABank Credit Nội địa Chuẩn", 50_000_000, "CREDIT"),
    ("VietABank Visa Classic", 80_000_000, "CREDIT"),
    ("VietABank Visa Platinum", 250_000_000, "CREDIT"),
]

CHANNELS = [
    "Tổng đài CSKH 1900 555 590",
    "Ứng dụng VietABank EzMobile",
    "Chi nhánh / PGD",
    "Internet Banking",
    "Email",
]

NORMAL_PURPOSES = [
    ("Chăm sóc định kỳ", "RM gọi hỏi thăm trải nghiệm sử dụng dịch vụ, khách hàng hài lòng."),
    ("Yêu cầu sao kê", "Khách hàng yêu cầu sao kê tài khoản 6 tháng gần nhất — đã hỗ trợ hoàn tất."),
    ("Tư vấn sản phẩm", "Tư vấn gói tiết kiệm online và ưu đãi lãi suất kỳ hạn 12 tháng."),
    ("Hỗ trợ kỹ thuật", "Hướng dẫn kích hoạt sinh trắc học trên ứng dụng VietABank EzMobile — đã xử lý xong."),
    ("Tra cứu biểu phí", "Khách hàng hỏi biểu phí chuyển tiền quốc tế và thẻ Visa — đã giải đáp."),
]

def rand_date(start: date, end: date) -> date:
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, max(delta, 1)))

def fmt_date(d):
    return d.isoformat() if d else None

def sql_val(v):
    if v is None:
        return "NULL"
    if isinstance(v, (int, float)):
        return str(v)
    escaped = str(v).replace("'", "''")
    return f"'{escaped}'"

def make_phone(idx: int) -> str:
    prefixes = ["090", "091", "093", "094", "096", "097", "098", "086", "088"]
    return f"{prefixes[idx % len(prefixes)]}{random.randint(1000000, 9999999)}"

def make_id_card(idx: int, gender: str, birth_year: int) -> str:
    prov = random.choice(["001", "079", "048", "031", "092", "036", "038", "075"])
    century_code = ("0" if gender == "M" else "1") if birth_year < 2000 else ("2" if gender == "M" else "3")
    yy = str(birth_year)[-2:]
    seq = f"{(100000 + idx * 7919) % 999999:06d}"
    return f"{prov}{century_code}{yy}{seq}"

def make_masked_card(card_type: str) -> str:
    bin_prefix = "4214" if "Visa" in card_type else "9704"
    return f"{bin_prefix}****{random.randint(1000, 9999)}"

# Containers for 12 tables
core_customers = []
crm_customers = []
deposit_accounts = []
loan_accounts = []
card_accounts = []
product_holdings = []
interaction_history = []
customer_master = []
data_grants = []
leads = []
product_catalog = []
offer_history = []

holding_seq = 500001
interaction_seq = 700001
offer_seq = 900001

def add_customer(
    idx: int,
    cif: str,
    full_name: str,
    gender: str,
    dob: date,
    segment: str,
    tier_name: str,
    credit_rating: str,
    branch_tuple,
    created_date: date,
    casa_balance: float,
    deposits: list,
    loans: list,
    cards: list,
    interactions: list,
    in_core: bool = True,
    crm_balance_drift: float = 0.0,
    custom_address: str = None,
    custom_phone: str = None,
):
    global holding_seq, interaction_seq
    branch_id, branch_name, region, dept_id, portfolio_id, rm_name = branch_tuple
    id_card = make_id_card(idx, gender, dob.year)
    phone = custom_phone or make_phone(idx)
    email = f"kh{cif}@vietabank-demo.vn"
    address = custom_address or f"Số {random.randint(12, 380)}, Khu vực {branch_name.split(' - ')[0]}"
    age = DATA_DATE.year - dob.year - ((DATA_DATE.month, DATA_DATE.day) < (dob.month, dob.day))

    total_dep = sum(d["balance"] for d in deposits)
    total_balance = round(casa_balance + total_dep, 2)
    crm_balance = round(total_balance + crm_balance_drift, 2)

    # 01_core_customer (optionally omitted for 2 CRM-only reconciliation test cases)
    if in_core:
        core_customers.append({
            "cif": cif,
            "full_name": full_name,
            "id_card": id_card,
            "created_date": fmt_date(created_date),
            "credit_rating": credit_rating,
            "branch_id": branch_id,
            "department_id": dept_id,
            "portfolio_id": portfolio_id,
            "total_balance": total_balance,
            "source_system": "Core Banking",
        })

    # 02_crm_customer
    crm_customers.append({
        "cif": cif,
        "full_name": full_name,
        "id_card": id_card,
        "dob": fmt_date(dob),
        "phone": phone,
        "email": email,
        "address": address,
        "segment": segment,
        "branch_id": branch_id,
        "department_id": dept_id,
        "portfolio_id": portfolio_id,
        "crm_balance": crm_balance,
        "source_system": "CRM",
    })

    # CASA holding
    if in_core:
        product_holdings.append({
            "holding_id": holding_seq,
            "cif": cif,
            "product_category": "CASA",
            "product_code": "VAB_CASA_01",
            "product_name": "Tài khoản thanh toán VietABank",
            "status": "ACTIVE",
            "opened_date": fmt_date(created_date),
            "branch_id": branch_id,
            "department_id": dept_id,
            "portfolio_id": portfolio_id,
            "source_system": "Core Banking",
        })
        holding_seq += 1

    # 03_deposit_account + 06_product_holding
    for d_i, dep in enumerate(deposits):
        acc_id = f"DP{cif}{d_i}"
        deposit_accounts.append({
            "account_id": acc_id,
            "cif": cif,
            "product_name": dep["product_name"],
            "balance": round(dep["balance"], 2),
            "currency": "VND",
            "open_date": fmt_date(dep["open_date"]),
            "maturity_date": fmt_date(dep["maturity_date"]),
            "interest_rate": round(dep["interest_rate"], 3),
            "status": dep.get("status", "ACTIVE"),
            "branch_id": branch_id,
            "department_id": dept_id,
            "portfolio_id": portfolio_id,
            "source_system": "Deposits",
        })
        product_holdings.append({
            "holding_id": holding_seq,
            "cif": cif,
            "product_category": "TIET_KIEM",
            "product_code": f"VAB_TD_{d_i+1:02d}",
            "product_name": dep["product_name"],
            "status": dep.get("status", "ACTIVE"),
            "opened_date": fmt_date(dep["open_date"]),
            "branch_id": branch_id,
            "department_id": dept_id,
            "portfolio_id": portfolio_id,
            "source_system": "Deposits",
        })
        holding_seq += 1

    # 04_loan_account + 06_product_holding
    for l_i, ln in enumerate(loans):
        loan_id = f"LN{cif}{l_i}"
        loan_accounts.append({
            "loan_id": loan_id,
            "cif": cif,
            "loan_type": ln["loan_type"],
            "principal_amount": round(ln["principal_amount"], 2),
            "remaining_balance": round(ln["remaining_balance"], 2),
            "start_date": fmt_date(ln["start_date"]),
            "end_date": fmt_date(ln["end_date"]),
            "interest_rate": round(ln["interest_rate"], 3),
            "status": ln.get("status", "ACTIVE"),
            "branch_id": branch_id,
            "department_id": dept_id,
            "portfolio_id": portfolio_id,
            "source_system": "LOS",
        })
        product_holdings.append({
            "holding_id": holding_seq,
            "cif": cif,
            "product_category": "VAY",
            "product_code": f"VAB_LN_{l_i+1:02d}",
            "product_name": ln["loan_type"],
            "status": ln.get("status", "ACTIVE"),
            "opened_date": fmt_date(ln["start_date"]),
            "branch_id": branch_id,
            "department_id": dept_id,
            "portfolio_id": portfolio_id,
            "source_system": "LOS",
        })
        holding_seq += 1

    # 05_card_account + 06_product_holding
    for c_i, cd in enumerate(cards):
        card_id = f"CD{cif}{c_i}"
        card_accounts.append({
            "card_id": card_id,
            "cif": cif,
            "card_type": cd["card_type"],
            "card_number_masked": cd.get("masked", make_masked_card(cd["card_type"])),
            "credit_limit": round(cd["credit_limit"], 2),
            "current_balance": round(cd["current_balance"], 2),
            "status": cd.get("status", "ACTIVE"),
            "issue_date": fmt_date(cd["issue_date"]),
            "branch_id": branch_id,
            "department_id": dept_id,
            "portfolio_id": portfolio_id,
            "source_system": "Cards",
        })
        prod_code = "VAB_CARD_CC" if ("Visa" in cd["card_type"] or "Credit" in cd["card_type"]) else "VAB_CARD_DB"
        product_holdings.append({
            "holding_id": holding_seq,
            "cif": cif,
            "product_category": "THE",
            "product_code": prod_code,
            "product_name": cd["card_type"],
            "status": cd.get("status", "ACTIVE"),
            "opened_date": fmt_date(cd["issue_date"]),
            "branch_id": branch_id,
            "department_id": dept_id,
            "portfolio_id": portfolio_id,
            "source_system": "Cards",
        })
        holding_seq += 1

    # 07_interaction_history
    for inter in interactions:
        interaction_history.append({
            "interaction_id": interaction_seq,
            "cif": cif,
            "interaction_date": fmt_date(inter["date"]),
            "channel": inter["channel"],
            "purpose": inter["purpose"],
            "notes": inter["notes"],
            "branch_id": branch_id,
            "department_id": dept_id,
            "portfolio_id": portfolio_id,
            "source_system": inter.get("source_system", "CRM"),
        })
        interaction_seq += 1

    # 08_customer_master
    tier_start = date(2026, 1, 1) if tier_name else None
    tier_end = date(2027, 1, 1) if tier_name else None
    customer_master.append({
        "data_date": fmt_date(DATA_DATE),
        "region": region,
        "department_id": dept_id,
        "branch_name": branch_name,
        "branch_id": branch_id,
        "portfolio_id": portfolio_id,
        "rm_name": rm_name,
        "cif": cif,
        "id_card": id_card,
        "full_name": full_name,
        "dob": fmt_date(dob),
        "age": age,
        "phone": phone,
        "gender": gender,
        "segment": segment,
        "tier_name": tier_name,
        "tier_start_date": fmt_date(tier_start),
        "tier_end_date": fmt_date(tier_end),
        "total_assets": total_balance,
        "address": address,
    })

# ==============================================================================
# GOLDEN SCENARIO 1 — CIF 200001: Nguyễn Minh Quân
# Event-Driven NBA & Sales Suppression ("Nuốt thẻ ATM -> Dừng bán -> Xử lý xong mới gọi lại")
# ==============================================================================
add_customer(
    idx=1,
    cif="200001",
    full_name="Nguyễn Minh Quân",
    gender="M",
    dob=date(1988, 5, 14),
    segment="Affluent",
    tier_name="Hạng Vàng",
    credit_rating="A",
    branch_tuple=BRANCHES[0],  # HN01 - Sở Giao dịch Hà Nội
    created_date=date(2020, 4, 15),
    casa_balance=250_000_000,
    deposits=[
        {
            "product_name": "Tiết kiệm Trực tuyến VietABank",
            "balance": 1_000_000_000,
            "open_date": date(2026, 2, 10),
            "maturity_date": date(2027, 2, 10),
            "interest_rate": 5.65,
        },
        {
            "product_name": "Tiền gửi Có kỳ hạn Linh hoạt",
            "balance": 600_000_000,
            "open_date": date(2026, 6, 15),
            "maturity_date": date(2026, 12, 15),
            "interest_rate": 5.10,
        },
    ],
    loans=[],
    cards=[
        {
            "card_type": "VietABank Debit Nội địa Vàng",
            "masked": "9704****8821",
            "credit_limit": 0,
            "current_balance": 0,
            "status": "LOCKED_ATM_RETAINED",
            "issue_date": date(2023, 3, 20),
        }
    ],
    interactions=[
        {
            "date": date(2026, 10, 12),
            "channel": "Ứng dụng VietABank EzMobile",
            "purpose": "Chăm sóc định kỳ",
            "notes": "Khách hàng giao dịch ổn định, số dư tiền gửi tăng đều, chưa sở hữu thẻ tín dụng quốc tế.",
            "source_system": "CRM",
        },
        {
            "date": date(2026, 11, 20),
            "channel": "Chi nhánh / PGD",
            "purpose": "Tư vấn sản phẩm",
            "notes": "[CAMPAIGN:NBO_VISA_PLATINUM | STAGE:IN_PROGRESS] RM đang tư vấn mở Thẻ tín dụng Quốc tế VietABank Visa Platinum (hạn mức đề xuất 200 triệu VND). Khách hàng quan tâm, hẹn gọi lại ngày 27/11 để chốt hồ sơ.",
            "source_system": "CRM",
        },
        {
            "date": date(2026, 11, 25),
            "channel": "Tổng đài CSKH 1900 555 590",
            "purpose": "Sự cố nuốt thẻ ATM - ĐANG XỬ LÝ",
            "notes": "[TICKET:TS-20261125-001 | INCIDENT:ATM_CARD_RETAINED | STATUS:OPEN | SEVERITY:HIGH] Khách hàng bị nuốt thẻ VietABank Debit Nội địa Vàng (9704****8821) tại cây ATM VietABank Hoàn Kiếm do lỗi kỹ thuật. Tổng đài đã khóa thẻ khẩn cấp và lập phiếu tra soát hẹn trả/cấp lại thẻ miễn phí trong 3-5 ngày làm việc. BẮT BUỘC TẠM DỪNG MỌI CUỘC GỌI BÁN HÀNG (SUPPRESS NBO) cho tới khi xử lý xong và qua thời gian hạ nhiệt 48 giờ.",
            "source_system": "CRM",
        },
    ],
    custom_address="Số 48 Lý Thường Kiệt, Quận Hoàn Kiếm, Hà Nội",
    custom_phone="0912345678",
)

# ==============================================================================
# GOLDEN SCENARIO 2 — CIF 200002: Trần Ngọc Lan Anh
# Clean NBO + Cross-Sell + RAG Policy Citation + Human-in-the-Loop Lead
# ==============================================================================
add_customer(
    idx=2,
    cif="200002",
    full_name="Trần Ngọc Lan Anh",
    gender="F",
    dob=date(1984, 9, 22),
    segment="Priority",
    tier_name="Hạng Bạch Kim",
    credit_rating="AA",
    branch_tuple=BRANCHES[2],  # HCM01 - Sở Giao dịch TP.HCM
    created_date=date(2019, 8, 5),
    casa_balance=550_000_000,
    deposits=[
        {
            "product_name": "Tiết kiệm Trực tuyến VietABank",
            "balance": 2_500_000_000,
            "open_date": date(2025, 12, 7),
            "maturity_date": date(2026, 12, 7),  # Sắp đáo hạn sau đúng 10 ngày!
            "interest_rate": 5.80,
        },
        {
            "product_name": "Chứng chỉ tiền gửi VietABank",
            "balance": 3_800_000_000,
            "open_date": date(2025, 7, 15),
            "maturity_date": date(2027, 7, 15),
            "interest_rate": 6.25,
        },
    ],
    loans=[],
    cards=[
        {
            "card_type": "VietABank Debit Nội địa Vàng",
            "masked": "9704****5590",
            "credit_limit": 0,
            "current_balance": 0,
            "status": "ACTIVE",
            "issue_date": date(2022, 6, 10),
        }
    ],
    interactions=[
        {
            "date": date(2026, 9, 18),
            "channel": "Ứng dụng VietABank EzMobile",
            "purpose": "Chăm sóc định kỳ",
            "notes": "Khách hàng Priority giao dịch chuyển khoản và mua sắm trực tuyến thường xuyên, đánh giá 5 sao chất lượng ứng dụng.",
            "source_system": "CRM",
        },
        {
            "date": date(2026, 11, 10),
            "channel": "Tổng đài CSKH 1900 555 590",
            "purpose": "Tư vấn sản phẩm",
            "notes": "Khách hàng hỏi về biểu lãi suất tái tục sổ tiết kiệm 2.5 tỷ VND sắp đáo hạn ngày 07/12/2026 và hỏi thêm về ưu đãi chi tiêu nước ngoài dịp cuối năm.",
            "source_system": "CRM",
        },
        {
            "date": date(2026, 11, 22),
            "channel": "Email",
            "purpose": "Tư vấn sản phẩm",
            "notes": "Khách hàng mở email giới thiệu đặc quyền khách hàng Priority VietABank (chưa có thẻ tín dụng quốc tế, không có khiếu nại hay sự cố mở).",
            "source_system": "DWH",
        },
    ],
    custom_address="Số 125 Nguyễn Huệ, Quận 1, TP. Hồ Chí Minh",
    custom_phone="0908765432",
)

# ==============================================================================
# BONUS COMPANION PERSONA — CIF 200003: Phạm Đức Hải
# Shows the AFTER state of Scenario 1 (ATM incident RESOLVED > 48h ago -> Ready to call back & resume NBO!)
# ==============================================================================
add_customer(
    idx=3,
    cif="200003",
    full_name="Phạm Đức Hải",
    gender="M",
    dob=date(1990, 2, 18),
    segment="Affluent",
    tier_name="Hạng Vàng",
    credit_rating="A",
    branch_tuple=BRANCHES[0],  # HN01
    created_date=date(2021, 11, 1),
    casa_balance=180_000_000,
    deposits=[
        {
            "product_name": "Tiết kiệm Truyền thống tại quầy",
            "balance": 1_200_000_000,
            "open_date": date(2026, 3, 1),
            "maturity_date": date(2027, 3, 1),
            "interest_rate": 5.50,
        },
    ],
    loans=[],
    cards=[
        {
            "card_type": "VietABank Debit Nội địa Vàng",
            "masked": "9704****3314",
            "credit_limit": 0,
            "current_balance": 0,
            "status": "ACTIVE",
            "issue_date": date(2026, 11, 22),  # Thẻ cấp lại mới
        }
    ],
    interactions=[
        {
            "date": date(2026, 11, 15),
            "channel": "Chi nhánh / PGD",
            "purpose": "Tư vấn sản phẩm",
            "notes": "[CAMPAIGN:NBO_VISA_PLATINUM | STAGE:PAUSED] RM tư vấn mở thẻ tín dụng VietABank Visa Platinum, khách đồng ý tìm hiểu.",
            "source_system": "CRM",
        },
        {
            "date": date(2026, 11, 18),
            "channel": "Tổng đài CSKH 1900 555 590",
            "purpose": "Sự cố nuốt thẻ ATM - ĐÃ XỬ LÝ",
            "notes": "[TICKET:TS-20261118-009 | INCIDENT:ATM_CARD_RETAINED | STATUS:CLOSED | RESOLVED_DATE:2026-11-22] Đã cấp lại thẻ miễn phí và bàn giao cho khách hàng ngày 22/11/2026. Khách hàng xác nhận hài lòng.",
            "source_system": "CRM",
        },
        {
            "date": date(2026, 11, 23),
            "channel": "Tổng đài CSKH 1900 555 590",
            "purpose": "Chăm sóc sau sự cố",
            "notes": "[TICKET:TS-20261118-009 | STATUS:RESOLVED | COOLING_OFF_PASSED:TRUE] Đã qua hơn 48 giờ từ khi đóng sự cố, đủ điều kiện mở lại chiến dịch tư vấn NBO và gọi hỏi thăm khách hàng.",
            "source_system": "CRM",
        },
    ],
    custom_address="Số 22 Tràng Tiền, Quận Hoàn Kiếm, Hà Nội",
    custom_phone="0987654321",
)

# ==============================================================================
# REMAINING 97 REALISTIC VIETABANK CUSTOMERS (CIF 200004 -> 200100)
# ==============================================================================
SEGMENTS = ["Priority", "Affluent", "Mass", "SME"]
SEGMENT_WEIGHTS = [0.18, 0.28, 0.38, 0.16]
RATINGS = ["AA", "A", "BB", "B", "C"]

# Designate special test cases for Data Quality & Dashboard variety:
# - CIF 200095, 200096: CRM-only (missing in Core Banking -> Silver reconciliation alert!)
# - CIF 200097, 200098: Core vs CRM balance mismatch (drift > 50M VND -> Silver reconciliation alert!)
# - CIF 200004..200009 (6 customers): Open incidents (ATM card retained / fee dispute / transfer error) -> Sales Suppressed!
# - CIF 200010..200019 (10 customers): Term deposit maturing within 15 days -> High-priority retention NBO!
# - CIF 200020..200029 (10 customers): High credit utilization (>75%) or eligible for credit card / loan upgrade!

for idx in range(4, 101):
    cif = str(200000 + idx)
    gender = random.choice(["M", "F"])
    ln = random.choice(LAST_NAMES)
    if gender == "M":
        full_name = f"{ln} {random.choice(MALE_MIDDLE)} {random.choice(MALE_FIRST)}"
    else:
        full_name = f"{ln} {random.choice(FEMALE_MIDDLE)} {random.choice(FEMALE_FIRST)}"

    dob = rand_date(date(1962, 1, 1), date(2002, 12, 31))
    segment = random.choices(SEGMENTS, weights=SEGMENT_WEIGHTS, k=1)[0]
    branch_tuple = random.choice(BRANCHES)
    created_date = rand_date(date(2016, 1, 1), date(2025, 10, 1))

    if segment == "Priority":
        tier_name = "Hạng Bạch Kim"
        credit_rating = random.choice(["AA", "A"])
        casa_bal = random.uniform(200_000_000, 1_200_000_000)
        num_dep = random.randint(1, 3)
        dep_range = (1_500_000_000, 6_000_000_000)
    elif segment == "Affluent":
        tier_name = "Hạng Vàng"
        credit_rating = random.choice(["AA", "A", "BB"])
        casa_bal = random.uniform(80_000_000, 450_000_000)
        num_dep = random.randint(1, 2)
        dep_range = (400_000_000, 2_000_000_000)
    elif segment == "SME":
        tier_name = random.choice(["Hạng Vàng", "Hạng Bạc"])
        credit_rating = random.choice(["A", "BB", "B"])
        casa_bal = random.uniform(150_000_000, 900_000_000)
        num_dep = random.randint(0, 2)
        dep_range = (300_000_000, 2_500_000_000)
    else:  # Mass
        tier_name = random.choice(["Hạng Chuẩn", None])
        credit_rating = random.choice(["A", "BB", "B", "C"])
        casa_bal = random.uniform(5_000_000, 120_000_000)
        num_dep = random.randint(0, 1)
        dep_range = (30_000_000, 300_000_000)

    # Ensure maturing deposits for idx 10..19
    if 10 <= idx <= 19 and num_dep == 0:
        num_dep = 1

    deposits = []
    for d_i in range(num_dep):
        pname, r_min, r_max = random.choice(DEPOSIT_PRODUCTS)
        open_d = rand_date(date(2024, 6, 1), date(2026, 9, 1))
        if 10 <= idx <= 19 and d_i == 0:
            mat_d = DATA_DATE + timedelta(days=random.randint(3, 15))
            open_d = mat_d - timedelta(days=365)
        else:
            mat_d = rand_date(date(2027, 1, 15), date(2028, 10, 1))
        deposits.append({
            "product_name": pname,
            "balance": round(random.uniform(*dep_range), -5),
            "open_date": open_d,
            "maturity_date": mat_d,
            "interest_rate": round(random.uniform(r_min, r_max), 2),
        })

    # Loans (~30% of customers)
    loans = []
    if random.random() < 0.32 or (segment == "SME" and random.random() < 0.5):
        ltype, lr_min, lr_max = random.choice(LOAN_PRODUCTS)
        principal = round(random.uniform(150_000_000, 3_500_000_000), -6)
        remaining = round(principal * random.uniform(0.35, 0.92), -5)
        s_date = rand_date(date(2022, 1, 1), date(2026, 6, 1))
        e_date = s_date + timedelta(days=random.randint(730, 3650))
        loans.append({
            "loan_type": ltype,
            "principal_amount": principal,
            "remaining_balance": remaining,
            "start_date": s_date,
            "end_date": e_date,
            "interest_rate": round(random.uniform(lr_min, lr_max), 2),
        })

    # Cards
    cards = []
    # Almost everyone has a debit card
    if random.random() < 0.85 or (4 <= idx <= 9):
        debit_type = "VietABank Debit Nội địa Vàng" if segment in ("Priority", "Affluent") else "VietABank Debit Nội địa Chuẩn"
        card_status = "LOCKED_ATM_RETAINED" if idx in (4, 5, 6) else "ACTIVE"
        cards.append({
            "card_type": debit_type,
            "credit_limit": 0,
            "current_balance": 0,
            "status": card_status,
            "issue_date": rand_date(created_date, date(2026, 8, 1)),
        })
    # ~38% have a credit card (leave ~62% eligible for cross-sell NBO!)
    if random.random() < 0.38:
        if segment == "Priority":
            cc_type, limit = "VietABank Visa Platinum", random.choice([200_000_000, 300_000_000, 500_000_000])
        elif segment in ("Affluent", "SME"):
            cc_type, limit = random.choice([("VietABank Visa Classic", 80_000_000), ("VietABank Visa Platinum", 150_000_000)])
        else:
            cc_type, limit = random.choice([("VietABank Credit Nội địa Chuẩn", 30_000_000), ("VietABank Visa Classic", 50_000_000)])
        util_ratio = random.uniform(0.76, 0.94) if (20 <= idx <= 29) else random.uniform(0.05, 0.55)
        cards.append({
            "card_type": cc_type,
            "credit_limit": limit,
            "current_balance": round(limit * util_ratio, -4),
            "status": "ACTIVE",
            "issue_date": rand_date(max(created_date, date(2022, 1, 1)), date(2026, 9, 1)),
        })

    # Interactions (2 to 4 per customer)
    interactions = []
    for _ in range(random.randint(2, 4)):
        purp, note = random.choice(NORMAL_PURPOSES)
        interactions.append({
            "date": rand_date(date(2025, 11, 1), date(2026, 11, 18)),
            "channel": random.choice(CHANNELS),
            "purpose": purp,
            "notes": note,
            "source_system": random.choice(["CRM", "DWH"]),
        })

    # Open incidents for idx 4..9 (Sales Suppression test pool for Dashboard!)
    if idx in (4, 5, 6):
        interactions.append({
            "date": DATA_DATE - timedelta(days=random.randint(1, 3)),
            "channel": "Tổng đài CSKH 1900 555 590",
            "purpose": "Sự cố nuốt thẻ ATM - ĐANG XỬ LÝ",
            "notes": f"[TICKET:TS-20261125-0{idx:02d} | INCIDENT:ATM_CARD_RETAINED | STATUS:OPEN | SEVERITY:HIGH] Khách hàng bị nuốt thẻ tại cây ATM. Đã khóa thẻ khẩn cấp, đang chờ hoàn tất cấp lại thẻ trong 3-5 ngày làm việc. Tạm dừng chào bán sản phẩm.",
            "source_system": "CRM",
        })
    elif idx in (7, 8, 9):
        interactions.append({
            "date": DATA_DATE - timedelta(days=random.randint(1, 4)),
            "channel": "Tổng đài CSKH 1900 555 590",
            "purpose": "Khiếu nại tra soát giao dịch - ĐANG XỬ LÝ",
            "notes": f"[TICKET:TS-20261124-0{idx:02d} | INCIDENT:DISPUTE_TXN | STATUS:OPEN | SEVERITY:HIGH] Khách hàng phản ánh rút tiền ATM không nhả tiền nhưng bị trừ tài khoản. Đang phối hợp NAPAS tra soát. Tạm dừng chào bán sản phẩm.",
            "source_system": "CRM",
        })

    in_core = idx not in (95, 96)
    drift = random.choice([75_000_000, -120_000_000]) if idx in (97, 98) else 0.0

    add_customer(
        idx=idx,
        cif=cif,
        full_name=full_name,
        gender=gender,
        dob=dob,
        segment=segment,
        tier_name=tier_name,
        credit_rating=credit_rating,
        branch_tuple=branch_tuple,
        created_date=created_date,
        casa_balance=round(casa_bal, -5),
        deposits=deposits,
        loans=loans,
        cards=cards,
        interactions=interactions,
        in_core=in_core,
        crm_balance_drift=drift,
    )

# ==============================================================================
# OPERATIONAL TABLES 09 -> 12
# ==============================================================================
data_grants = [
    {"username": "admin_vietabank", "role_name": "HO_ADMIN", "branch_id": "ALL", "can_view_pii": 1},
    {"username": "rm_hn01", "role_name": "BRANCH_RM", "branch_id": "HN01", "can_view_pii": 1},
    {"username": "rm_hcm01", "role_name": "BRANCH_RM", "branch_id": "HCM01", "can_view_pii": 1},
    {"username": "analyst_c360", "role_name": "DATA_ANALYST", "branch_id": "ALL", "can_view_pii": 0},
    {"username": "telesales_dn01", "role_name": "BRANCH_TELESALES", "branch_id": "DN01", "can_view_pii": 0},
]

product_catalog = [
    {
        "product_code": "VAB_VISA_PLATINUM",
        "product_name": "Thẻ tín dụng Quốc tế VietABank Visa Platinum",
        "product_category": "THE",
        "target_segment": "Priority, Affluent",
        "priority": 1,
        "rule_description": "Ưu tiên chào cho KH Priority/Affluent, tổng tài sản >= 1 tỷ VND, xếp hạng tín dụng AA/A, chưa sở hữu thẻ tín dụng quốc tế, và KHÔNG có sự cố/khiếu nại đang mở.",
        "rule_sql": "segment IN ('Priority','Affluent') AND total_assets >= 1000000000 AND credit_rating IN ('AA','A') AND has_credit_card = 0 AND open_incident_count = 0",
    },
    {
        "product_code": "VAB_TD_RENEWAL_VIP",
        "product_name": "Gói Tái tục Tiết kiệm Ưu đãi Priority",
        "product_category": "TIET_KIEM",
        "target_segment": "Priority, Affluent, Mass",
        "priority": 2,
        "rule_description": "Chào cho KH có sổ tiết kiệm sắp đáo hạn trong 15 ngày tới (days_to_maturity BETWEEN 0 AND 15) và không có sự cố đang mở, giúp giữ chân dòng tiền gửi.",
        "rule_sql": "days_to_next_maturity BETWEEN 0 AND 15 AND open_incident_count = 0",
    },
    {
        "product_code": "VAB_VISA_CLASSIC",
        "product_name": "Thẻ tín dụng Quốc tế VietABank Visa Classic",
        "product_category": "THE",
        "target_segment": "Mass, Affluent",
        "priority": 3,
        "rule_description": "Chào cho KH Mass/Affluent đủ 18 tuổi, tổng số dư >= 100 triệu VND, chưa có thẻ tín dụng và không có sự cố mở.",
        "rule_sql": "age >= 18 AND total_assets >= 100000000 AND has_credit_card = 0 AND open_incident_count = 0",
    },
    {
        "product_code": "VAB_CREDIT_LIMIT_UP",
        "product_name": "Nâng hạn mức Thẻ tín dụng VietABank",
        "product_category": "THE",
        "target_segment": "Priority, Affluent, Mass",
        "priority": 4,
        "rule_description": "Chào cho KH đã có thẻ tín dụng với tỷ lệ sử dụng hạn mức >= 75%, xếp hạng tín dụng AA/A/BB và không có sự cố mở.",
        "rule_sql": "has_credit_card = 1 AND max_card_utilization >= 0.75 AND credit_rating IN ('AA','A','BB') AND open_incident_count = 0",
    },
    {
        "product_code": "VAB_TD_ONLINE",
        "product_name": "Tiết kiệm Trực tuyến VietABank EzMobile",
        "product_category": "TIET_KIEM",
        "target_segment": "Mass, SME",
        "priority": 5,
        "rule_description": "Chào cho KH đang giữ số dư CASA nhàn rỗi >= 100 triệu VND nhưng chưa có sổ tiết kiệm kỳ hạn và không có sự cố mở.",
        "rule_sql": "casa_balance >= 100000000 AND deposit_count = 0 AND open_incident_count = 0",
    },
    {
        "product_code": "VAB_LOAN_SECURED",
        "product_name": "Vay tiêu dùng / Cầm cố sổ tiết kiệm VietABank",
        "product_category": "VAY",
        "target_segment": "Affluent, SME",
        "priority": 6,
        "rule_description": "Chào cho KH SME/Affluent có sổ tiết kiệm >= 500 triệu VND, chưa có khoản vay, xếp hạng AA/A/BB và không có sự cố mở.",
        "rule_sql": "segment IN ('Affluent','SME') AND deposit_balance >= 500000000 AND loan_count = 0 AND open_incident_count = 0",
    },
]

# Offer history (~150 historical records for MLflow NBO propensity training)
for i in range(150):
    c = random.choice(crm_customers)
    p = random.choice(product_catalog)
    o_date = rand_date(date(2025, 6, 1), date(2026, 10, 15))
    # Priority & Affluent accept at higher probability for realistic ML signal
    accept_prob = 0.65 if c["segment"] in ("Priority", "Affluent") else 0.42
    status = "ACCEPTED" if random.random() < accept_prob else "REJECTED"
    r_date = o_date + timedelta(days=random.randint(1, 10))
    offer_history.append({
        "offer_id": offer_seq,
        "cif": c["cif"],
        "product_code": p["product_code"],
        "product_name": p["product_name"],
        "offer_date": fmt_date(o_date),
        "channel": random.choice(["Chi nhánh / PGD", "Tổng đài CSKH 1900 555 590", "Ứng dụng VietABank EzMobile", "Email"]),
        "response_status": status,
        "response_date": fmt_date(r_date),
        "notes": "Khách hàng đồng ý mở sản phẩm." if status == "ACCEPTED" else "Khách hàng chưa có nhu cầu tại thời điểm tư vấn.",
    })
    offer_seq += 1

# ==============================================================================
# TABLE SCHEMAS & EXPORT HELPERS (CSV + PostgreSQL SQL + SQLite DB)
# ==============================================================================
TABLES = [
    ("01_core_customer", "core_customer", [
        ("cif", "TEXT"), ("full_name", "TEXT"), ("id_card", "TEXT"), ("created_date", "DATE"),
        ("credit_rating", "TEXT"), ("branch_id", "TEXT"), ("department_id", "TEXT"),
        ("portfolio_id", "TEXT"), ("total_balance", "NUMERIC(24,6)"), ("source_system", "TEXT"),
    ], "PRIMARY KEY (cif)", core_customers),
    ("02_crm_customer", "crm_customer", [
        ("cif", "TEXT"), ("full_name", "TEXT"), ("id_card", "TEXT"), ("dob", "DATE"),
        ("phone", "TEXT"), ("email", "TEXT"), ("address", "TEXT"), ("segment", "TEXT"),
        ("branch_id", "TEXT"), ("department_id", "TEXT"), ("portfolio_id", "TEXT"),
        ("crm_balance", "NUMERIC(24,6)"), ("source_system", "TEXT"),
    ], "PRIMARY KEY (cif)", crm_customers),
    ("03_deposit_account", "deposit_account", [
        ("account_id", "TEXT"), ("cif", "TEXT"), ("product_name", "TEXT"), ("balance", "NUMERIC(24,6)"),
        ("currency", "TEXT"), ("open_date", "DATE"), ("maturity_date", "DATE"),
        ("interest_rate", "NUMERIC(24,6)"), ("status", "TEXT"), ("branch_id", "TEXT"),
        ("department_id", "TEXT"), ("portfolio_id", "TEXT"), ("source_system", "TEXT"),
    ], "PRIMARY KEY (account_id)", deposit_accounts),
    ("04_loan_account", "loan_account", [
        ("loan_id", "TEXT"), ("cif", "TEXT"), ("loan_type", "TEXT"), ("principal_amount", "NUMERIC(24,6)"),
        ("remaining_balance", "NUMERIC(24,6)"), ("start_date", "DATE"), ("end_date", "DATE"),
        ("interest_rate", "NUMERIC(24,6)"), ("status", "TEXT"), ("branch_id", "TEXT"),
        ("department_id", "TEXT"), ("portfolio_id", "TEXT"), ("source_system", "TEXT"),
    ], "PRIMARY KEY (loan_id)", loan_accounts),
    ("05_card_account", "card_account", [
        ("card_id", "TEXT"), ("cif", "TEXT"), ("card_type", "TEXT"), ("card_number_masked", "TEXT"),
        ("credit_limit", "NUMERIC(24,6)"), ("current_balance", "NUMERIC(24,6)"), ("status", "TEXT"),
        ("issue_date", "DATE"), ("branch_id", "TEXT"), ("department_id", "TEXT"),
        ("portfolio_id", "TEXT"), ("source_system", "TEXT"),
    ], "PRIMARY KEY (card_id)", card_accounts),
    ("06_product_holding", "product_holding", [
        ("holding_id", "BIGINT"), ("cif", "TEXT"), ("product_category", "TEXT"), ("product_code", "TEXT"),
        ("product_name", "TEXT"), ("status", "TEXT"), ("opened_date", "DATE"), ("branch_id", "TEXT"),
        ("department_id", "TEXT"), ("portfolio_id", "TEXT"), ("source_system", "TEXT"),
    ], "PRIMARY KEY (holding_id)", product_holdings),
    ("07_interaction_history", "interaction_history", [
        ("interaction_id", "BIGINT"), ("cif", "TEXT"), ("interaction_date", "DATE"), ("channel", "TEXT"),
        ("purpose", "TEXT"), ("notes", "TEXT"), ("branch_id", "TEXT"), ("department_id", "TEXT"),
        ("portfolio_id", "TEXT"), ("source_system", "TEXT"),
    ], "PRIMARY KEY (interaction_id)", interaction_history),
    ("08_customer_master", "customer_master", [
        ("data_date", "DATE"), ("region", "TEXT"), ("department_id", "TEXT"), ("branch_name", "TEXT"),
        ("branch_id", "TEXT"), ("portfolio_id", "TEXT"), ("rm_name", "TEXT"), ("cif", "TEXT"),
        ("id_card", "TEXT"), ("full_name", "TEXT"), ("dob", "DATE"), ("age", "BIGINT"),
        ("phone", "TEXT"), ("gender", "TEXT"), ("segment", "TEXT"), ("tier_name", "TEXT"),
        ("tier_start_date", "DATE"), ("tier_end_date", "DATE"), ("total_assets", "NUMERIC(24,6)"),
        ("address", "TEXT"),
    ], None, customer_master),
    ("09_data_grant", "data_grant", [
        ("username", "TEXT"), ("role_name", "TEXT"), ("branch_id", "TEXT"), ("can_view_pii", "INTEGER"),
    ], "PRIMARY KEY (username)", data_grants),
    ("10_leads", "leads", [
        ("lead_id", "TEXT"), ("cif", "TEXT"), ("full_name", "TEXT"), ("branch_id", "TEXT"),
        ("rm_name", "TEXT"), ("product_code", "TEXT"), ("product_name", "TEXT"), ("action_type", "TEXT"),
        ("status", "TEXT"), ("notes", "TEXT"), ("created_by", "TEXT"), ("created_at", "TIMESTAMP"),
    ], "PRIMARY KEY (lead_id)", leads),
    ("11_product_catalog", "product_catalog", [
        ("product_code", "TEXT"), ("product_name", "TEXT"), ("product_category", "TEXT"),
        ("target_segment", "TEXT"), ("priority", "INTEGER"), ("rule_description", "TEXT"), ("rule_sql", "TEXT"),
    ], "PRIMARY KEY (product_code)", product_catalog),
    ("12_offer_history", "offer_history", [
        ("offer_id", "BIGINT"), ("cif", "TEXT"), ("product_code", "TEXT"), ("product_name", "TEXT"),
        ("offer_date", "DATE"), ("channel", "TEXT"), ("response_status", "TEXT"),
        ("response_date", "DATE"), ("notes", "TEXT"),
    ], "PRIMARY KEY (offer_id)", offer_history),
]

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

for file_stem, table_name, cols, pk, rows in TABLES:
    col_names = [c[0] for c in cols]

    # 1. Write CSV (UTF-8 with BOM-free clean header for AIDP)
    csv_path = os.path.join(CSV_DIR, f"{file_stem}.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=col_names)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: ("" if r.get(k) is None else r.get(k)) for k in col_names})

    # 2. Write PostgreSQL .sql file
    sql_path = os.path.join(SQL_DIR, f"{file_stem}.sql")
    col_defs = [f"    {name} {dtype}" for name, dtype in cols]
    if pk:
        col_defs.append(f"    {pk}")
    ddl = f"DROP TABLE IF EXISTS {table_name};\nCREATE TABLE {table_name} (\n" + ",\n".join(col_defs) + "\n);\n"

    with open(sql_path, "w", encoding="utf-8") as f:
        f.write(f"-- VietABank Customer 360 POC - {table_name.upper()} (postgres)\n")
        f.write(f"-- Generated: {DATA_DATE.isoformat()}\n")
        f.write("SET client_encoding = 'UTF8';\nSET standard_conforming_strings = on;\nBEGIN;\n\n")
        f.write(ddl)
        if rows:
            f.write(f"INSERT INTO {table_name} ({', '.join(col_names)}) VALUES\n")
            val_lines = []
            for r in rows:
                vals = ", ".join(sql_val(r.get(k)) for k in col_names)
                val_lines.append(f"({vals})")
            f.write(",\n".join(val_lines) + ";\n")
        f.write("COMMIT;\n")

    # 3. Load into unified SQLite DB
    cur.executescript(ddl)
    if rows:
        placeholders = ", ".join("?" for _ in col_names)
        cur.executemany(
            f"INSERT INTO {table_name} ({', '.join(col_names)}) VALUES ({placeholders})",
            [[r.get(k) for k in col_names] for r in rows],
        )

conn.commit()
conn.close()

print("Generated VietABank Customer 360 dataset successfully!")
for file_stem, table_name, _, _, rows in TABLES:
    print(f"  {file_stem:26s} -> {len(rows):4d} rows")
