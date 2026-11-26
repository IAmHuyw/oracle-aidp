# Từ điển thuật ngữ Oracle AI Data Platform (AIDP) cho người mới

> Danh sách các thuật ngữ tiếng Anh xuất hiện trong khóa học **Oracle AI Data Platform: Data Foundations for Analytics and AI**, kèm giải thích dễ hiểu bằng tiếng Việt. File này sẽ được cập nhật thêm sau mỗi module.

---

## Module 1: Oracle AI Data Platform Foundations

| Thuật ngữ | Nghĩa / Giải thích dễ hiểu cho người mới |
|---|---|
| **Oracle AI Data Platform (AIDP)** | Dịch vụ đám mây do Oracle quản lý sẵn hạ tầng (*managed cloud service*), gom mọi công việc dữ liệu (lưu trữ, phân quyền, làm sạch, chạy code, tự động hóa, chia sẻ, kết nối AI) vào **một không gian làm việc thống nhất có quản trị**. |
| **Managed Cloud Service** | Dịch vụ đám mây mà nhà cung cấp (Oracle) tự lo phần máy chủ, cài đặt, nâng cấp, bảo trì — bạn chỉ cần vào dùng. |
| **Governance (Data Governance)** | **Quản trị dữ liệu**: Bộ quy tắc kiểm soát *ai được xem/sửa dữ liệu gì*, dữ liệu có đáng tin và hợp lệ không, ai đã truy cập lúc nào (tuân thủ quy định & bảo mật). |
| **Governed Workspace** | Không gian làm việc có sẵn cơ chế quản trị, phân quyền và theo dõi bảo mật ngay từ đầu — không phải làm xong mới gắn bảo mật rời rạc. |
| **Fragmented Enterprise Data** | **Dữ liệu doanh nghiệp phân mảnh**: Dữ liệu nằm rải rác ở nhiều hệ thống/phòng ban khác nhau (file Excel, CRM, ERP, database riêng...), khó gom lại dùng chung. |
| **Curated Data / Business-Ready Assets** | Dữ liệu đã được chọn lọc, làm sạch, chuẩn hóa theo đúng định nghĩa nghiệp vụ — sẵn sàng để sếp xem báo cáo hoặc cho AI dùng ngay mà không sợ sai lệch. |
| **Data Pipeline** | **Đường ống dữ liệu**: Chuỗi các bước tự động đưa dữ liệu đi từ nguồn gốc (raw) → làm sạch → biến đổi → lưu ra bảng kết quả cuối cùng. |
| **Orchestration / Workflows** | **Điều phối / Luồng công việc tự động**: Lập lịch và sắp xếp thứ tự chạy nhiều bước xử lý dữ liệu (ví dụ: Bước 1 xong thì tự chạy Bước 2, lỗi thì báo). |
| **Data Engineer** | **Kỹ sư dữ liệu**: Người xây dựng đường ống dữ liệu (pipeline), tự động hóa workflow và tối ưu tài nguyên tính toán. |
| **Data Analyst** | **Chuyên viên phân tích dữ liệu**: Người tìm kiếm, truy vấn (query) và phân tích dữ liệu để tạo báo cáo, rút ra insight cho kinh doanh. |
| **Data Scientist** | **Nhà khoa học dữ liệu**: Người xây dựng mô hình Machine Learning (học máy) và phân tích nâng cao trên tài nguyên tính toán lớn. |
| **Data Steward** | **Người giám hộ/quản trị dữ liệu**: Người giám sát chất lượng dữ liệu, quyền riêng tư (privacy), phân quyền và tuân thủ quy định (compliance) trong tổ chức. |
| **Data Warehouse** | **Kho dữ liệu truyền thống**: Mạnh về dữ liệu có cấu trúc rõ ràng (dạng bảng hàng-cột), quản trị chặt và truy vấn SQL nhanh cho báo cáo BI; nhưng kém linh hoạt với file thô (PDF, ảnh, log, JSON phức tạp). |
| **Data Lake** | **Hồ dữ liệu**: Lưu trữ được khối lượng khổng lồ đủ loại dữ liệu thô (có cấu trúc lẫn phi cấu trúc) với chi phí rẻ và linh hoạt; nhưng nếu thiếu quản trị rất dễ biến thành "đầm lầy dữ liệu" lộn xộn. |
| **Data Lakehouse** | **Kiến trúc Nhà-Hồ dữ liệu**: Kết hợp điểm mạnh của cả hai — vừa linh hoạt & lưu trữ lớn như *Data Lake*, vừa có quản trị, bảo mật và truy vấn bảng đáng tin cậy như *Data Warehouse*. |
| **Metadata** | **Siêu dữ liệu** ("dữ liệu mô tả dữ liệu"): Thông tin về tên bảng, tên cột, kiểu dữ liệu, chủ sở hữu, ngày cập nhật, mô tả ý nghĩa... giống như mục lục/nhãn dán trên thùng hàng. |
| **Catalog** | **Danh mục dữ liệu**: Nơi đăng ký, tổ chức và quản lý tất cả các tài sản dữ liệu (database, bảng, file...) tập trung, giúp tìm kiếm và phân quyền dễ dàng. |
| **Audit (Audit Log)** | **Nhật ký kiểm toán**: Ghi lại lịch sử *ai đã làm gì, xem bảng nào, thay đổi gì, vào lúc nào* để kiểm tra bảo mật khi cần. |
| **Lineage (Data Lineage)** | **Nguồn gốc / Dòng chảy dữ liệu**: Bản đồ truy vết xem một bảng dữ liệu cuối cùng được tạo ra từ những nguồn nào và đi qua những bước biến đổi nào. |
| **Medallion Architecture** | **Kiến trúc Huy chương**: Cách tổ chức dữ liệu theo 3 mức độ sẵn sàng tăng dần: **Bronze** (thô) → **Silver** (đã làm sạch & làm giàu) → **Gold** (tinh tuyển sẵn sàng cho báo cáo & AI). |
| **Bronze Tier** | Tầng **Đồng** trong Medallion Architecture — lưu dữ liệu thô nguyên bản ngay khi vừa nạp (*ingest*) từ hệ thống nguồn. |
| **Silver Tier** | Tầng **Bạc** — dữ liệu từ Bronze đã được làm sạch (*cleaned*), sắp xếp (*organized*), sửa lỗi (*corrected*) và bổ sung thêm ngữ cảnh (*enriched*). |
| **Gold Tier** | Tầng **Vàng** — dữ liệu từ Silver đã được tổng hợp, tinh tuyển (*curated*) thành các bảng chuẩn nghiệp vụ cho báo cáo BI, ML và AI Agent. |
| **Ingest / Ingestion** | **Nạp dữ liệu**: Quá trình đưa dữ liệu từ các hệ thống bên ngoài vào trong nền tảng (ví dụ: đổ vào tầng Bronze). |
| **Apache Spark** | Công cụ **xử lý dữ liệu phân tán** mã nguồn mở cực mạnh — chia nhỏ khối lượng dữ liệu lớn ra nhiều máy để xử lý song song cực nhanh. |
| **Delta Lake** | Định dạng bảng mở dành cho Lakehouse giúp dữ liệu lưu trên Data Lake vẫn đáng tin cậy như database (không bị hỏng bảng khi ghi lỗi, hỗ trợ xem lại lịch sử phiên bản). |
| **Delta Sharing** | Giao thức mở giúp **chia sẻ dữ liệu có kiểm soát** cho hệ thống/đối tác khác **mà không cần sao chép nhân bản dữ liệu** sang nơi mới. |
| **Apache Iceberg / Apache Hudi** | Hai định dạng bảng mở phổ biến khác trong thế giới Lakehouse (cùng nhóm với Delta Lake). AIDP hỗ trợ tương tác (*interoperability*) với các định dạng này. |
| **JDBC Connectivity** | Chuẩn kết nối phổ biến (**Java Database Connectivity**) giúp các công cụ phân tích / BI bên ngoài kết nối vào và đọc dữ liệu đã được quản trị trong AIDP. |
| **BI (Business Intelligence) Tools** | Công cụ trực quan hóa và báo cáo kinh doanh (tạo biểu đồ, dashboard), ví dụ như **Oracle Analytics Cloud (OAC)**, Power BI, Tableau... |
| **Agentic AI / AI Agent** | **AI tác tử**: Ứng dụng AI không chỉ trả lời chat mà còn có thể **tự tra cứu dữ liệu, đối chiếu quy định và dùng công cụ được cấp phép để thực hiện hành động** (ví dụ: phát hiện hóa đơn sai quy định và soạn email nhắc nhân viên). |
| **Guardrails** | **Hàng rào an toàn cho AI**: Các quy tắc giới hạn để AI Agent không nói bậy, không tự ý thực hiện hành động vượt quyền hoặc làm lộ dữ liệu nhạy cảm. |
| **RBAC (Role-Based Access Control)** | **Phân quyền theo vai trò**: Thay vì cấp quyền lẻ tẻ cho từng người, ta tạo các vai trò (ví dụ: Analyst, Engineer, Steward), gán quyền cho vai trò rồi gán người vào vai trò đó. *(Sẽ học sâu ở Module 3)* |

---

## Module 2: Provision an AIDP Instance

| Thuật ngữ | Nghĩa / Giải thích dễ hiểu cho người mới |
|---|---|
| **Provisioning** | **Khởi tạo tài nguyên đám mây**: Quá trình cấu hình và tạo ra một hệ thống mới (instance) trên cloud để sẵn sàng sử dụng. |
| **OCI (Oracle Cloud Infrastructure)** | Nền tảng điện toán đám mây của Oracle (tương tự AWS của Amazon hay Azure của Microsoft) — nơi AIDP chạy trên đó. |
| **OCI IAM (Identity and Access Management)** | Hệ thống **quản lý danh tính và phân quyền** của OCI, gồm **Users** (người dùng), **Groups** (nhóm), **Policies** (chính sách quyền) và **Permissions** (quyền thao tác). |
| **Tenancy** | **Tài khoản thuê bao đám mây tổng** của cả công ty/tổ chức trên OCI (cấp cao nhất, chứa mọi compartment bên trong). |
| **Compartment** | **Ngăn chứa logic** trên OCI dùng để gom nhóm tài nguyên theo phòng ban/dự án và giới hạn ai được phép chạm vào tài nguyên nào. |
| **Region** | **Khu vực địa lý** đặt trung tâm dữ liệu đám mây (ví dụ: Singapore, Tokyo, US East...) nơi tài nguyên của bạn được tạo ra. |
| **Tags (Required Tags)** | **Nhãn phân loại** gắn lên tài nguyên cloud (ví dụ: tên dự án, trung tâm chi phí). Nếu compartment đặt luật bắt buộc có tag mà bạn bỏ trống thì sẽ không tạo được instance. |
| **Workbench Instance** | Thể hiện hệ thống AIDP tổng thể được khởi tạo — môi trường bảo mật chung cho mọi hoạt động dữ liệu, phân tích và AI. |
| **Initial / Default Workspace** | **Không gian làm việc đầu tiên** được tạo kèm khi khởi tạo instance, là nơi tổ chức notebooks, workflows và libraries của dự án. |
| **Autonomous AI Lakehouse (ALH)** | Cơ sở dữ liệu Lakehouse tự quản trị tích hợp AI của Oracle. Kết nối ALH (bản mới hoặc có sẵn từ **26ai** trở lên) là điều kiện để mở khóa các tính năng **AI-native** trong AIDP. |
| **AI-Native Capabilities** | Các tính năng AI cốt lõi tích hợp sâu trong nền tảng: **Knowledge Bases** *(cơ sở tri thức)*, **Agent Flows** *(luồng AI Agent)* và **AI Compute** *(tính toán cho AI)*. |
| **Knowledge Base** | **Cơ sở tri thức**: Kho tài liệu/dữ liệu chuẩn hóa (như file chính sách công ty) mà AI Agent có thể tra cứu để trả lời chính xác dựa trên sự thật. |
| **Encryption Key** | **Chìa khóa mã hóa**: Dùng để mã hóa dữ liệu lưu trữ nhằm ngăn kẻ gian đọc trộm nếu lộ file lưu trữ. |
| **Oracle-Managed Key** | Khóa mã hóa do **Oracle tự tạo và tự quản lý** (mặc định, đơn giản nhất). |
| **Customer-Managed Key** | Khóa mã hóa do **chính công ty bạn tự giữ và quản lý** qua OCI Vault — kiểm soát bảo mật cao hơn nhưng đi kèm trách nhiệm vận hành (mất/tắt khóa sẽ mất truy cập dữ liệu). |
| **OCI Vault** | **Két sắt lưu khóa mã hóa** trên OCI giúp công ty tự quản lý chìa khóa bảo mật, xoay vòng khóa (*key rotation*) và theo dõi kiểm toán (*audit trail*). |
| **Key Rotation** | **Xoay vòng khóa**: Thay khóa mã hóa định kỳ theo quy định bảo mật để giảm rủi ro nếu khóa cũ bị lộ. |
| **Policy Scope (Standard vs. Advanced)** | **Phạm vi áp dụng chính sách quyền** khi khởi tạo AIDP: **Standard** áp dụng rộng ở cấp **Tenancy** (dễ dùng), còn **Advanced** giới hạn hẹp trong **Compartment** (kiểm soát chặt hơn). |
| **Private Network** | **Mạng riêng nội bộ** không mở công khai ra Internet — thường cần bật thêm **Optional policies** để AIDP kết nối an toàn vào nguồn dữ liệu bên trong. |

---

## Module 3: Data Foundation, Catalogs, and Governance

| Thuật ngữ | Nghĩa / Giải thích dễ hiểu cho người mới |
|---|---|
| **Master Catalog** | **Danh mục tổng** ở cấp cao nhất trong AIDP, là bản đồ chứa tất cả các Catalog (Standard & External) và tài sản dữ liệu được quản trị. |
| **Standard Catalog** | Catalog mà **AIDP tự lưu trữ và quản lý trực tiếp** cả cấu trúc, tài sản (Tables, Volumes, Knowledge Bases, Models) lẫn metadata. |
| **External Catalog** | Catalog kết nối tới dữ liệu nằm ở **hệ thống bên ngoài**; AIDP chỉ đồng bộ (*synchronize*) metadata để tìm kiếm & truy vấn mà **không copy dữ liệu** vào AIDP. |
| **`OCI_AI_MODELS`** | **Schema dành riêng (reserved schema)** nằm sẵn trong `default` catalog, liệt kê các mô hình ngôn ngữ lớn nền tảng (*Foundation LLMs*) từ **OCI Generative AI** sẵn sàng để dùng trong AIDP. |
| **Schema** | **Ngăn chứa con bên trong Catalog** giúp gom nhóm các tài sản dữ liệu và AI liên quan (Tables, Volumes, Knowledge Bases, Models) cho gọn gàng và dễ phân quyền. |
| **Table (Managed vs. External)** | **Bảng dữ liệu có cấu trúc** (hàng & cột). **Managed Table** do AIDP lưu cả dữ liệu & metadata; **External Table** chỉ lưu metadata trỏ tới file trong OCI Object Storage. |
| **Volume (Managed vs. External)** | **Kho chứa file và thư mục cho dữ liệu phi cấu trúc** (PDF, DOCX, TXT, ảnh...). **Managed Volume** do AIDP quản lý cả dữ liệu & metadata; **External Volume** chỉ quản lý metadata trỏ tới một Bucket/Folder sẵn có trên OCI Object Storage. |
| **OCI Object Storage** | Dịch vụ lưu trữ file dạng đối tượng (tương tự ổ đĩa đám mây dung lượng cực lớn theo cấu trúc **Compartment → Bucket → Folder/File**) trên OCI. |
| **Bucket** | "Thùng chứa" logic cấp cao nhất bên trong OCI Object Storage để đựng các file và thư mục. |
| **Partition Key** | **Khóa phân vùng**: Cột dùng để chia nhỏ dữ liệu bảng theo nhóm (ví dụ theo ngày/tháng hoặc khu vực) giúp truy vấn nhanh hơn vì chỉ cần đọc đúng phần cần thiết. |
| **RAG (Retrieval-Augmented Generation)** | Kỹ thuật cho AI **tra cứu tài liệu thật trước rồi mới trả lời** (giúp AI trả lời đúng theo chính sách công ty thay vì tự bịa). |
| **Vector Embeddings** | **Biểu diễn vector số học**: Biến đoạn văn bản thành dãy số phản ánh *ý nghĩa* của câu chữ để máy tính tìm được đoạn văn có ý nghĩa tương đồng (**Semantic Search**). |
| **Embedding Model** | Mô hình AI chuyên biến văn bản thành Vector Embeddings. Trong AIDP Demo có 2 lựa chọn: `ALL_MINILM_L12_V2` (chỉ tiếng Anh) và `MULTILINGUAL_E5_SMALL` (100 ngôn ngữ). |
| **Chunk Size & Chunk Overlap** | Khi lập chỉ mục tài liệu cho Knowledge Base, văn bản dài được cắt thành từng mẩu nhỏ (**Chunk**). **Chunk size** là độ dài mỗi mẩu (tính theo ký tự); **Chunk overlap** là phần ký tự lặp chồng giữa 2 mẩu kế nhau để không bị đứt ý giữa chừng. |
| **Auto Populate Catalog** | Công cụ **trích xuất metadata tự động** từ file trong OCI Object Storage (CSV, JSON, Avro, ORC, Parquet, Delta Lake) để tự tạo schemas, tables và partitions hàng loạt (có thể bật chế độ duyệt tay *Manual approval*). |
| **Credential Store** | **Kho lưu trữ thông tin bí mật tập trung** (token, mật khẩu, tài khoản dịch vụ) trong AIDP giúp code & AI Agent xác thực an toàn mà **không dán cứng (hardcode)** bí mật trong code. |
| **OCID (Oracle Cloud Identifier)** | Mã định danh dài và duy nhất do Oracle cấp cho mọi tài nguyên trên OCI (user, vault secret, bucket, instance...). |
| **MCP Server (Model Context Protocol Server)** | Cầu nối chuẩn giúp **AI Agent** giao tiếp và gọi công cụ/dữ liệu từ hệ thống bên ngoài (như Oracle Analytics Cloud) một cách có kiểm soát. |
| **System Roles (`AI_DATA_PLATFORM_ADMIN` & `AUDITOR`)** | 2 vai trò mặc định của hệ thống AIDP. `AI_DATA_PLATFORM_ADMIN` có toàn quyền quản trị và **chỉ 1 người duy nhất** được giữ tại một thời điểm; `AUDITOR` chỉ được xem Audit Logs. |
| **Principal / Principal Type** | **Đối tượng được gán quyền hoặc thêm vào Role** — trong AIDP gồm 3 loại: **User** (người dùng lẻ), **Group** (nhóm OCI IAM), và **Role** (vai trò AIDP khác). |
| **Hierarchical Inheritance** | **Kế thừa phân cấp**: Khi cấp quyền trên đối tượng cha (vd: Catalog), đối tượng con bên trong (vd: Table) tự động được thừa hưởng quyền đó. *(Lưu ý: Workspace, Folder và Compute là các cây phân quyền tách biệt!)* |
| **Least-Privilege Access** | **Nguyên tắc đặc quyền tối thiểu**: Chỉ cấp cho mỗi vai trò/người dùng/AI Agent đúng lượng quyền tối thiểu cần để làm việc, không cấp thừa. |
| **Notifications vs. Audit Logs** | **Notifications** báo kết quả tức thời các tác vụ vận hành (upload xong, job lỗi...); **Audit Logs** là nhật ký kiểm toán lưu dài hạn ghi rõ *ai thay đổi gì và kết quả ra sao*. |

---

## Module 4: Create and Organize Workspaces and Compute Resources

| Thuật ngữ | Nghĩa / Giải thích dễ hiểu cho người mới |
|---|---|
| **Workspace** | **Không gian làm việc dự án** — vùng chứa logic gom Files, Folders, Notebooks, Workflows, Jobs, Compute Clusters và Experiments của một dự án/nhóm. |
| **Workspace Isolation** | **Cô lập không gian làm việc**: Tách biệt cả về mặt **vận hành** *(Operational: compute, jobs, logs, quotas không tranh chấp nhau)* lẫn **tổ chức** *(Organizational: team, phân quyền, vòng đời dev/test/prod)*. |
| **Quota** | **Hạn mức tài nguyên** tối đa được phép dùng trong một workspace hoặc ngăn chứa để tránh một dự án ngốn hết tài nguyên chung. |
| **VCN & Subnet** | **Virtual Cloud Network** *(mạng đám mây riêng ảo)* và **Subnet** *(mạng con)* trên OCI — cần khai báo nếu bật **Private Network** cho Workspace để nối tới nguồn dữ liệu nội bộ. |
| **Compute Cluster** | **Cụm máy tính đa năng (All-purpose compute)** chạy Spark/CPU/GPU dùng cho hầu hết việc trong AIDP: chạy Notebooks, scripts, Workflows, Jobs, Knowledge Base ingestion và Auto-populate catalog. |
| **Driver Node & Worker Nodes** | Trong cụm xử lý phân tán Spark: **Driver node** là "máy trưởng" điều phối công việc; **Worker nodes** là các "máy thợ" cùng xử lý dữ liệu song song. |
| **OCPU (Oracle CPU)** | Đơn vị đo sức mạnh vi xử lý CPU trên Oracle Cloud (1 OCPU tương đương 1 nhân CPU vật lý hỗ trợ đa luồng). |
| **Autoscale** | **Tự động co giãn tài nguyên**: Cluster tự tăng thêm số Worker nodes khi việc nặng và tự thu nhỏ lại (trong khoảng min–max) khi rảnh để tiết kiệm chi phí. |
| **Idle Timeout** | **Thời gian chờ tự tắt khi rảnh**: Tự động tắt Compute Cluster nếu không có ai chạy tác vụ trong một khoảng thời gian (vd: 120 hoặc 180 phút) để tránh tốn tiền cloud. |
| **Init Script** | **Kịch bản khởi tạo**: Đoạn script tự chạy mỗi khi Compute Cluster khởi động để cài đặt môi trường hoặc cấu hình nâng cao. |
| **Spark UI** | Giao diện giám sát kỹ thuật của Apache Spark giúp theo dõi tiến độ chạy job, tác vụ nào đang chậm và tối ưu hiệu năng. |
| **AI Compute** | **Tài nguyên tính toán chuyên biệt cho AI Agents** — chỉ dùng cho việc thử nghiệm (**Agent Playground**) và phục vụ AI Agent đã triển khai (**Deployed Agent Endpoints**). |
| **Compute Replicas** | **Các bản sao tính toán**: Nhân bản thêm các bản sao của AI Compute để tăng sức chịu tải khi nhiều người dùng cùng gọi AI Agent một lúc. |
| **Agent Playground** | Sân chơi thử nghiệm tương tác giúp lập trình viên chat, kiểm thử và tinh chỉnh AI Agent trước khi đưa ra chạy thực tế (production). |
| **Endpoint (Deployed Agent Endpoint)** | Địa chỉ API/cổng kết nối ổn định để ứng dụng bên ngoài gọi và tương tác với AI Agent đã triển khai. |
| **ML Experiment** | **Thí nghiệm Học máy**: Nơi ghi nhận và so sánh nhiều lần chạy huấn luyện mô hình (*training runs*) với thuật toán/dữ liệu khác nhau để chọn mô hình chuẩn nhất. |
| **Git Folder** | Thư mục trong AIDP Workspace liên kết trực tiếp với một kho mã nguồn **Git** bên ngoài (GitHub, Bitbucket, GitLab, OCI DevOps) hỗ trợ `commit`, `push`, `pull`, `merge`. |
| **Personal Access Token (PAT)** | **Mã thông báo truy cập cá nhân** (tạo trên GitHub/Git provider) dùng thay mật khẩu để cấp quyền cho AIDP kết nối và đồng bộ code an toàn với kho Git của bạn. |
