# Chat KTR 실행 방법

## 🚀 한 줄 실행

```bash
py -3.11 web_chatbot.py
```

또는

```bash
python web_chatbot.py
```

---

## 📋 실행 순서

### 1. 터미널 열기
- VSCode: `Ctrl + `` (백틱)
- 또는 Windows PowerShell 실행

### 2. 프로젝트 폴더로 이동
```bash
cd C:\Users\user\Desktop\Work\ktrGPT
```

### 3. 서버 실행
```bash
py -3.11 web_chatbot.py
```

### 4. 브라우저에서 접속
```
http://localhost:5000
```

---

## ✅ 실행 성공 확인

터미널에 다음과 같이 표시되면 성공!

```
============================================================
Chat KTR 서버 시작
============================================================
URL: http://localhost:5000
지식 베이스: 27개 질문-답변
의미 기반 검색 활성화
============================================================
```

---

## 🌐 접속 방법

### 같은 컴퓨터
```
http://localhost:5000
```

### 다른 컴퓨터 (같은 네트워크)
1. 서버 컴퓨터의 IP 확인:
```bash
ipconfig
```
IPv4 주소 확인 (예: 192.168.0.100)

2. 다른 컴퓨터에서 접속:
```
http://192.168.0.100:5000
```

---

## ⚙️ 실행되는 과정

```
1. web_chatbot.py 실행
   ↓
2. data/data.xlsx 로딩 (27개 질문-답변)
   ↓
3. OpenAI API로 임베딩 생성 (약 8초)
   ↓
4. Flask 서버 시작 (포트 5000)
   ↓
5. 접속 가능! 🎉
```

---

## 🛑 서버 종료

터미널에서:
```
Ctrl + C
```

---

## ❗ 문제 해결

### Python 버전 오류
```bash
# Python 3.11이 없으면
py web_chatbot.py

# 또는
python3 web_chatbot.py
```

### 포트 5000 이미 사용 중
```bash
# 다른 포트 사용 (web_chatbot.py 수정)
app.run(host='0.0.0.0', port=5001, debug=True)
```

### 패키지 없음 오류
```bash
pip install -r requirements.txt
```

---

## 📦 필요한 파일 확인

실행에 필요한 파일들:
```
ktrGPT/
├── web_chatbot.py          ← 이 파일 실행!
├── rag_chatbot_v2.py       (자동 import)
├── question_logger.py      (자동 import)
├── config.py               (자동 import)
├── data/
│   └── data.xlsx           (27개 질문-답변)
├── templates/
│   ├── index.html          (메인 페이지)
│   └── logs.html           (로그 페이지)
└── static/
    ├── ktr_logo.png
    └── favicon.png
```

모든 파일이 있으면 실행 가능! ✅







