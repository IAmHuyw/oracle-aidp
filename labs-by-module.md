# Hướng dẫn Thực hành Hands-on theo từng Module (Module 2 → Module 7)

> **Lưu ý:** **Module 1** là phần kiến thức nền tảng (không có bài Lab thao tác). Từ **Module 2 đến Module 7**, các bài thực hành nối tiếp nhau để xây trọn vẹn kịch bản **Expense Compliance Pipeline** từ con số 0.  
> *Hướng dẫn bên dưới được tổng hợp sát từng bước thao tác thực tế trong 11 bài Demo của khóa học. Nếu bạn mở môi trường **Request Lab** và cuốn **Activity Guide** trên Oracle MyLearn, có thể dùng checklist này làm xương sống và đối chiếu tên tài nguyên/tài khoản riêng của môi trường Lab.*

---

## Lab Module 2: Khởi tạo một AIDP Instance (Provisioning)

**Mục tiêu:** Tạo mới 1 AIDP Workbench Instance + Autonomous AI Lakehouse (ALH) từ OCI Console và truy cập kho code mẫu.

- [ ] **Bước 1:** Đăng nhập **OCI Console** → mở menu điều hướng → **Analytics & AI** → **AI Data Platform** → **AI Data Platform Workbench**.
- [ ] **Bước 2:** Bấm **Create AI Data Platform Workbench** *(OCI sẽ tự kiểm tra quyền IAM `manage` trên compartment)*.
- [ ] **Bước 3:** Nhập tên:
  - **Workbench Instance Name:** `expense AIDP` *(hoặc tên dự án của bạn)*
  - **Default / Initial Workspace Name:** đặt tên workspace mặc định.
- [ ] **Bước 4 — Cấu hình Autonomous AI Lakehouse (ALH):**
  - Chọn **`Create new`** *(hoặc chọn ALH có sẵn từ bản **`26ai`** trở lên để bật các tính năng AI-native)*.
  - Giữ Username `ADMIN` và đặt **Password** mạnh cho tài khoản ADMIN.
- [ ] **Bước 5 — Mã hóa lưu trữ (Storage Encryption):**
  - Chọn **`Oracle-managed key`** *(mặc định — lưu ý không thể đổi sau khi tạo!)*.
- [ ] **Bước 6 — Advanced Options & Tags:**
  - Mở **Show advanced options** kiểm tra nếu compartment có yêu cầu **Required Tags** thì điền đầy đủ.
- [ ] **Bước 7 — Add Policies (Policy Scope):**
  - Chọn **`Standard`** *(Tenancy level — khuyên dùng để dễ bắt đầu)*.
- [ ] **Bước 8:** Bấm **Create** và chờ khoảng **5+ phút** → khi trạng thái sẵn sàng, bấm vào tên instance (đăng nhập nếu được hỏi) để mở **AIDP Homepage**.
- [ ] **Bước 9:** Tại mục **Sample code**, bấm **Browse** để mở kho GitHub `oracle-samples/oracle-aidp-samples` tham khảo các thư mục mẫu (`ai`, `data-engineering`, `getting-started`...).

---

## Lab Module 3: Catalogs, Data Assets, Auto Populate, Credential Store & RBAC

**Mục tiêu:** Tổ chức toàn bộ tài sản dữ liệu (Bảng, File, Knowledge Base) trong Master Catalog, lưu bí mật an toàn và phân quyền chuẩn theo vai trò.

### Lab 3.1 — Tạo External Catalog (`expenses_db`)
- [ ] Vào **Master catalog** (menu trái) → xem 2 catalog có sẵn (`default` chứa schema `OCI_AI_MODELS` + external catalog của ALH mặc định).
- [ ] Bấm **Create Catalog** → đặt tên `expenses_db`, **Catalog Type:** `External Catalog`.
- [ ] Chọn **External Source Type** (vd Autonomous AI Lakehouse ngoài) → upload file **Wallet**, nhập **Wallet password**, **DB Username/Password** và **Service level**.
- [ ] Bấm **Test Connection** → thành công thì bấm **Create** → mở vào kiểm tra các schema & bảng đồng bộ sang.

### Lab 3.2 — Tạo Standard Catalog, Schema & Tables (`acme_expenses`)
- [ ] Quay lại **Master catalog** → **Create Catalog** → tên `acme_expenses`, **Catalog Type:** `Standard` → **Create**.
- [ ] Mở `acme_expenses` → bấm **`+`** tạo schema tên **`expenses`**.
- [ ] Vào schema `expenses` → tab **Tables** → bấm **`+`**:
  - **Tạo Managed Table:** Chọn upload file dữ liệu từ máy tính → chọn định dạng file + Advanced options → bấm **Preview Data** → **Create**. Vào tab **Columns** thử thêm mô tả cột.
  - **Tạo External Table:** Chọn Table type **`External`** → định dạng **`CSV`** (bật `Data has headers`, `UTF-8`, delimiter `,`) → **Location type:** `OCI Object Storage` → chọn **Compartment, Bucket, Folder** → **Preview Data** → đặt tên `acme_expense_preview_training` → **Create**.

### Lab 3.3 — Tạo Volumes & Knowledge Base cho RAG (`expense_policies_kb`)
- [ ] Trong schema `expenses` → tab **Volumes** → bấm **`+`**:
  - Tạo **Managed Volume** tên `expense_policies` → mở volume → bấm **`+`** upload các file chính sách (**PDF / DOCX / TXT**) hoặc tạo subfolder.
  - Tạo **External Volume** tên `external_volume` → chọn `External` → chọn Compartment, Bucket, Folder trên OCI Object Storage → **Create**.
- [ ] Chuyển sang tab **Knowledge Bases** → bấm **`+`**:
  - **Name:** `expense_policies_kb`
  - **Cluster used for ingestion:** để trống *(dùng default master catalog compute)*.
  - **Embedding model:** chọn `ALL_MINILM_L12_V2` *(tiếng Anh)* hoặc `MULTILINGUAL_E5_SMALL` *(đa ngôn ngữ/tiếng Việt)*.
  - **Chunk size:** `100` | **Chunk overlap:** `25` → **Create**.
- [ ] Mở `expense_policies_kb` → tab **Data Sources** → **Add** → chọn volume/folder `expense_policies` *(nhớ: chỉ chọn được Volume hoặc Folder, không chọn file lẻ!)* → theo dõi trạng thái nạp dữ liệu (hoặc bấm **Ingest Now**).

### Lab 3.4 — Auto Populate Catalog (Quét metadata tự động)
- [ ] Menu trái → **Auto-populate catalog** → bấm **`+`** tạo Metadata Extractor.
- [ ] Nhập **Name:** `object storage extract` và **Description** *(bắt buộc)*.
- [ ] Chọn **Standard Catalog** đích (`default`), chọn **Compute cluster**, chọn **Compartment / Bucket / Folder** (hoặc nhập URI).
- [ ] Chọn **Create entities:** `Manually`, **Schema:** `default` → **Create**.
- [ ] Đợi trạng thái chuyển `In-progress` → `In review` → mở extractor → tab **Entities awaiting review** → kiểm tra cột (đổi tên bảng nếu cần) → bấm **Accept all → Submit** → kiểm tra bảng mới trong `Master catalog → default → default → Tables`.

### Lab 3.5 — Lưu bí mật trong Credential Store (`oac_token`)
- [ ] Menu trái → **Credential store** → bấm **`+`**.
- [ ] **Name:** `oac_token` | **Credential type:** `Secret token`.
- [ ] Nhập key `access token` và giá trị token → **Create** *(khi hết hạn, bấm **Edit** để xoay/cập nhật giá trị mới)*.

### Lab 3.6 — Thiết lập Phân quyền RBAC (`AI_Agent_Developers`)
- [ ] Menu trái → **Roles** → bấm **`+`** → tạo role tên **`AI_Agent_Developers`**.
- [ ] Mở role → tab **Members** → bấm **`+`** thêm thành viên theo `User` (OCID hoặc Compartment/Domain) và `Group` (OCI IAM Group).
- [ ] Cấp quyền trên **từng đối tượng đích** *(nhớ: Workspace, Folder, Compute là các cây phân quyền riêng!)*:
  1. `Master catalog → acme_expenses → Permissions → +`: cấp **`MANAGE`** cho Role `AI_Agent_Developers` *(làm tương tự cho `expenses_db`; mở 1 bảng con kiểm tra kế thừa)*.
  2. *(Sau khi làm Lab 4.1–4.2)* `Workspaces → expense_compliance → Permissions → +`: cấp **`Privileged User`**.
  3. `Content → expense_medallion → Permissions → +`: cấp **`Manage`** và **tick chọn `Inherit to all subfolders and items`**.
  4. `Compute → expense_cluster → Permissions → +`: cấp **`USE`**.
  5. `Compute → AI Compute → expense_ai_compute → Permissions → +`: cấp **`USE`**.

---

## Lab Module 4: Workspaces, Compute Clusters, AI Compute, Experiments & Git Folder

**Mục tiêu:** Dựng không gian làm việc riêng, tạo tài nguyên tính toán và kết nối GitHub quản lý mã nguồn.

### Lab 4.1 — Tạo Workspace & Cấu trúc thư mục Medallion
- [ ] Menu trái → **Workspaces** → **Create** → đặt tên **`expense_compliance`** → **Create**.
- [ ] Mở `expense_compliance` → bấm **`+`** tạo thư mục **`expense_medallion`**.
- [ ] Bên trong `expense_medallion`, tạo 3 thư mục con: **`bronze`**, **`silver`**, **`gold`**.
- [ ] Import 3 file notebook tương ứng vào từng thư mục con *(từ Lab Files hoặc kho mẫu)*.

### Lab 4.2 — Tạo Compute Cluster & AI Compute
- [ ] Trong `expense_compliance` → **Compute** → tab **Clusters** → bấm **`+`**:
  - **Cluster name:** `expense_cluster`
  - **Configuration:** chọn **`Quickstart`**, giữ **`Autoscale`** bật.
  - **Idle timeout:** đổi thành **`180`** phút → **Create**.
  - Khi cluster chuyển sang `Active`, mở xem các tab `Spark UI`, `Logs`, `Metrics`, `Connection Details` và `Library`.
- [ ] Chuyển sang tab **AI compute** → bấm **`+`**:
  - **Name:** `expense_ai_compute`
  - **Compute replicas:** `1` | **OCPUs:** `1` | **Memory:** `16 GB` → **Create**.

### Lab 4.3 — Tạo ML Experiment
- [ ] Trong `expense_compliance` → **Experiments** → **Create** → đặt tên **`expense_review_classifier`** → **Create**.

### Lab 4.4 — Kết nối GitHub & Tạo Git Folder
- [ ] Trên **GitHub**: vào `Settings → Developer Settings → Personal Access Tokens → Tokens (Classic)` (hoặc Fine-grained) → tạo token mới và copy.
- [ ] Trên **AIDP**: `Settings → User → Git linked accounts → + Add credential` → chọn **GitHub**, đặt tên credential, nhập email và dán **Personal Access Token** → **Add**.
- [ ] Trong Workspace `expense_compliance → Content → + → Git folder`:
  - Chọn Git credential vừa tạo, dán **Git Repository URL**, đặt **Git folder name** (`git_folder`) và **Branch name** (`main`) → **Create**.
- [ ] Mở `git_folder`: vào tab **Content** upload thử 1 file → chuyển sang tab **Git**, tick file thay đổi, nhập commit message → bấm **Commit & Push** để xác nhận đồng bộ thành công.

---

## Lab Module 5: Chạy Notebooks Medallion (Bronze → Silver → Gold), LLM & MLflow

**Mục tiêu:** Chạy toàn bộ pipeline 3 tầng bằng code, gọi LLM qua `query_model`, huấn luyện & đăng ký mô hình ML và xuất bản bảng Gold sang External Catalog.

- [ ] **Lab 5.1 — Chạy Bronze Notebook & Gọi LLM:**
  - Mở `expense_medallion/bronze/01_acme_expense_bronze_tier.ipynb`.
  - Thanh trên cùng: **Cluster → Attach existing cluster → `expense_cluster`**.
  - Thử dùng sidebar **Master catalog**: chuột phải một bảng (xem cú pháp 3 phần `acme_expenses.expenses.acme_expenses`) và chuột phải một model trong `default → oci_ai_models` chọn **Copy sample code** (xem hàm `query_model(...)` cho cả PySpark & SQL `%%sql`).
  - Chạy từng cell rồi chạy hết notebook → kiểm tra các bảng mới tạo trong `acme_expenses.bronze`.
- [ ] **Lab 5.2 — Chạy Silver Notebook & MLflow Model Registry:**
  - Mở Silver notebook (`02_acme_expense_silver_tier.ipynb`) → chạy để làm sạch bảng Silver, huấn luyện các mô hình ứng viên qua **MLflow** và đăng ký mô hình có **AUC** cao nhất vào Model Registry (`acme_expenses.silver.expense_review_classifier`).
  - Mở sidebar **Experiments → `expense_review_classifier`** kiểm tra `Metrics`, `Parameters`, `Artifacts`.
  - Mở **Master catalog → `acme_expenses` → `silver` → `Models`** xác nhận mô hình đã đăng ký (`Details`, `Versions`, `Artifacts`).
- [ ] **Lab 5.3 — Chạy Gold Notebook & Publish sang ALH:**
  - Mở `expense_medallion/gold/03_acme_expense_gold_tier.ipynb` → chạy để chấm điểm dữ liệu (`manual_review_threshold = 0.50`) và tạo các bảng Gold (`expenses_scored_gold`, `expense_review_queue_gold`, `expense_review_summary_gold`...).
  - Kiểm tra trong **Master catalog → `expenses_db` → `expenses`** xác nhận bảng `expenses_scored_gold` đã được xuất bản thành công sang External Catalog.

---

## Lab Module 6: Tự động hóa bằng Workflows, If-Else, Lập lịch & Giám sát

**Mục tiêu:** Ghép 3 notebook thành 1 Job tự động có kiểm tra ngưỡng chất lượng mô hình, đặt lịch chạy định kỳ và theo dõi log.

- [ ] **Lab 6.1 — Tạo Job `medallion` với 4 Tasks:**
  - Trong Workspace `expense_compliance` → **Workflow** → **Create job** → đặt tên **`medallion`** → **Create**.
  - **Task 1 (`bronze_tier`):** `Notebook task` → chọn Bronze notebook, `expense_cluster`, timeout `1 Hour`.
  - **Task 2 (`silver_tier`):** `Notebook task` → chọn Silver notebook *(cuối notebook có `oidlutils.parameters.setTaskValue('model_accuracy', ...)`)*, `Depends on: bronze_tier`, `Run if: All dependencies have executed and succeeded`.
  - **Task 3 (`accuracy_check`):** `If-else condition` → `Depends on: silver_tier` → đặt điều kiện:
    `{{tasks.silver_tier.values.model_accuracy}} >= 0.99` *(dùng `0.99` để test nhánh False; production đặt `0.9`)*.
  - **Task 4 (`gold_tier`):** `Notebook task` → chọn Gold notebook, `Depends on: accuracy_check true`.
- [ ] **Lab 6.2 — Chạy thử, Xem Graph/Timeline & Đặt lịch:**
  - Bấm **Run now** → vào tab **Runs → View** → quan sát tab **`Graph`** (xác nhận `gold_tier` ở trạng thái `Excluded` khi đặt ngưỡng `0.99`), tab **`Timeline`** và tab **`Details`** (xem cluster logs & nút **`Repair run`**).
  - Quay lại `medallion.job` → tab **Details** → mục **Schedule → Add** → tạo lịch `Calendar` chạy `Weekly` vào `Sunday` (chọn múi giờ & giờ 24h), trạng thái `Active` → **Create**.
  - Xem thử mục **Job parameters → Add value** để biết các System Parameters (`{{job.run_id}}`, `{{job.repair_count}}`...).
- [ ] **Lab 6.3 — Kiểm tra Notifications & Audit Logs:**
  - Menu trái → **Notifications**: lọc `Operation type = RUN_WORKFLOW_JOB` hoặc `Status = Failed` để xem cột `Message`.
  - Menu trái → **Audit logs**: tìm kiếm theo đường dẫn `expense_medallion/gold` để kiểm tra chi tiết lịch sử thao tác và OCID người thực hiện.

---

## Lab Module 7: Chia sẻ dữ liệu (Delta Sharing) & Kết nối Oracle Analytics Cloud (OAC)

**Mục tiêu:** Chia sẻ bảng Delta ra hệ thống ngoài không copy dữ liệu và vẽ dashboard trên OAC từ bảng Gold.

### Lab 7.1 — Tạo Delta Share & Truy cập từ Python/Spark bên ngoài
- [ ] Menu trái → **Data sharing** → bấm **`+`** tạo share tên **`expense_data_share`**.
- [ ] Tab **Assets** → bấm **`+`** thêm schema **`silver`** *(chỉ chia sẻ được Delta tables)*.
- [ ] Tab **Recipients** → bấm **`+`** tạo recipient **`audit_team`** (+ email nếu muốn) → mở tab **Details** kích hoạt (hoặc gửi one-time activation link) → mở link lấy **Credential Profile** lưu thành file `.share` (vd `aidp_demo.share`).
- [ ] Trên máy ngoài (vd VS Code + Python/PySpark): đọc thử bảng bằng `spark.read.format("deltaSharing").load(f"{profile_path}#share.schema.table")` và thử làm mới **Bearer Token** *(hạn mặc định 90 ngày)*.
- [ ] Quay lại **AIDP Notebook**, chạy câu lệnh sau để kiểm tra ngày hết hạn token và endpoint của recipient:
  ```python
  spark.sql("DESCRIBE recipient audit_team").show(truncate=False)
  ```

### Lab 7.2 — Kết nối Oracle Analytics Cloud (OAC) & Tạo Workbook
- [ ] Trong AIDP: `Workspaces → expense_compliance → Compute → expense_cluster → Connection details` → bấm icon **Oracle Analytics Cloud** để tải file **`config.json`**.
- [ ] Trên **OCI Console**: vào **Profile → Tokens and Keys** kiểm tra (hoặc tạo mới) **API Key** cho user tạo AIDP instance / user Admin, copy **Fingerprint**.
- [ ] Mở file `config.json` kiểm tra **`fingerprint`** khớp với API key và **`region`** khớp chính xác region của AIDP instance → lưu lại.
- [ ] Mở **Oracle Analytics Cloud (OAC)**:
  - **Create → Connection → Oracle AI Data Platform** → đặt tên **`expenses_AIDP`**.
  - Upload **`config.json`** *(tự điền DSN, User OCID, Tenancy OCID, Region, Fingerprint)*.
  - Upload file **Private API Key (`.pem`)** tương ứng.
  - Chọn **Catalog:** `acme_expenses` *(nhớ: chỉ chọn được 1 Standard Catalog duy nhất)* → **Save**.
- [ ] **Create → Data Set** → chọn connection `expenses_AIDP` → mở schema `gold` → kéo bảng `expenses_scored_gold` → **Save**.
- [ ] Bấm **Create Workbook** → thử tạo biểu đồ: `Amount` theo `Business Unit`, cờ `Missing Receipt` / `Meal Limit`, và khối lượng chi phí theo `Submission Month`.
