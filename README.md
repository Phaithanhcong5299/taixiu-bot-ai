# 🤖 Bot Tài Xỉu AI – Sun.Win Auto Collector & Predictor

Bot Python tự động thu thập kết quả trò chơi Tài/Xỉu từ Sun.Win và dự đoán kết quả ván tiếp theo bằng phương pháp Pattern Voting + mô hình học sâu LSTM.

## 🚀 Tính năng

- ✅ Tự đăng nhập Sun.Win và thu thập kết quả: mã ván, xúc xắc, tổng, kết quả thật
- 📄 Ghi dữ liệu vào Google Sheets (Main + Sheet 100 ván mới nhất)
- 🔍 Phát hiện chuỗi bị đứt (mất kết nối)
- 🧠 Dự đoán kết quả tiếp theo bằng:
  - Pattern Voting (chuỗi 5 gần nhất)
  - LSTM (tự huấn luyện và cập nhật)
- 📊 Ghi đúng/sai và tính % chính xác
- 🔁 Tự reconnect và hoạt động 24/7
- 🛡️ credentials.json được giữ riêng tư (không đưa vào GitHub)

## 🛠️ Cách sử dụng

1. **Clone repo này về máy**:
   ```bash
   git clone https://github.com/Phaithanhcong5299/taixiu-bot-ai.git
   cd taixiu-bot-ai
   ```

2. **Đặt file `credentials.json` vào thư mục này** (Google API key của bạn)

3. **Cài đặt thư viện cần thiết**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Chạy bot**:
   ```bash
   python main.py
   ```

✅ Bot sẽ tự thu thập và ghi dữ liệu dự đoán vào Google Sheets của bạn.

---

## 📋 Cấu trúc Google Sheets

| Mã ván | Xúc xắc | Tổng | KQ thật | Voting | LSTM | Kết luận | Dự đoán cuối | Đúng/Sai | % Chính xác | Chuỗi đứt | Thời gian |
|--------|---------|------|---------|--------|------|----------|---------------|----------|--------------|-------------|-----------|

---

## 💡 Gợi ý

- Bạn có thể deploy bot này lên **Replit** hoặc **VPS** để chạy 24/7
- Chỉnh `pattern_len` trong `pattern_vote()` để tăng độ dài chuỗi
- Sau khi thu thập đủ > 1000 ván, mô hình LSTM sẽ chính xác hơn nhiều

---

## 📬 Liên hệ / Tác giả

Được xây dựng bởi Phaithanhcong5299 & trợ lý ChatGPT 🤝
