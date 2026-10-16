import pytest
import urllib.request
from urllib.parse import urlencode

BASE = "http://127.0.0.1:5000"

order_data = [
    ({"pid":101,"qty":1}, "下单成功", "ORDER_001"),
    ({"pid":101,"qty":2}, "下单成功", "ORDER_002"),
    ({"pid":102,"qty":1}, "下单成功", "ORDER_003"),
    ({"pid":102,"qty":5}, "下单成功", "ORDER_004"),
    ({"pid":103,"qty":1}, "商品缺货，无法下单", "ORDER_005"),
    ({"pid":101,"qty":0}, "数量至少为1", "ORDER_006"),
    ({"pid":101,"qty":-1}, "数量至少为1", "ORDER_007"),
    ({"pid":101,"qty":11}, "超过库存", "ORDER_008"),
    ({"pid":102,"qty":6}, "超过库存", "ORDER_009"),
    ({"pid":999,"qty":1}, "商品不存在", "ORDER_010"),
    ({"pid":0,"qty":1}, "商品不存在", "ORDER_011"),
    ({"pid":101,"qty":"abc"}, "商品不存在", "ORDER_012"),
    ({"pid":102,"qty":3}, "下单成功", "ORDER_013"),
    ({"pid":101,"qty":10}, "下单成功", "ORDER_014"),
    ({"pid":102,"qty":4}, "下单成功", "ORDER_015"),
    ({"pid":103,"qty":5}, "商品缺货，无法下单", "ORDER_016"),
    ({"pid":101,"qty":5}, "下单成功", "ORDER_017"),
    ({"pid":101,"qty":100}, "超过库存", "ORDER_018"),
]

@pytest.mark.parametrize("data, expect, tag", order_data)
def test_order(data, expect, tag):
    try:
        req = urllib.request.Request(BASE + "/order", data=urlencode(data).encode())
        body = urllib.request.urlopen(req).read().decode()
    except Exception as e:
        body = f"请求异常:{str(e)}"
    assert expect in body, f"用例 {tag} 失败：预期[{expect}]，实际[{body}]"