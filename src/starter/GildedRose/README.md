# Gilded Rose

Gilded Rose 는 게임 "World of Warcraft"에 나오는 여관 이름입니다.  
아이템은 퀄리티 속성을 가지고 있으며, 예외 사항이 있는 아이템들이 있습니다.  
- 아이템은 [아이템 이름, 퀄리티, 유통기한]의 속성을 가집니다.  
- 아이템의 퀄리티는 0 이상이고 아이템의 퀄리티는 하루가 지날 때마다 1씩 줄어듭니다.  
- 유통 기한이 지난 아이템의 퀄리티는 2배의 속도로 떨어집니다.  
- 퀄리티는 최대값이 50입니다.  

### Aged Brie, Backstage Pass, Sulfuras 의 예외적 규칙  

- Aged Brie는 하루가 지날 때마다 퀄리티가 1씩 증가합니다.  
- 유통기한이 지나면 퀄리티가 2씩 증가합니다.  
- Backstage Pass 는 유통기한(콘서트일)이 다가올수록 퀄리티가 증가합니다.  
  유통기한이 11일 이상일 때는 1, 10일 이하일 때는 2, 5일 이하일 때는 3씩 증가하지만  
  콘서트 날이 지나면 퀄리티는 0이 됩니다.  
- Sulfuras의 퀄리티는 변화가 없습니다.  
  
---------------------------------------------------------  
## 실습 목적 :  테스트 코드 작성을 통한 legacy code 이해

### 프로젝트 구조 (Python)

```
python/
├── item.py                 # Item 클래스 (수정 불가)
├── gilded_rose.py          # GildedRose 클래스 (update_quality() 구현)
└── test_gilded_rose.py     # unittest 기반 테스트
```

### 가상환경 설정 및 테스트 실행

```bash
cd python

# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source venv/bin/activate

# 테스트 실행
python -m unittest test_gilded_rose -v

# 가상환경 비활성화
deactivate
```

### test_gilded_rose.py : failed test 수정
- update_quality() 의 test case를 추가 작성해 보세요.
- unit test 내용 : 문서상에 나타난 동작들 확인

### unit test VS golden-master test 비교


---------------------------------------------------------
## 이 폴더 사용법 (TDD 마스터 과정 · 부록 A · B)

카타 원본의 `python/` 폴더 내용을 이 폴더 **루트**로 옮겨 두었다. 교안의 프롬프트는 모두 이 폴더를 기준으로 한다.

```
GildedRose/
├── GildedRoseRequirements.txt   # 요구사항 (읽기만)
├── README.md                    # 이 파일 (한국어 요약)
├── item.py                      # Item 클래스 — 수정 금지 (다른 팀 소유)
├── gilded_rose.py               # GildedRose.update_quality() — 레거시 원본 (중첩 조건문)
├── pytest.ini                   # pythonpath = . (루트의 모듈을 import)
├── requirements.txt             # pytest · approvaltests
├── tests/
│   └── test_gilded_rose.py      # 카타가 주는 자리표시 테스트 test_foo (일부러 실패한다)
└── docs/                        # 실습 중 AI 가 만드는 문서 (규칙표 · 분기지도 · 테스트케이스 · 특성화)
```

```bash
cd C:\DEV\tdd-course\GildedRose
python -m venv .venv
.venv\Scripts\activate                 # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q                      # 처음에는 1 failed (test_foo) 가 정상
```

- 프롬프트: `prompts.md` (슬라이드 순서대로, 프롬프트 · 저장할 파일 · 실행 명령 · 기대 결과)
- 막히면 `checkpoints\A.3_테스트케이스완료\GildedRose` 등 같은 이름의 폴더를 복사해 이어서 한다.
