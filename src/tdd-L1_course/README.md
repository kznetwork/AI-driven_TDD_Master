# L2 · AI 시대의 TDD (2일) — 실습 폴더

| 폴더 | 교안 시간 | 하는 일 |
|------|-----------|---------|
| starter/cart-a | Day 1 09:00 | 실험 A — 테스트 없이 AI에게 맡기기 (A-1 ~ A-9) |
| starter/calc   | Day 1 오전 | RED → GREEN → REFACTOR 첫 사이클 (tests/ 비어 있음) |
| starter/cart   | Day 1 오후 ~ Day 2 | 장바구니 할인 — 예시 표 → 테스트 → 구현 |
| starter/ship   | Day 2 수료 실습 | 배송비 — 혼자서 TDD 사이클 |

solution/ 은 정답입니다. 수강생에게는 starter/ 만 배포하세요.

```bash
cd starter/calc
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
pytest -q                          # 처음에는 "no tests ran" 이 정상
gemini                             # 이 폴더에서 Gemini CLI 실행
```

## 프롬프트 파일
- `starter/<프로젝트>/prompts.md` — 실습 순서대로 쓴 프롬프트 (VS Code 에서 열어 두고 복사)
- `프롬프트_템플릿.md` — 꺾쇠 `< >` 만 바꿔 실무에서 재사용하는 일반형
- `solution/프롬프트_모음.md` — 슬라이드 번호 · 기대 결과 · 진행 메모 포함
