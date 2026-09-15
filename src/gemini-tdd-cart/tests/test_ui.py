import pytest

from src.app import app


def make_client():
  app.config["TESTING"] = True
  return app.test_client()


@pytest.mark.ui
def test_e_1_음수_수량은_정상_합계가_아니라_오류다():
  response = make_client().post(
    "/",
    data={"price": "12000", "qty": "-1", "vip": ""},
  )

  assert 400 <= response.status_code < 500
  assert "0" not in response.get_data(as_text=True)


@pytest.mark.ui
def test_e_2_items_없는_주문은_500이_아닌_통제된_오류다():
  response = make_client().post("/", data={})

  assert response.status_code != 500
  assert 400 <= response.status_code < 500


@pytest.mark.ui
def test_u_1_주문_입력_폼을_표시한다():
  response = make_client().get("/")
  html = response.get_data(as_text=True)

  assert response.status_code == 200
  assert 'method="post"' in html.lower()
  assert 'name="price"' in html
  assert 'name="qty"' in html
  assert 'name="vip"' in html


@pytest.mark.ui
def test_u_2_vip_주문의_최종_금액을_표시한다():
  response = make_client().post(
    "/",
    data={"price": "60000", "qty": "1", "vip": "on"},
  )

  assert response.status_code == 200
  assert "51,300" in response.get_data(as_text=True)
