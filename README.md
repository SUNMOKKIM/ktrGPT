# KTR GPT 챗봇

KTR(한국기술연구원) 신입직원 교육을 위한 AI 챗봇 시스템입니다.

## 주요 기능

- 🤖 **의미 기반 검색**: 한국어 특화 임베딩 모델을 사용한 정확한 질문-답변 매칭
- 📊 **Excel 데이터 기반**: 기존 교육 자료를 활용한 지식 베이스
- 🌐 **웹 인터페이스**: 사용자 친화적인 웹 UI 제공
- 📝 **미답변 질문 로깅**: 답변하지 못한 질문 자동 수집 및 관리
- 🔍 **실시간 통계**: 질문 처리 현황 실시간 모니터링

## 기술 스택

- **Backend**: Python, Flask
- **AI/ML**: 
  - Sentence Transformers (ko-sroberta-multitask)
  - Scikit-learn (코사인 유사도)
  - Pandas (데이터 처리)
- **Frontend**: HTML, CSS, JavaScript
- **Data**: Excel (.xlsx)

## 설치 및 실행

### 1. 저장소 클론
```bash
git clone https://github.com/nadasunmok/ktrGPT.git
cd ktrGPT
```

### 2. 가상환경 생성 및 활성화
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. 데이터 파일 준비
- `data/data.xlsx` 파일이 있는지 확인
- Excel 파일에는 '질문'과 '답변' 컬럼이 있어야 함

### 5. 서버 실행
```bash
python web_chatbot.py
```

### 6. 접속
- 메인 페이지: http://localhost:5000
- 로그 페이지: http://localhost:5000/logs

## API 엔드포인트

### 채팅 API
```
POST /api/chat
Content-Type: application/json

{
    "question": "사용자 질문"
}
```

### 서버 상태 확인
```
GET /api/health
```

### 미답변 질문 조회
```
GET /api/unanswered
```

## 프로젝트 구조

```
ktrGPT/
├── web_chatbot.py          # Flask 웹 서버
├── rag_chatbot_v2.py       # RAG 챗봇 핵심 로직
├── question_logger.py      # 질문 로깅 시스템
├── config.py              # 설정 파일 (API 키 등)
├── requirements.txt        # Python 의존성
├── data/
│   └── data.xlsx          # 질문-답변 데이터
├── templates/
│   ├── index.html         # 메인 페이지
│   └── logs.html          # 로그 페이지
├── static/                # 정적 파일
├── logs/                  # 로그 파일
└── README.md              # 프로젝트 설명
```

## 주요 특징

### 1. 의미 기반 검색
- 한국어 특화 임베딩 모델 사용
- 코사인 유사도 기반 질문 매칭
- 정확도 높은 답변 제공

### 2. 자동 로깅 시스템
- 답변하지 못한 질문 자동 수집
- Excel 파일로 로그 관리
- 실시간 통계 제공

### 3. 웹 인터페이스
- 직관적인 채팅 UI
- 실시간 로그 모니터링
- 반응형 디자인

## 설정

### config.py 수정
```python
# 데이터 파일 경로
DATA_CONFIG = {
    'excel_file_path': './data',
    'question_column': '질문',
    'answer_column': '답변',
}

# 임베딩 모델 설정
EMBEDDING_CONFIG = {
    'model_name': 'jhgan/ko-sroberta-multitask',
    'device': 'cpu',  # 또는 'cuda'
}
```

## 배포

### 클라우드 서버 배포
1. Ubuntu 서버 준비
2. Python 3.11+ 설치
3. 의존성 설치
4. Gunicorn으로 프로덕션 서버 실행
5. Nginx 리버스 프록시 설정
6. SSL 인증서 적용

자세한 배포 가이드는 프로젝트 문서를 참조하세요.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 기여

버그 리포트나 기능 제안은 Issues를 통해 알려주세요.

## 연락처

- 이메일: nadasunmok@naver.com
- GitHub: https://github.com/nadasunmok