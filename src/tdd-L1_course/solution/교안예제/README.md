# 교안 예제 코드

교안 슬라이드의 코드와 실행 결과는 모두 이 폴더에서 `pytest -v` 로 실제 실행한 것이다.
각 폴더에서 `pip install pytest approvaltests` 후 `pytest -q`.

first_indep · first_repeat · first_self_fix 는 교안에서 '실패하는 모습'을 보여 주는 예제라 실패가 정상이다 (first_self_fix 는 greet.py 의 'Helo' 를 'Hello' 로 고치면 GREEN).

| 폴더 | 교안 |
|---|---|
| first_fast | 2.2 F · Fast — 느린 테스트 |
| first_fast_fix | 2.2 F · 개선 — 대역 |
| first_indep | 2.2 I · Independent — 전역 상태 공유 |
| first_indep_fix | 2.2 I · 개선 — fixture |
| first_repeat | 2.2 R · Repeatable — 현재 시각 의존 |
| first_repeat_fix | 2.2 R · 개선 — 시계 주입 |
| first_self | 2.2 S · Self-validating — 출력만 |
| first_self_fix | 2.2 S · 개선 — capsys |
| first_timely | 2.2 T · Timely — RED → GREEN |
| bicep | 2.3 Right-BICEP |
| correct | 2.3 CORRECT |
| prop | 1.3 Example vs Property |
| smell_duplicate | 3.1 ① 중복 코드 |
| smell_long_function | 3.1 ② 긴 함수 |
| smell_large_class | 3.1 ③ 거대한 클래스 |
| smell_long_params | 3.1 ④ 긴 매개변수 목록 |
| smell_dead_code | 3.1 ⑤ 죽은 코드 |
| smell_magic_number | 3.1 ⑥ 매직 넘버 |
| smell_deep_nesting | 3.1 ⑦ 깊은 중첩 |
| smell_bad_names | 3.1 ⑧ 부적절한 이름 |
| 부록A_gilded_rose | 부록 A — 테스트 안전망 (Conjured 포함 17 passed) |
| 부록B_gilded_rose | 부록 B — 리팩터링 최종 구조 (레거시와 30일 출력 비교 포함 20 passed) |
