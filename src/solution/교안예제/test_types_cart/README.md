# 4종 테스트 비교 — 장바구니 final_total() 하나를 네 가지 방식으로

교안 Day 2 · 4교시 '불변식' 바로 뒤의 비교 슬라이드 예제. 같은 함수를 서로 다른 질문으로 검증한다.

| 파일 | 종류 | 묻는 것 |
|---|---|---|
| tests/test_1_parametrize.py | 파라미터 테스트 | 같은 규칙에 대해 여러 입력 → 기대값 표 |
| tests/test_2_property.py | 속성 테스트 | 어떤 입력에서도 항상 참인 성질 (hypothesis) |
| tests/test_3_characterization.py | 특성화 테스트 | 명세에 없지만 지금 이렇게 동작한다 |
| tests/test_4_approval.py | 승인(골든 마스터) 테스트 | 출력 전체를 파일로 고정하고 사람이 승인 |

```bash
pip install pytest hypothesis approvaltests
pytest -q                 # 4종 모두 통과
pytest -q -k parametrize  # 하나만
```
