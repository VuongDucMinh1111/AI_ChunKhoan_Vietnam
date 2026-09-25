# HỆ THỐNG GIAO DỊCH CHỨNG KHOÁN VIỆT NAM BẰNG TRÍ TUỆ NHÂN TẠO (AI QUANT)

Hệ thống tích hợp toàn diện từ cào dữ liệu, xử lý đặc trưng, học máy (Machine Learning), học tăng cường (Reinforcement Learning), quản trị rủi ro Bayes đến giao diện Web/Desktop.

---

## 📁 CẤU TRÚC HỆ THỐNG THEO TỪNG BƯỚC (STEPS)

Dự án được quy hoạch theo từng bước rõ ràng:

### 1. Các Module Lõi (Core Engine)
- `quan_tri_rui_ro.py`: Quản trị rủi ro vốn, bộ lọc Expected Value (EV) và Cầu dao cắt lỗ động (Dynamic Stop-loss).
- `uoc_luong_bat_dinh_bayes.py`: Mạng Bayesian Neural Network (MC Dropout) đo lường phương sai/độ tự tin của mô hình trước khi cho phép vào lệnh.
- `phan_tich_cam_xuc_tin_tuc.py`: Động cơ tổng hợp cảm xúc tin tức đa AI kết hợp trọng số độ uy tín nguồn tin.
- `moi_truong_giao_dich_rl.py`: Môi trường Gym giao dịch chứng khoán đa mã cổ phiếu phục vụ huấn luyện Reinforcement Learning.
- `agent_q_learning.py`: Thuật toán Q-Learning tự học bằng bảng Q-Table thuần Numpy.

### 2. Quy Trình Thực Thi Từng Bước (Steps)
- `Step1_Thu_Thap_Va_Tao_Dac_Trung.py`: Tự động tải dữ liệu giá 50 mã cổ phiếu lớn (VN30 & Midcaps) qua Yahoo Finance, trích xuất chỉ báo kỹ thuật (RSI, MACD, OBV, ATR), vĩ mô và dòng tiền ngoại.
- `Step2_Huan_Luyen_Machine_Learning.py`: Huấn luyện các mô hình phân loại xu hướng giá (LightGBM, Random Forest, Neural Network MLP).
- `Step3_Huan_Luyen_AI_Hoc_Tang_Cuong.py`: Huấn luyện Agent tự động trading bằng thuật toán PPO (Proximal Policy Optimization) trên môi trường 50 mã cổ phiếu.
- `Step4_Kiem_Thu_Va_Quet_Thi_Truong.py`: Kiểm thử chiến lược lịch sử (Backtest) Out-of-sample và quét radar tìm mã cổ phiếu tiềm năng kèm bộ lọc rủi ro.
- `Step5_Giao_Dien_Web_Dashboard.py`: Bảng điều khiển Web Dashboard trực quan viết bằng Streamlit (Giám sát Real-time, MLOps Retraining, Lịch sử lệnh).
- `Step6_Giao_Dien_Desktop_App.py`: Ứng dụng Desktop Window viết bằng Tkinter.

### 3. Phím Tắt Khởi Động Nhanh (1-Click Launchers)
- `Chay_Giao_Dien_Web.bat`: Kích hoạt ngay Web Dashboard.
- `Chay_Giao_Dien_Desktop.bat`: Kích hoạt ngay Desktop App.

---

## 🚀 HƯỚNG DẪN CÀI ĐẶT & CHẠY

### 1. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

### 2. Chạy thử nghiệm từng bước:
- **Bước 1 (Thu thập dữ liệu):**
  ```bash
  python Step1_Thu_Thap_Va_Tao_Dac_Trung.py
  ```
- **Bước 2 (Huấn luyện Machine Learning):**
  ```bash
  python Step2_Huan_Luyen_Machine_Learning.py
  ```
- **Bước 3 (Huấn luyện Học tăng cường PPO):**
  ```bash
  python Step3_Huan_Luyen_AI_Hoc_Tang_Cuong.py
  ```
- **Bước 4 (Backtest & Quét Radar):**
  ```bash
  python Step4_Kiem_Thu_Va_Quet_Thi_Truong.py
  ```
- **Bước 5 (Giao diện Web Streamlit):**
  ```bash
  streamlit run Step5_Giao_Dien_Web_Dashboard.py
  ```
- **Bước 6 (Giao diện Desktop):**
  ```bash
  python Step6_Giao_Dien_Desktop_App.py
  ```

---

## 📤 HƯỚNG DẪN ĐẨY LÊN GITHUB

1. Tạo một repository mới trên GitHub (ví dụ: `ai-chung-khoan-vn`).
2. Mở terminal tại thư mục này và chạy các lệnh sau:
```bash
git remote add origin <URL_REPOSITORY_CUA_BAN>
git branch -M main
git push -u origin main
```
