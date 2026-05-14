# 📊 한국 증시 대시보드

매일 오전 7시 자동 업데이트되는 가족용 증시 브리핑 페이지입니다.

## 🚀 설치 방법 (5분 완성)

### 1단계 — GitHub 저장소 생성
1. https://github.com 로그인
2. 우상단 `+` → **New repository**
3. Repository name: `korea-stock-dashboard`
4. **Public** 선택 (GitHub Pages 무료 사용 필수)
5. **Create repository** 클릭

### 2단계 — 파일 업로드
1. 저장소 메인에서 **uploading an existing file** 클릭
2. 이 폴더의 모든 파일을 드래그 업로드
   - `index.html`
   - `fetch_data.py`
   - `.github/workflows/update.yml`
   - `data/market.json`
3. **Commit changes** 클릭

### 3단계 — GitHub Pages 활성화
1. 저장소 → **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: **main** / **/ (root)** 선택
4. **Save** 클릭
5. 약 1~2분 후 `https://[아이디].github.io/korea-stock-dashboard` 접속 확인

### 4단계 — Actions 권한 설정
1. 저장소 → **Settings** → **Actions** → **General**
2. **Workflow permissions** → **Read and write permissions** 선택
3. **Save**

### 5단계 — 첫 수동 실행 테스트
1. 저장소 → **Actions** 탭
2. **Update Stock Dashboard** 클릭
3. **Run workflow** → **Run workflow**
4. 초록 체크가 뜨면 성공! `data/market.json`이 업데이트됩니다.

---

## ⏰ 자동 실행 스케줄
- 매일 **오전 7시 (KST)** 자동 실행
- GitHub Actions 무료 플랜: 월 2,000분 제공 (스크립트 실행 약 30초이므로 충분)

## 🔗 카카오톡 공유
`https://[GitHub아이디].github.io/korea-stock-dashboard`
위 링크를 가족 단체방에 고정 메시지로 등록하세요!

## 📁 파일 구조
```
korea-stock-dashboard/
├── index.html                      # 대시보드 페이지
├── fetch_data.py                   # 데이터 수집 (Yahoo Finance + 네이버 뉴스)
├── data/
│   └── market.json                 # 자동 업데이트되는 데이터
└── .github/
    └── workflows/
        └── update.yml              # 매일 07시 자동 실행 설정
```
