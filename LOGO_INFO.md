# KTR 로고 정보

## 🎨 생성된 로고 파일

### 1. SVG 버전 (벡터)
- **파일**: `static/ktr_logo.svg`
- **용도**: 웹에서 사용 (확대해도 선명)
- **특징**: 
  - 그라디언트 색상 (보라 → 핑크)
  - 깔끔한 벡터 그래픽
  - 애니메이션 효과 (천천히 회전)

### 2. PNG 버전 (래스터)
- **파일**: `static/ktr_logo.png`
- **크기**: 800x800px
- **용도**: 일반 이미지, 다운로드용
- **특징**:
  - 고해상도
  - 투명 배경
  - 그라디언트 효과

### 3. Favicon
- **파일**: `static/favicon.png`
- **크기**: 256x256px
- **용도**: 브라우저 탭 아이콘
- **특징**: 작은 크기에 최적화

## 🎯 로고 디자인 요소

### 색상 팔레트
```
주 색상 (Primary):
- 보라색: #667eea
- 진보라: #764ba2

강조 색상 (Accent):
- 핑크: #f093fb
- 레드핑크: #f5576c
```

### 구성 요소
1. **배경 원**: 그라디언트 보라색
2. **내부 원**: 흰색 (95% 불투명도)
3. **KTR 텍스트**: 그라디언트 효과
4. **장식 라인**: 하단 곡선
5. **장식 점**: 상하좌우 4개

### 애니메이션
- **회전**: 20초에 한 바퀴 (매우 천천히)
- **호버**: 마우스 올리면 회전 멈춤

## 🔧 로고 커스터마이징

### 실제 회사 로고로 교체하는 방법

#### 방법 1: 파일 교체
1. 실제 KTR 로고 파일을 준비 (PNG, SVG, JPG 등)
2. 파일명을 `ktr_logo.png` 또는 `ktr_logo.svg`로 변경
3. `static/` 폴더에 덮어쓰기

#### 방법 2: HTML 수정
`templates/index.html`에서:
```html
<!-- 현재 -->
<img src="/static/ktr_logo.svg" alt="KTR Logo" class="logo">

<!-- 교체 예시 -->
<img src="/static/your_logo.png" alt="KTR Logo" class="logo">
```

### 로고 크기 조정
`templates/index.html`의 CSS 부분:
```css
.logo-container {
    width: 80px;   /* 원하는 크기로 변경 */
    height: 80px;
}

.logo {
    width: 80px;
    height: 80px;
}
```

### 애니메이션 제거
애니메이션을 원하지 않으면:
```css
.logo {
    /* animation: logoSpin 20s linear infinite; */  /* 주석 처리 */
}
```

## 📁 파일 위치

```
ktrGPT/
├── static/
│   ├── ktr_logo.svg      ← SVG 로고
│   ├── ktr_logo.png      ← PNG 로고 (800x800)
│   └── favicon.png       ← Favicon (256x256)
├── templates/
│   └── index.html        ← 로고 사용하는 HTML
└── create_logo.py        ← 로고 생성 스크립트
```

## 🎨 로고 재생성

색상이나 디자인을 변경하고 싶으면:

1. `create_logo.py` 파일 수정
2. 실행:
   ```bash
   py -3.11 create_logo.py
   ```
3. 서버 재시작

## 💡 디자인 팁

### 로고에 그림자 추가
```css
.logo {
    filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.3));
}
```

### 로고 호버 효과
```css
.logo:hover {
    transform: scale(1.1);
    transition: transform 0.3s;
}
```

### 로고 회전 속도 조정
```css
/* 빠르게 */
animation: logoSpin 5s linear infinite;

/* 천천히 */
animation: logoSpin 60s linear infinite;
```

## 🖼️ 로고 사용 예시

### 웹사이트 헤더
✅ 현재 사용 중

### 이메일 서명
PNG 버전 사용 권장

### 문서/보고서
PNG 버전 (고해상도)

### SNS 프로필
Favicon 버전 사용 가능

---

**Made with ❤️ for KTR**
