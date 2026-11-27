# Hướng dẫn thực hành Lab: Customer 360 và Next Best Action trên AIDP

> **Dự án:** Phân hệ AI Customer 360 (PGBank)  
> **Nền tảng:** AI Data Platform (AIDP)

> **Lưu ý về dữ liệu:** Toàn bộ dữ liệu là **giả lập** phục vụ học tập. Tên ngân hàng trong dữ liệu gốc (ví dụ "LPBank Visa Platinum", "Ứng dụng LPBank") được giữ nguyên theo quyết định ngày 2026-11-26. Bảng `offer_history` và tài liệu quy trình thẻ dùng số liệu minh hoạ.

---

## 1\. Tổng quan bài toán và mục tiêu

Trong ngân hàng, dữ liệu khách hàng nằm rải rác ở nhiều hệ thống: Core Banking, CRM, Thẻ, Tín dụng, DWH. Bộ lab này hướng dẫn học viên xây dựng phân hệ **Customer 360 có AI Agent** theo một chu trình khép kín:

1. **Hợp nhất dữ liệu đa nguồn:** gom dữ liệu từ 7 hệ thống nguồn quanh một mã định danh duy nhất là **CIF**.  
2. **Hiểu khách hàng và đối soát:** dựng chân dung tài chính, phát hiện chỗ lệch giữa Core Banking và CRM.  
3. **Next Best Offer (NBO) và Next Best Action (NBA):** AI Agent dùng các luật trong danh mục sản phẩm để gợi ý **sản phẩm** nên bán chéo và **hành động** tiếp theo cho cán bộ quản lý khách hàng (RM).  
4. **Tra cứu quy trình nội bộ có căn cứ (RAG):** AI trả lời về điều kiện, thủ tục kèm trích dẫn nguồn.  
5. **Thực thi hành động:** AI soạn Lead bán hàng; con người xác nhận rồi mới ghi vào CRM.  
6. **Bảo mật và phân quyền:** mỗi cán bộ chỉ thấy khách hàng thuộc chi nhánh mình (Row-Level Security); CCCD và SĐT bị che với tài khoản không có quyền xem.

---

## 2\. Bản đồ 12 bảng dữ liệu

Mỗi bảng có 2 file trong thư mục `sql_tables/`:

- **`.sql`**: nạp vào PostgreSQL.  
- **`.db`**: SQLite, mở xem ngay.

Ngoài ra, file `customer360.db` ở thư mục gốc chứa đủ 12 bảng, dùng để chạy truy vấn JOIN.

```
                         ┌──────────────────────────────┐
                         │  ĐỊNH DANH TRUNG TÂM (CIF)   │
                         └──────────────┬───────────────┘
        ┌──────────────────┬────────────┴─────┬───────────────────┐
┌───────▼────────┐ ┌───────▼────────┐ ┌───────▼────────┐ ┌────────▼─────────┐
│  CORE BANKING  │ │  CARD SYSTEM   │ │   CRM & DWH    │ │  VẬN HÀNH AGENT  │
├────────────────┤ ├────────────────┤ ├────────────────┤ ├──────────────────┤
│01 core_customer│ │05 card_account │ │02 crm_customer │ │09 data_grant     │
│03 deposit_acc. │ │                │ │07 interaction  │ │10 leads          │
│04 loan_account │ │                │ │08 cust_master  │ │11 product_catalog│
│06 prod_holding │ │                │ │                │ │12 offer_history  │
└────────────────┘ └────────────────┘ └────────────────┘ └──────────────────┘
```

&nbsp;

| STT | Bảng | Số dòng | Nguồn | Ý nghĩa trong lab |
| :---: | :---- | ----: | :---- | :---- |
| 01 | `core_customer` | 45.000 | Core Banking | Định danh và số dư tổng theo Core Banking |
| 02 | `crm_customer` | 45.004 | CRM | Thông tin liên hệ, phân khúc (Priority, Affluent, Mass, SME), số dư theo CRM. Có 4 khách chỉ có trong CRM (xem Lab 2\) |
| 03 | `deposit_account` | 89.794 | Deposits | Từng tài khoản tiết kiệm, chứng chỉ tiền gửi, ngày mở, ngày đáo hạn (`maturity_date`) |
| 04 | `loan_account` | 13.094 | LOS (Tín dụng) | Khoản vay: loại vay, dư nợ gốc, dư nợ còn lại, lãi suất |
| 05 | `card_account` | 20.168 | Cards (CMS) | Thẻ ghi nợ và thẻ tín dụng, hạn mức (`credit_limit`), dư nợ thẻ |
| 06 | `product_holding` | 168.308 | Nhiều hệ thống | Các sản phẩm khách đang nắm giữ (CASA, tiết kiệm, thẻ…) |
| 07 | `interaction_history` | 112.156 | CRM / DWH | Nhật ký tiếp xúc đa kênh (tổng đài, chi nhánh, ứng dụng…): mục đích, ghi chú |
| 08 | `customer_master` | 45.004 | DWH | Hồ sơ tổng hợp, **bản rút gọn 20 cột định danh** (file gốc có 112 cột, đã bỏ vector embedding) |
| 09 | `data_grant` | 3 | Quản trị dữ liệu | Phân quyền theo chi nhánh và cờ xem dữ liệu nhạy cảm (`can_view_pii`) |
| 10 | `leads` | 0 | CRM | Bảng rỗng, nhận Lead khi AI Agent thực thi hành động |
| 11 | `product_catalog` | 5 | Quản lý sản phẩm | 5 sản phẩm cốt lõi kèm luật gợi ý: bằng lời (`rule_description`) và bằng SQL (`rule_sql`) |
| 12 | `offer_history` | 800 | **Giả lập** | Lịch sử chào mời có nhãn (428 `ACCEPTED`, 372 `REJECTED`) cho bài toán học máy mở rộng |

&nbsp;