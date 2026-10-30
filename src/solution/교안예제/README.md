# 교안 예제 코드 (강사용)

교안 슬라이드의 코드와 실행 결과는 모두 이 폴더에서 `pytest -v` 로 실제 실행한 것이다.
각 폴더에서 `pip install pytest approvaltests hypothesis` 후 `pytest -q`.

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
| gwt | 2.4 Given-When-Then (Gherkin → pytest) |
| design_patterns/dp_refactor_vs_restructure | 3.1 리팩토링 vs 리스트럭처링 |
| design_patterns/dp_pull_up | 3.9 Pull Up Field · Method |
| design_patterns/dp_template_method | 3.9 긴 함수의 중복 → 템플릿 메서드 |
| design_patterns/dp_command | 3.9 함수를 명령으로 바꾸기 |
| design_patterns/dp_factory_method | 3.9 팩토리 메서드 |
| design_patterns/dp_feature_envy | 3.9 기능 편애 → 메서드 이동 |
| design_patterns/dp_strategy | 3.9 전략 패턴 (할인 정책) |
| design_patterns/dp_strategy_gilded_rose | 3.9 Gilded Rose 에 전략 적용 |
| design_patterns/dp_visitor | 3.9 방문자 패턴 |
| property_based/prop_calc · prop_cart | 부록 C 속성 테스트 (hypothesis) |
| gwt | 2.4 Given-When-Then (Gherkin → pytest) |
| design_patterns/dp_refactor_vs_restructure | 3.1 리팩토링 vs 리스트럭처링 |
| design_patterns/dp_pull_up | 3.9 Pull Up Field · Method |
| design_patterns/dp_template_method | 3.9 긴 함수의 중복 → 템플릿 메서드 |
| design_patterns/dp_command | 3.9 함수를 명령으로 바꾸기 |
| design_patterns/dp_factory_method | 3.9 팩토리 메서드 |
| design_patterns/dp_feature_envy | 3.9 기능 편애 → 메서드 이동 |
| design_patterns/dp_strategy | 3.9 전략 패턴 (할인 정책) |
| design_patterns/dp_strategy_gilded_rose | 3.9 Gilded Rose 에 전략 적용 |
| design_patterns/dp_visitor | 3.9 방문자 패턴 |
| property_based/prop_calc · prop_cart | 부록 C 속성 테스트 (hypothesis) |
| gwt | 2.4 Given-When-Then (Gherkin → pytest) |
| design_patterns/dp_refactor_vs_restructure | 3.1 리팩토링 vs 리스트럭처링 |
| design_patterns/dp_pull_up | 3.9 Pull Up Field · Method |
| design_patterns/dp_template_method | 3.9 긴 함수의 중복 → 템플릿 메서드 |
| design_patterns/dp_command | 3.9 함수를 명령으로 바꾸기 |
| design_patterns/dp_factory_method | 3.9 팩토리 메서드 |
| design_patterns/dp_feature_envy | 3.9 기능 편애 → 메서드 이동 |
| design_patterns/dp_strategy | 3.9 전략 패턴 (할인 정책) |
| design_patterns/dp_strategy_gilded_rose | 3.9 Gilded Rose 에 전략 적용 |
| design_patterns/dp_visitor | 3.9 방문자 패턴 |
| property_based/prop_calc · prop_cart | 부록 C 속성 테스트 (hypothesis) |
| gwt | 2.4 Given-When-Then (Gherkin → pytest) |
| design_patterns/dp_refactor_vs_restructure | 3.1 리팩토링 vs 리스트럭처링 |
| design_patterns/dp_pull_up | 3.9 Pull Up Field · Method |
| design_patterns/dp_template_method | 3.9 긴 함수의 중복 → 템플릿 메서드 |
| design_patterns/dp_command | 3.9 함수를 명령으로 바꾸기 |
| design_patterns/dp_factory_method | 3.9 팩토리 메서드 |
| design_patterns/dp_feature_envy | 3.9 기능 편애 → 메서드 이동 |
| design_patterns/dp_strategy | 3.9 전략 패턴 (할인 정책) |
| design_patterns/dp_strategy_gilded_rose | 3.9 Gilded Rose 에 전략 적용 |
| design_patterns/dp_visitor | 3.9 방문자 패턴 |
| property_based/prop_calc · prop_cart | 부록 C 속성 테스트 (hypothesis) |
| 부록A_gilded_rose | 부록 A — 테스트 안전망 (Conjured 포함 17 passed) |
| 부록B_gilded_rose | 부록 B — 리팩터링 최종 구조 (레거시와 30일 출력 비교 포함 20 passed) |
