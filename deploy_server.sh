#!/bin/bash

# KTR GPT 챗봇 서버 배포 스크립트
# 사용법: bash deploy_server.sh

echo "=========================================="
echo "KTR GPT 챗봇 서버 배포 시작"
echo "=========================================="

# 1. 시스템 업데이트
echo "1단계: 시스템 업데이트 중..."
sudo apt update

# 2. 필수 패키지 설치
echo "2단계: 필수 패키지 설치 중..."
sudo apt install -y python3 python3-pip python3-venv python3-dev git build-essential libssl-dev libffi-dev

# 3. 프로젝트 디렉토리로 이동
echo "3단계: 프로젝트 디렉토리 설정 중..."
cd ~
if [ -d "ktrGPT" ]; then
    echo "기존 프로젝트 폴더 발견. 업데이트 중..."
    cd ktrGPT
    git pull origin main
else
    echo "새 프로젝트 클론 중..."
    git clone https://github.com/SUNMOKKIM/ktrGPT.git
    cd ktrGPT
fi

# 4. 가상환경 생성 및 활성화
echo "4단계: Python 가상환경 설정 중..."
python3 -m venv venv
source venv/bin/activate

# 5. 의존성 설치
echo "5단계: Python 패키지 설치 중..."
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn

# 6. 로그 디렉토리 생성
echo "6단계: 로그 디렉토리 생성 중..."
mkdir -p logs

# 7. Gunicorn 설정 파일 생성
echo "7단계: Gunicorn 설정 파일 생성 중..."
cat > gunicorn.conf.py << 'EOF'
bind = "0.0.0.0:8000"
workers = 2
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 100
preload_app = True
daemon = False
pidfile = "/home/ktr/ktrGPT/gunicorn.pid"
accesslog = "/home/ktr/ktrGPT/logs/access.log"
errorlog = "/home/ktr/ktrGPT/logs/error.log"
loglevel = "info"
EOF

# 8. systemd 서비스 파일 생성
echo "8단계: systemd 서비스 설정 중..."
sudo tee /etc/systemd/system/ktrgpt.service > /dev/null << 'EOF'
[Unit]
Description=KTR GPT Chatbot
After=network.target

[Service]
Type=exec
User=ktr
Group=ktr
WorkingDirectory=/home/ktr/ktrGPT
Environment=PATH=/home/ktr/ktrGPT/venv/bin
ExecStart=/home/ktr/ktrGPT/venv/bin/gunicorn --config gunicorn.conf.py web_chatbot:app
Restart=always
RestartSec=3
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

# 9. 서비스 활성화
echo "9단계: 서비스 활성화 중..."
sudo systemctl daemon-reload
sudo systemctl enable ktrgpt
sudo systemctl start ktrgpt

# 10. 방화벽 설정
echo "10단계: 방화벽 설정 중..."
sudo ufw allow 8000:9000/tcp

# 11. 서비스 상태 확인
echo "11단계: 서비스 상태 확인 중..."
sleep 3
sudo systemctl status ktrgpt --no-pager

echo "=========================================="
echo "배포 완료!"
echo "=========================================="
echo "서버 접속 URL: http://192.168.1.210:8000"
echo "서비스 상태 확인: sudo systemctl status ktrgpt"
echo "서비스 재시작: sudo systemctl restart ktrgpt"
echo "로그 확인: sudo journalctl -u ktrgpt -f"
echo "=========================================="
