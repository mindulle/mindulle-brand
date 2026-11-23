# SNS 채널 인벤토리 및 프로필 자산 정본 (BRAND-12)

> **SSOT:** `mindulle-brand` 저장소가 채널 핸들·소개문·프로필 그래픽의 단일 정본입니다.
> **연결:** `PORT-19` (포트폴리오 소셜 링크 섹션) · `BRAND-13` (프로필 자산)

---

## 1. 채널 인벤토리

| 플랫폼 | 상태 | 정본 핸들 / URL | 용도 |
| --- | --- | --- | --- |
| **GitHub** | 보유 · 활성 | `https://github.com/mindulle` | 오픈소스·코드 기록 |
| **Blog (사유의 정원)** | 보유 · 활성 | `https://blog.sonagi.space` | 기술 노트·작업 연감 |
| **Portfolio (쇼룸)** | 보유 · 활성 | `https://portfolio.sonagi.space` | 3D 시네마틱 쇼룸 |
| **Design System** | 보유 · 활성 | `https://design.sonagi.space` | MDS 토큰·컴포넌트 규격 |
| **Email** | 보유 · 활성 | `craftsman@sonagi.space` | 공식 외주·협업 문의 |
| **LinkedIn** | 등록 예정 | 추천: `hyeseong-park` / `mindulle-atelier` | Upwork·클라이언트 신뢰 검증 |
| **Behance** | 등록 예정 | 추천: `mindulle` | 디자인 시스템·쇼룸 케이스 아카이브 |
| **Dribbble** | 등록 예정 | 추천: `mindulle` | UI·1px 모노라인 스냅샷 |
| **X (Twitter)** | 등록 예정 | 추천: `@mindulle_studio` (예비 `@sonagi_space`) | 3D·드로잉 작업 과정 공유 |

> **네이밍 원칙:** 영문 핸들은 **`mindulle`**(우선) → **`mindulle_studio`** → **`sonagi_space`** 순으로 선점합니다.
> **콘테스트 플랫폼**(라우드소싱·99designs)은 성격이 달라 §4에서 따로 관리합니다. 1차 수주 채널입니다.

---

## 2. 채널 소개문 정본 (150자 이내 · `korean-humanize` 기준)

### 2.1 라우드소싱 프로필 (2026-11-23 확정)

디자인 콘테스트 플랫폼은 **개발 이력이 아니라 인쇄·패키지 역량**으로 읽힌다. 그래서 별도 문안을 쓴다.

| 항목 | 값 |
| --- | --- |
| 닉네임 | `민들레 스튜디오` (핸들·URL은 `magicwand` 유지) |
| 한 줄 소개 | `브랜드와 패키지를 만드는 디자이너` (16/20) |
| 관심 분야 | `로고/브랜딩` · `패키지` |

**자기소개 (확정)**

```
브랜드와 패키지를 만듭니다. 로고·아이덴티티부터 라벨·파우치·단상자까지,
쓰는 사람이 헷갈리지 않게 규칙을 먼저 정하고 그립니다.

인쇄는 직접 하지 않습니다. 대신 인쇄소가 바로 받을 수 있는 파일 규격 —
도련 3mm·CMYK·재단선·바코드 조용영역 — 까지 맞춰서 넘깁니다.
마감 전날 규격 때문에 다시 그리는 일이 없도록, 전개도·여백·색을 처음에 확정합니다.
```

- **인쇄를 직접 한다고 쓰지 않는다.** 실제로 해본 적이 없으므로 "인쇄용 규격까지 맞춘다"로 사실만 적는다
- 범위(브랜드·패키지)는 한 줄 소개가 담고, 인쇄 규격 대응은 자기소개가 담당한다
- 웹·3D 역량은 문안이 아니라 **작업 사례**로 보여준다
- 첫 수주 전에 샘플 인쇄 1건을 실제로 돌려보면 이 문장의 근거가 생긴다


- **국문 정본 (112자):**
  > 코드와 화면을 한 손으로 깎는 1인 공방 Mindulle Atelier입니다. Three.js/WebGL, W3C 디자인 토큰, Next.js 기반으로 오래 남는 도구를 만듭니다.
- **영문 변형 1 (LinkedIn / Upwork용):**
  > Solo Software & Design Studio (Mindulle Atelier). Building interactive Three.js/WebGL experiences, W3C design token systems, and calm Next.js products.
- **영문 변형 2 (Behance / Dribbble용):**
  > Mindulle Atelier — Independent software & design practice. 3D WebGL, Figma-synced design tokens, and 1px editorial interfaces.
- **영문 변형 3 (X / Threads용):**
  > Mindulle Atelier · Solo studio crafting WebGL worlds, W3C design systems & Next.js tools.

---

## 3. 프로필·배너·스킬 아이콘 자산 규격 (`BRAND-12` / `BRAND-13`)

| 파일 경로 | 규격 (`viewBox`) | 용도 |
| --- | --- | --- |
| `assets/svg/social/avatar-dark-1024.svg` | `1024×1024` | GitHub·X·Behance·Dribbble 다크 아바타 |
| `assets/svg/social/avatar-light-1024.svg` | `1024×1024` | 신문지 톤(`#FBF9F5`) 라이트 아바타 |
| `assets/svg/social/banner-linkedin-1584x396.svg` | `1584×396` | LinkedIn·Upwork 가로형 커버 |
| `assets/svg/social/banner-x-1500x500.svg` | `1500×500` | X(Twitter) 헤더 배너 |
| `assets/svg/social/banner-behance-3200x410.svg` | `3200×410` | Behance 프로필 배너 |
| `assets/svg/social/banner-dribbble-1600x1200.svg` | `1600×1200` | Dribbble 4:3 커버/샷 |
| `assets/svg/social/banner-99designs-2480x400.svg` | `2480×400` | 99designs 프로필 커버 |
| `assets/svg/skills/skill-*.svg` (6종) | `120×120` | Three.js/WebGL · Design Systems · Next.js/React · Figma Tokens · GLSL Shaders · SVG Editorial |


---

## 4. 콘테스트 플랫폼 (1차 수주 채널)

패키지 우선 전략(WORK-29)으로 국내는 라우드소싱, 해외는 99designs를 쓴다.
**계정 운영(가입·심사·지원서)은 WORK 트랙, 핸들·링크·프로필 그래픽은 이 문서(BRAND)가 정본**이다.

| 플랫폼 | 상태 | 핸들 / URL | 용도 | 관리 경계 |
| --- | --- | --- | --- | --- |
| **라우드소싱** | 보유 · 활성 (2026-11-20 LOUD 제출) | `https://www.loud.kr/m/mindullestudio` (핸들 `mindullestudio` · 닉네임 `민들레 스튜디오`) | 국내 패키지·로고 공모전 수주 | 계정·제출 이력: WORK-25 / 링크·자산: BRAND-12 |
| **99designs** | 미보유 (확인 필요) | — | 해외 웹·북커버·인쇄물 | 프로필 문안: WORK-15·16 / 링크·자산: BRAND-12 |

### 4.1 자산 규격 (실측)

| 플랫폼 | 자산 | 규격 | 비고 |
| --- | --- | --- | --- |
| 라우드소싱 | 프로필 이미지 | **132 × 132 px** | 2026-11-23 확인: 이미 등록돼 있음(교체는 선택) |
| 라우드소싱 | 프로필 배경 | **1920 × 240 px** (권장) | `loudsourcing-1920x240.png` |
| 라우드소싱 | 참여작 썸네일 | **600 × 600 px** | 작품 요약 |
| 라우드소싱 | 참여작 상세 이미지 | **가로 1024 px · 세로 자유** | RGB 저장(CMYK 원본과 별도) |
| 라우드소싱 | 업로드 제한 | **5MB · 최대 10장** | WebP 지원 |
| 99designs | 아바타 | **500 × 500 px** | 원형 크롭 표시 |
| 99designs | 프로필 커버 | **2480 × 400 px** (최소 1240×200) | 데스크톱 1240×200 · 모바일 540×200 |
| 99designs | 참여작·포트폴리오 | **960×960 ~ 2040×8160 px**, RGB, PNG/JPG/GIF, **8MB** | 정사각 최소 |

- 라우드소싱은 **썸네일(600²)과 상세(1024 가로)를 따로** 올린다. 상세는 세로 자유라 길게 만들 수 있다
- 라우드소싱 제출물은 **RGB**로 저장한다. 인쇄용 CMYK 원본과 별개 파일
- 작품 등록 시 **사용 AI 도구·스톡 라이선스**를 함께 제출한다(요청 시 프롬프트)

### 4.2 기존 자산 재사용

콘테스트 프로필에는 아래 자산을 우선 재사용하고, 규격이 다르면 크롭한다.

- 아바타: `assets/svg/social/avatar-dark-1024.svg` → 132²(라우드소싱) · 500²(99designs)로 축소
- 가로 커버: `assets/svg/social/banner-linkedin-1584x396.svg` → 99designs 2480×400은 별도 제작 필요
- 참여작 썸네일 600²: `press mockup` PNG를 1:1 크롭
- 참여작 상세 1024 가로: `press mockup` PNG를 1024 폭으로 리사이즈(세로 자유)

### 4.2.1 PNG 내보내기

```bash
python3 scripts/export_social.py --all                       # 아바타·배너 세트
python3 scripts/export_social.py --entry path/to/mockup.png  # 참여작 600²·1024·1200
```

산출물은 `assets/png/social/`에 쌓인다. 규격은 아래와 같다.

| 파일 | 크기 | 용도 |
| --- | --- | --- |
| `avatar-dark-1024-loudsourcing-132.png` | 132² | 라우드소싱 프로필 |
| `avatar-dark-1024-99designs-500.png` | 500² | 99designs 아바타(원형 안전) |
| `99designs-2480x400.png` | 2480×400 | 99designs 커버 |
| `loudsourcing-1920x240.png` | 1920×240 | 라우드소싱 배경 |
| `linkedin-1584x396.png` · `x-1500x500.png` · `behance-3200x410.png` · `dribbble-1600x1200.png` | 각 규격 | SNS 배너 |
| `<mockup>-thumbnail-600.png` | 600² | 라우드소싱 썸네일 |
| `<mockup>-detail-1024.png` | 1024 가로 | 라우드소싱 상세 |
| `<mockup>-99designs-1200.png` | 1200 가로 | 99designs 참여작 |

- 참여작 썸네일은 **잘라내지 않고 여백을 둔다**(contain). 잘라내면 브랜드명이 사라진다
- SVG 렌더는 chromium을 쓰며, snap 제약 때문에 저장소 안 `.tmp-social/`에 임시 파일을 만든다

### 4.3 하지 않는 것

- 플랫폼 계정 생성·심사 대응·지원서 제출은 이 문서 범위가 아니다 (WORK)
- 99designs 로고·일러스트 카테고리는 AI 금지라 참여하지 않는다 (WORK-29 D16)
