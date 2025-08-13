# 🚀 Code Challenger

Một nền tảng thử thách lập trình tự động sử dụng AI để tạo ra các câu hỏi coding và giúp developers nâng cao kỹ năng thông qua các bài tập với 3 mức độ Easy, Medium và Hard.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

## 📋 Mục Lục

- [Giới Thiệu](#giới-thiệu)
- [Tính Năng](#tính-năng)
- [Công Nghệ Sử Dụng](#công-nghệ-sử-dụng)
- [Cài Đặt](#cài-đặt)
- [Sử Dụng](#sử-dụng)
- [API Documentation](#api-documentation)

## 🎯 Giới Thiệu

Code Challenger là một nền tảng học tập lập trình được hỗ trợ bởi AI, được thiết kế để:

- 🤖 Tự động tạo câu hỏi coding sử dụng LLM models từ TogetherAI
- ⚡ Cung cấp giao diện trắc nghiệm đơn giản và thân thiện
- 📊 Theo dõi lịch sử thử thách và tiến độ cá nhân
- 🔒 Quản lý quota sử dụng hàng ngày cho từng user


## ✨ Tính Năng

### Core Features
- 🤖 **AI-Generated Questions**: Tự động tạo câu hỏi coding sử dụng LLM models từ TogetherAI
- 📝 **Multiple Choice Interface**: Giao diện trắc nghiệm đơn giản và user-friendly
- 📈 **Challenge History**: Xem lại lịch sử các thử thách đã hoàn thành
- 🔐 **User Authentication**: Đăng ký/đăng nhập với Clerk authentication
- ⏰ **Daily Usage Limits**: Hệ thống quản lý quota sử dụng hàng ngày
- 🔄 **Auto Provisioning**: Tự động cấp phát quota khi tạo tài khoản mới

### Technical Features
- 🚀 **FastAPI Backend**: RESTful API hiệu suất cao
- 🗄️ **SQLAlchemy ORM**: Quản lý database với schema system hoàn chỉnh
- 🔗 **Webhook Integration**: Tích hợp webhook với Ngrok cho development
- ⚛️ **React Frontend**: Giao diện modern và responsive

## 🛠️ Công Nghệ Sử Dụng

### Backend
- **Framework**: FastAPI (Python)
- **Database**: SQLAlchemy ORM
- **Authentication**: Clerk
- **AI Integration**: TogetherAI LLM Models
- **Development Tools**: Ngrok (webhooks)
- ### Key Dependencies
```toml
# Backend (pyproject.toml)
clerk-backend-api = ">=3.1.11"
fastapi = ">=0.116.1" 
openai = ">=1.98.0"
python-dotenv = ">=1.1.1"
sqlalchemy = ">=2.0.42"
svix = ">=1.70.0"
together = ">=1.5.21"
uvicorn = ">=0.35.0"
```

### Frontend
- **Framework**: React
- **UI Components**: Multiple-choice interface
- **State Management**: React hooks
- **Styling**: CSS/Tailwind CSS

### Infrastructure
- **API Architecture**: RESTful API
- **Webhook System**: Auto user provisioning
- **Database Schema**: Challenges, Challenge History, Daily Usage Limits

## 🚀 Cài Đặt

### Yêu Cầu Hệ Thống
- Python >= 3.8
- Node.js >= 16.0.0
- npm hoặc yarn
- Ngrok (cho development)

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/code-challenger.git
cd code-challenger
```
### 2. Setup Backend
```bash
cd backend
# Install uv if not already installed
pip install uv

# Install dependencies using uv
uv sync
```
### 3. Setup Frontend
```bash
cd frontend
npm install
```
### 4. Environment Configuration
Tạo file .env trong thư mục backend:
```
JWT_KEY= you_public_key

# TogetherAI
TOGETHER_AI_API_KEY=your_together_ai_key

# Clerk Authentication
CLERK_SECRET_KEY=your_clerk_secret_key
CLERK_WEBHOOK_SECRET=your_webhook_secret
```
Tạo file .env trong thư mục frontend:
```
# Clerk
VITE_CLERK_PUBLISHABLE_KEY= your_key
```
### 5. Database Setup
chạy ứng dụng
```
cd backend
python -m alembic upgrade head
```
### 6. Chạy Ứng Dụng
Development Mode
```# Terminal 1: Backend
cd backend
uv run server.py

# Terminal 2: Frontend  
cd frontend
npm run dev

# Terminal 3: Ngrok (for webhooks)
ngrok http 5000
```
Ứng dụng sẽ chạy tại:

- Frontend: http://localhost:3000
- Backend API: http://localhost:5000
- API Documentation: http://localhost:5000/docs
### 📖 Sử Dụng
Đăng Ký Tài Khoản

-  Truy cập trang chủ
-  Click "Sign Up" và đăng ký qua Clerk
-  Hệ thống tự động cấp phát daily quota
-  Bắt đầu thử thách ngay lập tức!

Thực Hiện Challenge

- Click "Generate New Challenge"
- AI sẽ tạo ra câu hỏi coding tự động
- Chọn đáp án đúng trong giao diện multiple-choice
- Xem kết quả và giải thích chi tiết
- Kiểm tra quota còn lại trong ngày

Xem Lịch Sử

- Vào mục "Challenge History"
- Xem lại tất cả challenges đã hoàn thành
- Review câu trả lời và điểm số
- Theo dõi tiến độ học tập

### 📚 API Documentation
API documentation được tạo tự động bằng FastAPI và có thể truy cập tại /docs.
Các Endpoints Chính
```
http# Challenge Management
POST /api/generate-challenges  # Tạo challenge mới với AI

#Các chức năng đăng kí đăng nhập do clerk đảm nhận 

# User Management
GET /api//my-history           # Lấy thông tin history
GET /api/quota                 # Kiểm tra daily quota
GET /api/webhooks/clerk        # Clerk webhook cho user provisioning
      
```
Authentication
Sử dụng Clerk session token:
```bash
Authorization: Bearer clerk_session_token
```
