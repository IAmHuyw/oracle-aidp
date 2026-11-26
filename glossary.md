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
