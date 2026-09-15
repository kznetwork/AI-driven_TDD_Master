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
