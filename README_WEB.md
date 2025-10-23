# KTR 지식 챗봇 웹 버전

## 🎉 완성!

전문적인 디자인의 웹 챗봇이 완성되었습니다!

## 🚀 실행 방법

### 1. 서버 시작

```bash
py -3.11 web_chatbot.py
```

### 2. 브라우저에서 접속

```
http://localhost:5000
```

## ✨ 주요 기능

### 1. 전문적인 디자인
- ✅ KTR 로고 포함
- ✅ 그라디언트 배경 (보라색 → 핑크)
- ✅ 현대적인 UI/UX
- ✅ 반응형 디자인 (모바일 대응)

### 2. 실시간 채팅
- ✅ 즉각적인 응답
- ✅ 타이핑 인디케이터
- ✅ 메시지 타임스탬프
- ✅ 부드러운 애니메이션

### 3. 의미 기반 검색
- ✅ 정확한 키워드가 아니어도 찾기
- ✅ "전화할때 주의할점" → "전화예절" 매칭
- ✅ 엑셀 데이터 그대로 답변

### 4. 추천 질문
- ✅ 클릭 한 번으로 질문 가능
- ✅ 자주 묻는 질문 표시

## 📁 파일 구조

```
ktrGPT/
├── web_chatbot.py           ← Flask 서버
├── rag_chatbot_v2.py        ← 의미 기반 검색 챗봇
├── templates/
│   └── index.html           ← 웹 페이지 (HTML + CSS + JS)
├── static/                  ← 정적 파일 (이미지 등)
└── data/
    └── data.xlsx            ← 질문-답변 데이터
```

## 🎨 디자인 특징

### 색상 팔레트
- **Primary**: 보라색 (#667eea → #764ba2 그라디언트)
- **배경**: 그라디언트 (보라 → 핑크)
- **카드**: 깔끔한 흰색 (#ffffff)
- **텍스트**: 다크 그레이 (#202124)

### UI 요소
- **KTR 로고**: 원형 배지에 그라디언트 텍스트
- **상태 표시**: 온라인 상태 + 애니메이션
- **메시지 버블**: 사용자/봇 구분, 둥근 모서리
- **입력창**: 포커스 시 하이라이트
- **버튼**: 호버 시 상승 효과

## 🌐 배포 방법

### 로컬 네트워크에서 접속

1. 서버 실행 (위와 동일)
2. 내 IP 주소 확인:
   ```bash
   ipconfig
   ```
3. 같은 네트워크의 다른 기기에서 접속:
   ```
   http://[내_IP주소]:5000
   ```

### 인터넷에 배포 (옵션)

#### 방법 1: Heroku
```bash
# requirements.txt 확인
pip freeze > requirements.txt

# Heroku 배포
git init
heroku create ktr-chatbot
git add .
git commit -m "Deploy KTR chatbot"
git push heroku main
```

#### 방법 2: Vercel, Railway, Render 등
- 무료 호스팅 서비스 활용
- GitHub 연동으로 자동 배포

## 🔧 커스터마이징

### 로고 이미지로 변경
1. `static/` 폴더에 `logo.png` 추가
2. `index.html`에서 수정:
   ```html
   <div class="logo-container">
       <img src="/static/logo.png" alt="KTR Logo">
   </div>
   ```

### 색상 변경
`index.html`의 CSS `:root` 부분 수정:
```css
:root {
    --primary-color: #1a73e8;  /* 원하는 색상으로 변경 */
}
```

### 추천 질문 변경
`index.html`의 `.suggested-questions` 부분 수정

## 📊 API 엔드포인트

### POST /api/chat
채팅 메시지 전송

**요청:**
```json
{
    "question": "그룹웨어 주소가 뭐야?"
}
```

**응답:**
```json
{
    "success": true,
    "answer": "그룹웨어 주소는 A입니다."
}
```

### GET /api/health
서버 상태 확인

**응답:**
```json
{
    "status": "ok",
    "knowledge_base_size": 8
}
```

## 🛠️ 문제 해결

### 포트 5000이 이미 사용 중
`web_chatbot.py` 마지막 줄 수정:
```python
app.run(host='0.0.0.0', port=5001, debug=True)  # 포트 변경
```

### 챗봇 응답이 느림
- OpenAI API 호출이므로 약간의 지연 정상
- 임베딩은 초기화 시 한 번만 생성

### 데이터 업데이트
1. `data/data.xlsx` 수정
2. 서버 재시작 (Ctrl+C 후 재실행)

## 🎯 다음 단계

### 추천 개선사항
1. **로그인 기능** 추가
2. **대화 히스토리** 저장
3. **파일 업로드** 기능 (PDF, 문서 등)
4. **관리자 페이지** (데이터 추가/수정)
5. **다국어 지원** (영어, 중국어 등)
6. **음성 입력/출력**
7. **이미지 첨부** 기능

## 📞 문의

문제가 있거나 개선 사항이 있으면 말씀해주세요!

---

**Made with ❤️ for KTR**
