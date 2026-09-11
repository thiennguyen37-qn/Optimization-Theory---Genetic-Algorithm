# CLAUDE.md

## Quy ước file tạm
Các file `tmp` ở thư mục gốc là file tạm, dùng để thử nghiệm và xem lại trước khi đưa nội dung chính thức vào report.

## File Report Review.md
File `Report Review.md` ở thư mục gốc dùng để tổng hợp các lỗi phát hiện được và các ý muốn sửa đổi khi review báo cáo. File này không đưa vào repo (đã thêm vào `.gitignore`). Mỗi khi file này được cập nhật, phải đọc lại nội dung và sửa report theo đúng yêu cầu đã ghi trong đó.

Khi người dùng nhập đúng từ "Updated" vào đoạn chat, tự động đọc lại `Report Review.md`, tiến hành sửa report theo các yêu cầu ghi trong đó, rồi báo cáo lại kết quả đã sửa trên đoạn chat.

## Quy tắc làm việc
- Không tự ý commit và push khi chưa có lệnh rõ ràng từ người dùng.
- Trong quá trình làm việc, nếu có điểm nào không chắc chắn hoặc chưa hiểu rõ, phải hỏi lại người dùng trước khi tiếp tục, không tự suy diễn.
- Khi commit, phải chia nhỏ theo từng thay đổi có mục đích riêng biệt, tránh dồn nhiều sửa đổi không liên quan vào một commit, để việc review sau này được dễ dàng.

## Văn phong
- Viết rõ ràng, mạch lạc, theo chuẩn học thuật, nghiêm túc.
- Cấm sử dụng các từ ngữ dân dụng gây khó chịu hoặc khó hiểu cho người đọc.
- Không chia ý thành các câu ngắn, rời rạc, thiếu liên kết; các câu và đoạn văn phải có sự kết nối logic rõ ràng.
