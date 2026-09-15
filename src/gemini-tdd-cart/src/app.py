from flask import Flask, render_template_string, request

from src.cart import final_total


app = Flask(__name__)

ORDER_FORM = """
<form method="post">
  <input name="price" type="number">
  <input name="qty" type="number">
  <input name="vip" type="checkbox">
  <button type="submit">계산</button>
</form>
{% if total is not none %}<p>{{ total }}</p>{% endif %}
"""


@app.route("/", methods=["GET", "POST"])
def order_form():
  total = None

  if request.method == "POST":
    price = request.form.get("price")
    qty = request.form.get("qty")

    if price is None or qty is None or int(qty) < 0:
      return "", 400

    items = [{"price": int(price), "qty": int(qty)}]
    total = f"{final_total(items, is_vip='vip' in request.form):,}"

  return render_template_string(ORDER_FORM, total=total)
