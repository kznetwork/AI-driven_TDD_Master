from src.cart import subtotal


def test_ac_1_tc_1_subtotal은_각_항목의_금액을_모두_더한다():
  items = [
    {"price": 1000, "qty": 3},
    {"price": 2000, "qty": 2},
  ]

  assert subtotal(items) == 7000


def test_e_3_tc_3_금액이_50000이면_10퍼센트_할인한다():
  from src import cart

  assert cart.apply_threshold_discount(50000) == 45000


def test_e_2_tc_4_금액이_49999이면_할인하지_않는다():
  from src import cart

  assert cart.apply_threshold_discount(49999) == 49999


def test_u_1_tc_7_vip이면_문턱_할인_후_5퍼센트를_추가_할인한다():
  from src import cart

  items = [{"price": 60000, "qty": 1}]

  assert cart.final_total(items, is_vip=True) == 51300
