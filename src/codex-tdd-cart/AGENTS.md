# Repository instructions
장바구니 할인 계산기 — Python 3.12, pytest 기반 Dual-Track TDD 프로젝트.
이 파일은 백과사전이 아니라 '지침'이다.

## 프로젝트 구조
- src/cart.py  : Logic 트랙(순수 함수: 금액·할인 계산)
- src/app.py   : UI 트랙(Flask 주문 폼)
- tests/test_cart.py / tests/test_ui.py : 트랙별 테스트

## 테스트 명령
- 전체: pytest -q   - Logic: pytest tests/test_cart.py -q   - UI: pytest tests/test_ui.py -q

## 개발 워크플로 — TDD 필수
- 반드시 테스트를 먼저 작성한다. '실패하는 테스트'가 항상 구현보다 앞선다.
- RED 단계: tests/ 만 작성·수정. src/ 는 절대 건드리지 않는다.
- GREEN 단계: 실패 테스트를 통과시키는 '최소 구현'만 한다.
- 끝나기 전 반드시 pytest -q 로 전부 통과(GREEN)를 확인한다.
- 커밋은 RED(test)와 GREEN(feat)을 분리한다.

## 금지 (Don't)
- assert True · pytest.skip · 예외 삼키기 같은 우회 금지.
- 요청받지 않은 기존 테스트 수정·삭제 금지.
- 한 커밋에 RED와 GREEN을 섞지 않는다.
AGENTS.md 작성 5원칙
① 짧게 — 30줄이 300줄보다 낫다.  ② 테스트 “명령”을 명시한다.  ③ “성격”이 아니라 “행동”을 적는다.
④ 금지(Don't) 목록을 둔다 — 위 5조항은 벡의 두 경고 신호(과잉 구현·테스트 속임)를 규칙으로 옮긴 것으로, 에이전트가 “테스트 통과 자체”를 최적화하는 목표 왜곡을 차단하는 안전장치입니다.
⑤ 자세한 건 docs/로 미루고 여기엔 “어디를 보라”만 적는다.
▶ Codex CLI 프롬프트 — 하네스 적용 확인 (세션 시작 직후 1회)
AGENTS.md 를 읽고, 이 저장소에서 네가 지켜야 할 규칙을 5줄로 요약해줘.
특히 금지 5조항을 그대로 복창해줘. 파일은 수정하지 마.
# Repository instructions
장바구니 할인 계산기 — Python 3.12, pytest 기반 Dual-Track TDD 프로젝트.
이 파일은 백과사전이 아니라 '지침'이다.

## 프로젝트 구조
- src/cart.py  : Logic 트랙(순수 함수: 금액·할인 계산)
- src/app.py   : UI 트랙(Flask 주문 폼)
- tests/test_cart.py / tests/test_ui.py : 트랙별 테스트

## 테스트 명령
- 전체: pytest -q   - Logic: pytest tests/test_cart.py -q   - UI: pytest tests/test_ui.py -q

## 개발 워크플로 — TDD 필수
- 반드시 테스트를 먼저 작성한다. '실패하는 테스트'가 항상 구현보다 앞선다.
- RED 단계: tests/ 만 작성·수정. src/ 는 절대 건드리지 않는다.
- GREEN 단계: 실패 테스트를 통과시키는 '최소 구현'만 한다.
- 끝나기 전 반드시 pytest -q 로 전부 통과(GREEN)를 확인한다.
- 커밋은 RED(test)와 GREEN(feat)을 분리한다.

## 금지 (Don't)
- assert True · pytest.skip · 예외 삼키기 같은 우회 금지.
- 요청받지 않은 기존 테스트 수정·삭제 금지.
- 한 커밋에 RED와 GREEN을 섞지 않는다.
AGENTS.md 작성 5원칙
① 짧게 — 30줄이 300줄보다 낫다.  ② 테스트 “명령”을 명시한다.  ③ “성격”이 아니라 “행동”을 적는다.
④ 금지(Don't) 목록을 둔다 — 위 5조항은 벡의 두 경고 신호(과잉 구현·테스트 속임)를 규칙으로 옮긴 것으로, 에이전트가 “테스트 통과 자체”를 최적화하는 목표 왜곡을 차단하는 안전장치입니다.
⑤ 자세한 건 docs/로 미루고 여기엔 “어디를 보라”만 적는다.
▶ Codex CLI 프롬프트 — 하네스 적용 확인 (세션 시작 직후 1회)
AGENTS.md 를 읽고, 이 저장소에서 네가 지켜야 할 규칙을 5줄로 요약해줘.
특히 금지 5조항을 그대로 복창해줘. 파일은 수정하지 마.
