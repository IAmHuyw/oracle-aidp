# Oracle AI Data Platform: Data Foundations for Analytics and AI — Bộ tài liệu tự học

> Tổng hợp đầy đủ **7 module (28 bài học)** từ khóa học trên Oracle MyLearn (*thuộc lộ trình Become an Oracle AI Data Platform Professional*), biên soạn dễ hiểu cho người mới kèm giải thích mọi thuật ngữ tiếng Anh.

---

## Mục lục bài học

| Module | Chủ đề | Ghi chú chi tiết |
|---|---|---|
| **Module 1** | Oracle AI Data Platform Foundations *(AIDP, Data Lakehouse, Medallion Architecture, kịch bản Expense Compliance Agent)* | [module-01-foundations.md](./module-01-foundations.md) |
| **Module 2** | Provision an AIDP Instance *(OCI IAM, ALH 26ai, Encryption Keys, Policy Scope, Demo OCI Console)* | [module-02-provisioning.md](./module-02-provisioning.md) |
| **Module 3** | Data Foundation, Catalogs, and Governance *(Master/Standard/External Catalog, Tables, Volumes, Knowledge Bases, Auto Populate, Credential Store, RBAC, Audit Logs)* | [module-03-catalogs-governance.md](./module-03-catalogs-governance.md) |
| **Module 4** | Create and Organize Workspaces and Compute Resources *(Workspace Isolation, Compute Clusters vs. AI Compute, ML Experiments, Git Folders)* | [module-04-workspaces-compute.md](./module-04-workspaces-compute.md) |
| **Module 5** | Running Code in AIDP Notebooks *(Python/SQL/Scala, 3-part naming, `query_model`, MLflow & Model Registry, Medallion Notebooks)* | [module-05-notebooks.md](./module-05-notebooks.md) |
| **Module 6** | Automate Data Processing *(Jobs, 5 Task Types, Parameter Precedence, If-Else, Calendar/Cron Scheduling, Repair Run)* | [module-06-workflows.md](./module-06-workflows.md) |
| **Module 7** | Share and Integrate Data *(Delta Sharing, OAC Built-in Connector, JDBC/ODBC, Kafka Streaming, Oracle Fusion BICC)* | [module-07-share-integrate.md](./module-07-share-integrate.md) |
| **Từ điển** | **Từ điển thuật ngữ tiếng Anh → tiếng Việt xuyên suốt cả 7 module** | [glossary.md](./glossary.md) |
| **Thực hành** | **Hướng dẫn thực hành Hands-on từng bước theo Module (Module 2 → 7)** | [labs-by-module.md](./labs-by-module.md) |

---

## Cheat Sheet: 15 điểm cực quan trọng & bẫy hay ra thi

1. **Medallion Architecture:** **Bronze** *(thô nguyên bản)* → **Silver** *(đã làm sạch, sửa lỗi, làm giàu)* → **Gold** *(tinh tuyển chuẩn nghiệp vụ cho BI, ML và AI Agents)*.
2. **AIDP không tự thiết kế quy trình thay bạn:** AIDP cung cấp môi trường quản trị và tái sử dụng, nhưng đội ngũ vẫn tự quyết định cách ingest, clean, validate, curate và govern.
3. **Autonomous AI Lakehouse (ALH) khi Provisioning:** Dùng ALH có sẵn phải từ bản **`26ai` trở lên**. Nếu không nối ALH → vẫn xử lý dữ liệu có cấu trúc được nhưng **mọi tính năng AI-native (Knowledge Bases, Agent Flows, AI Compute) bị vô hiệu hóa**.
4. **Encryption Key là BẤT BIẾN (Immutable):** Không thể đổi giữa Oracle-managed key và Customer-managed key (OCI Vault) sau khi đã tạo AIDP instance — muốn đổi bắt buộc phải tạo instance mới và migrate sang.
5. **Required Tags:** Nếu OCI Compartment yêu cầu tags bắt buộc mà quên nhập khi tạo AIDP → khởi tạo sẽ **thất bại**.
6. **Reserved Schema `OCI_AI_MODELS`:** Nằm sẵn trong `default` catalog, chứa danh sách các mô hình LLM từ OCI Generative AI — gọi trực tiếp trong SQL/PySpark bằng hàm **`query_model(...)`**.
7. **Knowledge Bases (RAG):** Dùng Oracle Database 26ai Vector Search, nhận **PDF, DOCX, TXT**, nhưng **CHỈ nạp cả Volume hoặc Folder trong Volume (KHÔNG nạp trực tiếp 1 file lẻ!)**. Embedding model: `ALL_MINILM_L12_V2` *(chỉ tiếng Anh)* vs. `MULTILINGUAL_E5_SMALL` *(100 ngôn ngữ)*.
8. **System Role `AI_DATA_PLATFORM_ADMIN`:** Chỉ có **MỘT người dùng duy nhất** giữ role này tại một thời điểm trên mỗi instance (và tự động nằm trong `AUDITOR`).
9. **Cấp quyền RBAC đúng chỗ:** Quyền được cấp tại **tab `Permissions` của ĐỐI TƯỢNG ĐÍCH** (không phải trên trang Roles). Catalog kế thừa xuống Table, nhưng **Workspace, Folder và Compute là các cây phân quyền TÁCH BIỆT** (phải cấp riêng `USE` cho Compute/AI Compute và `Manage` + inherit cho Folder).
10. **Compute Cluster vs. AI Compute:** **Compute Cluster** *(All-purpose CPU/GPU)* chạy Notebooks, Workflows, KB ingestion, Auto-populate catalog; **AI Compute** *(scale bằng **Compute Replicas**)* **CHỈ** chạy Agent Playground & Deployed Agent Endpoints.
11. **Three-part Naming:** Mọi bảng trong cả Standard & External Catalog đều tham chiếu dạng **`catalog.schema.table`**.
12. **Parameter Precedence trong Workflows:** **`Job Run value` (cao nhất) → `Task value` → `Job value` (thấp nhất)**. Truyền giá trị giữa task bằng `oidlutils.parameters.setTaskValue(...)` và đọc bằng `{{tasks.<task_name>.values.<param_name>}}`.
13. **Repair Run:** Chỉ chạy lại các task bị lỗi đã chọn; **tham số truyền cho Repair Run chỉ áp dụng cho riêng lần sửa lỗi đó**.
14. **Delta Sharing:** **Chỉ chia sẻ Delta Tables / Schemas** *(KHÔNG chia sẻ Workspace files hay Volumes)*. Bearer token mặc định **90 ngày**; xem ngày hết hạn & endpoint bằng **`DESCRIBE recipient <name>`**.
15. **OAC Built-in Connector & Fusion BICC:** Mỗi kết nối OAC dùng `config.json` + Private API Key và **chỉ gắn tới 1 Standard Catalog duy nhất** *(không hỗ trợ External Catalog)*. Dữ liệu Oracle Fusion kéo vào AIDP qua **BICC → OCI Object Storage → External Table/Volume**.
