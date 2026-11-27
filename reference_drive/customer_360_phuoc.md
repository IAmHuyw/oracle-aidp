Username: admin  
Password: IndaV4@Bql0vOXG  
Đăng nhập tại: [http\://138.2.103.239:3004/](http://138.2.103.239:3004/)

Phân Quyền:  
Username: nv.chinhanh.hn\_01   
Password: IndaV4@Bql0vOXG  
Đăng nhập tại: [http\://138.2.103.239:3004/](http://138.2.103.239:3004/)

## **CUSTOMER 360**

“Em xin phép trình bày tính năng Customer360 trên nền tảng AI của TPBank. Phần demo này em sẽ dựa vào kịch bản thực tế Customer360 – chúng ta sẽ đi từ xem hồ sơ khách hàng, dùng AI tư vấn sản phẩm, tra cứu kho tri thức cho tới khởi tạo Lead để chăm sóc khách hàng.” (vietnqs thêm: Toàn bộ dữ liệu theo bộ dữ liệu POC giả lập gồm có cấu trúc và phi cấu trúc)

“Em sẽ bắt đầu với Customer 360: Thay vì hỏi chatbot trước, cán bộ có thể trực tiếp tìm khách hàng đang chuẩn bị làm việc. Ở đây chúng ta đang xem hồ sơ của khách hàng Bùi Lan Chi (CIF: 113628). Từ một CIF, hệ thống có thể liên kết những thông tin của khách hàng nằm rải rác ở nhiều hệ thống khác nhau.”

Điểm quan trọng: 

1. Nền tảng của Customer 360 không phải AI, mà là dữ liệu khách hàng được liên kết chuẩn xác. CIF đóng vai trò định danh trung tâm để kết nối như thông tin khách hàng, phân khúc, chi nhánh, tiền gửi, sản phẩm, tài khoản và lịch sử tương tác.   
2. Chỉ khi có một Customer 360 đủ tin cậy thì AI phía trên mới có ngữ cảnh tốt để phân tích.  
3. Như vậy, cán bộ đã có cái nhìn tổng quan về khách hàng.   
4. Thay vì đọc thủ công từng mục, chúng ta có thể chuyển toàn bộ bối cảnh dữ liệu này sang cho AI phân tích ngay.  
5. vietnqs thêm:  Mọi thứ chạy ở local bao gồm cả AI

### **Hỏi đáp dữ liệu & Tra cứu kho tri thức**

“Em xin sử dụng tính năng Hỏi AI. AI sử dụng ngữ cảnh Customer 360 để tổng hợp thông tin quan trọng thành nhận định ban đầu. Như vậy chúng ta chuyển từ: Có dữ liệu về khách hàng sang Hiểu khách hàng.”

“Dựa trên những thông tin tổng hợp này, cán bộ quản lý khách hàng có thể nhanh chóng nắm bắt được nhu cầu hiện tại cũng như lịch sử tương tác gần đây mà không cần phải tốn thời gian tra cứu rải rác.”

“Và chúng ta cũng có thể tìm hiểu thêm về lịch sử tương tác của khách hàng đó.”⁷

Nhập câu hỏi: "Cho tôi các thông tin tương tác gần nhất của khách hàng”

“Sau khi nắm rõ tổng quan hồ sơ, bước tiếp theo của RM không chỉ là dừng lại ở việc nắm bắt thông tin mà là biến thông tin thành hành động mang lại giá trị kinh doanh: Với khách hàng này, chúng ta nên tư vấn thêm sản phẩm gì?”

Nhập câu hỏi: “Với khách hàng này thì tôi nên tư vấn thêm sản phẩm gì?”

“Đây là nơi dữ liệu Customer 360 bắt đầu được chuyển thành hành động. AI không chỉ nói khách hàng đang có gì, mà sử dụng hồ sơ hiện tại để gợi ý sản phẩm hoặc hành động tiếp    theo cho cán bộ. Nói cách khác, hành trình đã chuyển từ: Nhìn khách hàng sang Hiểu khách hàng đến việc Xác định nên làm tiếp theo.”

### **Gợi ý sản phẩm phù hợp và hành động**

“Sau khi xác định sản phẩm phù hợp, cán bộ có thêm một câu hỏi rất thực tế: Nếu muốn tư vấn sản phẩm này thì tôi phải làm như thế nào? Người dùng không cần biết tên quy định, mã văn bản hay điều khoản cụ thể.”

Nhập câu hỏi: “Tôi muốn bán Thẻ tín dụng quốc tế LPBank Visa Platinum cho khách hàng thì thủ tục và quy trình làm như thế nào?”

“Ở đây, AI chuyển từ dữ liệu Customer 360 sang kho tri thức và quy định nội bộ. Hệ thống sẽ đưa ra hướng dẫn các bước cần thực hiện đồng thời cung cấp Citation (nguồn trích dẫn). Điểm quan trọng là câu trả lời này phải có căn cứ từ tài liệu chứ không do model tự tạo. Nếu cán bộ cần kiểm tra sâu hơn, có thể mở trực tiếp tài liệu nguồn để xem nội dung. Như vậy chúng ta chuyển từ: AI trả lời sang AI trả lời có căn cứ và có thể kiểm chứng.”

“Sau khi đã nắm được các quy định và các bước thực hiện, nếu đánh giá đây là cơ hội bán hàng tiềm năng, chúng ta có thể tiến hành tạo lead chăm sóc khách hàng ngay trên giao diện.”

### **AI tạo lead đẩy sang hệ thống CRM**

Nhập lệnh: “Tạo lead cho khách hàng trên”

“Anh chị có thể quan sát thấy, hệ thống sẽ mở ra một form xác nhận minh bạch chứ hoàn toàn không tự ý tạo dữ liệu ngầm.”

“Trên màn hình lúc này, toàn bộ thông tin khách hàng như chị Bùi Lan Chi đã được tự động điền theo bối cảnh. Sản phẩm quan tâm cũng được đề xuất chính xác là thẻ Visa Platinum từ cuộc trao đổi trước đó, đồng thời cán bộ vẫn có thể chủ động bổ sung các ghi chú riêng nếu cần. Sau khi rà soát kỹ lưỡng, chúng ta mới bấm xác nhận để hoàn tất.”

“Điều này thể hiện rất rõ nguyên tắc cốt lõi: AI đóng vai trò phân tích, tổng hợp và chuẩn bị, còn quyền quyết định thực thi cuối cùng luôn nằm trong tay con người.”

### **Bảo mật, Masking**

“Như vậy, chúng ta đã đi qua toàn bộ chu trình nghiệp vụ thực tế — từ tra cứu Customer 360, tư vấn sản phẩm, tra cứu quy định cho tới khởi tạo Lead. Đến đây, một câu hỏi then chốt được đặt ra: Làm thế nào để đảm bảo toàn bộ dữ liệu nhạy cảm này chỉ được truy cập đúng người, đúng thẩm quyền? Đó chính là lý do yếu tố Bảo mật và Phân quyền dữ liệu được thiết kế chặt chẽ ngay từ nền tảng.”

“Bây giờ, em xin phép chuyển sang một tài khoản có quyền hạn thấp hơn để kiểm tra tính năng bảo mật.”

“Nền tảng AI tuân thủ nghiêm ngặt cơ chế phân quyền. AI chỉ phản hồi đúng trong phạm vi quyền hạn của tài khoản đang đăng nhập.”

Tình huống: Chuyển sang tài khoản không có quyền tra cứu thông tin khách hàng.  
Nhập câu hỏi: “Hồ sơ 360 khách hàng CIF 113628 (Bùi Lan Chi): tổng quan tiền gửi, khoản vay, thẻ và các lưu ý rủi ro?”  
Hoặc nhấp vào một câu hỏi mặc định.

“Anh chị có thể thấy, hệ thống lập tức từ chối truy cập do tài khoản không đủ quyền. Điều này giúp đảm bảo dữ liệu khách hàng luôn được bảo vệ an toàn tuyệt đối.”

“Bên cạnh việc chặn truy cập hoàn toàn, hệ thống còn hỗ trợ tính năng che thông tin nhạy cảm (Data Masking) cho các vai trò chỉ được phép xem một phần dữ liệu.”

“Như anh chị thấy, thông tin nhạy cảm như Số căn cước công dân đã được tự động che bớt giúp đảm bảo tuân thủ bảo mật nhưng vẫn vận hành hiệu quả. ”

