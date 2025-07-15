# 🎓 AI Packet Analyzer for Attack Detection

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Scapy](https://img.shields.io/badge/Scapy-PacketSniffing-green?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-Dashboard-teal?style=for-the-badge)
![Sklearn](https://img.shields.io/badge/Sklearn-AI-orange?style=for-the-badge)

## 🚀 Mô tả

**AI Packet Analyzer** là hệ thống:
- **Sniff packet real-time** trên mạng.
- **Trích xuất features**: entropy, packet size, protocol.
- **AI (RandomForest)** phân loại **Malicious / Benign**.
- **Dashboard realtime FastAPI + WebSocket** hiển thị kết quả.
- Phục vụ nghiên cứu **Attack Detection** và SOC Automation.

## 🛠️ Yêu cầu hệ thống

- Python 3.10+
- pip
- Linux (Ubuntu, Kali, Arch, Termux), hoặc WSL
- Quyền root (để sniff packet)

## 📦 Cài đặt

```bash
git clone https://github.com/Yuri08loveElaina/ai-packet-analyzer.git
cd ai-packet-analyzer

pip install -r requirements.txt
```

## ⚙️ Hướng dẫn sử dụng

### 1️⃣ Huấn luyện mô hình

```bash
python ai_model.py
```
Tạo file `packet_model.pkl` dùng cho phân tích packet.

### 2️⃣ Chạy Dashboard

```bash
python server_dashboard.py
```
Truy cập:
```
http://localhost:8000
```

### 3️⃣ Chạy Packet Sniffer

Mở **terminal mới**, chạy:
```bash
sudo python packet_sniffer.py
```

Hệ thống sẽ:
✅ Sniff packet real-time.  
✅ Gửi kết quả phân loại lên dashboard qua WebSocket.  
✅ Hiển thị `src`, `dst`, `size`, `label` (BENIGN/MALICIOUS).

## 🧩 Cấu trúc thư mục

```
.
├── ai_model.py          # Train & save AI model
├── packet_sniffer.py    # Sniff packet + analyze
├── server_dashboard.py  # FastAPI dashboard
└── requirements.txt     # Dependencies
```

## 🎯 Tính năng chính

✅ Sniff packet real-time với Scapy.  
✅ Trích xuất feature:
- **Entropy** payload.
- **Packet size** (normalized).
- **Protocol type** (normalized).

✅ AI phân loại packet (RandomForest).  
✅ Dashboard realtime quan sát.  
✅ Dễ mở rộng sang:
- Kết nối SIEM tự động block IP.
- Lưu PCAP nghi ngờ.
- Phân tích payload malware nâng cao.

## 🛡️ Ứng dụng thực tế

✅ Hệ thống SOC mini nghiên cứu.  
✅ Phát hiện bất thường, phân loại zero-day traffic.  
✅ Bổ sung module honeypot để thu thập mẫu.  
✅ Bảo vệ hệ thống doanh nghiệp / phòng lab thực nghiệm.

## 🚦 TODO

- [ ] Thu thập dataset thực tế để train model tốt hơn.
- [ ] Tích hợp Elastic/Grafana để trực quan lịch sử.
- [ ] Triển khai Docker/K8s cho môi trường sản xuất.
- [ ] Thêm module phân tích gói TLS (JA3 Fingerprinting).

## 🪐 License

MIT © 2025 [Yuri08loveElaina](https://github.com/Yuri08loveElaina)

