from flask import Flask, request, render_template

app = Flask(__name__)

USERS = {"user1": "123456", "user2": "123456"}  # 合法账号密码
PRODUCTS = [
    {"id": 101, "name": "华为手机", "price": 2990.00, "stock": 10, "cat": "数码"},
    {"id": 102, "name": "苹果充电器", "price": 149.00, "stock": 5, "cat": "数码"},
    {"id": 103, "name": "高数教材", "price": 39.90, "stock": 0, "cat": "教材"},
]

orders = []
order_no = 1000

# 让主页同时支持 GET(展示页面) 和 POST(接收表单提交)
@app.route("/", methods=["GET", "POST"])
def index():
    msg = ""
    if request.method == "POST":
        u = request.form.get("username", "").strip()
        p = request.form.get("password", "").strip()
        if u not in USERS:
            msg = "用户名不存在"
        elif USERS[u] != p:
            msg = "用户名或密码错误"
        else:
            msg = "登录成功"
    # 将 msg 返回到前端页面进行渲染
    return render_template("login.html", msg=msg)

# 保留 /login 路由以防表单 action 指向这里，同样处理逻辑
@app.route("/login", methods=["POST"])
def login():
    u = request.form.get("username", "").strip()
    p = request.form.get("password", "").strip()
    if u not in USERS:
        msg = "用户名不存在"
    elif USERS[u] != p:
        msg = "用户名或密码错误"
    else:
        msg = "登录成功"
    return render_template("login.html", msg=msg)

@app.route("/products")
def products():
    txt = ""
    for it in PRODUCTS:
        flag = "缺货" if it["stock"] == 0 else f"库存{it['stock']}"
        txt += f"{it['id']} {it['name']} ¥{it['price']:.2f} {flag}<br>"
    return txt

@app.route("/order", methods=["POST"])
def order():
    global order_no
    pid = int(request.form.get("pid", 0))
    qty = int(request.form.get("qty", 0))
    if qty <= 0:
        return "数量至少为1"
    it = next((x for x in PRODUCTS if x["id"] == pid), None)
    if it is None:
        return "商品不存在"
    if it["stock"] == 0:
        return "商品缺货，无法下单"
    if qty > it["stock"]:
        return "超过库存"
    order_no += 1
    total = it["price"] * qty
    orders.append({"no": order_no, "pid": pid, "qty": qty, "total": total})
    return f"下单成功 订单号{order_no} 金额{total:.2f}元"

if __name__ == "__main__":
    app.run(port=5000)