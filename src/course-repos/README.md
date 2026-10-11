# L2 · AI 시대의 TDD (2일) — 실습 폴더

교안: `(교안) 실전-Coding Agent 실전 AI기반 TDD 마스터 과정_20261010_작업폴더안내.pptx` (슬라이드 번호는 이 교안 기준)

| 폴더 | 교안 시간 | 하는 일 | 슬라이드 |
|------|-----------|---------|---------|
| starter/cart-a | Day 1 09:00 | 실험 A — 테스트 없이 AI에게 맡기기 (A-1 ~ A-9) | 12–22 |
| starter/calc   | Day 1 오전 · 오후 | RED → GREEN → REFACTOR 첫 사이클, R1 ~ R7, 골든 마스터 (tests/ 비어 있음) | 85–108 |
| starter/cart   | Day 2 08:30 ~ 12:00 | 사양 찾기(예시 표) → 장바구니 TDD 1·2 → GEMINI.md → 골든 마스터 | 114–142 |
| starter/ship   | Day 2 15:00 ~ 16:50 | 확인 실습 — 계약표 · 테스트 플랜 · TDD · 골든 마스터 · 전략 패턴 | 204–217 |
| solution/교안예제 | 교안 전체 | 교안에 나온 코드의 실행 가능한 원본 (README 참고) | — |

Day 2 시간표: 08:30 사양 찾기 · 09:30 장바구니 TDD 1 · 10:30 GEMINI.md · 11:10 장바구니 TDD 2 · 13:00 3장 클린 코드와 리팩토링 · 14:00 리팩터링 · 실험 B · 15:00 확인 실습 · 17:00 마무리.

solution/ 은 강사용 정답입니다. 수강생에게는 starter/ 와 checkpoints/ 만 배포하세요 (`course-repos-수강생용/` 참고).

```bash
cd starter/calc
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
pytest -q                          # 처음에는 "no tests ran" 이 정상
gemini                             # 이 폴더에서 Gemini CLI 실행
```

## 프롬프트 파일
- `starter/<프로젝트>/prompts.md` — 실습 순서대로 쓴 프롬프트와 슬라이드 번호 (VS Code 에서 열어 두고 복사)
- `프롬프트_템플릿.md` — 꺾쇠 `< >` 만 바꿔 실무에서 재사용하는 일반형
- `프롬프트_GildedRose_범용.md` — 부록 A · B · C 의 코딩 에이전트 공통 프롬프트
- `solution/프롬프트_모음_강사용.md` — 슬라이드 번호 · 기대 결과 · 진행 메모 포함 (강사용)

## 골든 마스터 / 속성 테스트
- 골든 파일 갱신: `UPDATE_GOLDEN=1 pytest -q tests/test_golden_master.py` (PowerShell: `$env:UPDATE_GOLDEN=1`). 갱신은 diff 를 읽고 승인한 뒤에만.
- 속성 테스트(부록 C): `pip install hypothesis` — `solution/교안예제/property_based/`
