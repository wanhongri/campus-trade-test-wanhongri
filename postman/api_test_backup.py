# -*- coding: utf-8 -*-
import urllib.request
from urllib.parse import urlencode

BASE = "http://127.0.0.1:5000"
PASS_N = 0
FAIL_N = 0

def test_api(name, url, data, expect):
    global PASS_N, FAIL_N
    try:
        req = urllib.request.Request(url, data=urlencode(data).encode())
        res = urllib.request.urlopen(req).read().decode()
        if expect in res:
            PASS_N += 1
            print(f"[PASS] {name} 接口返回符合预期")
        else:
            FAIL_N += 1
            print(f"[FAIL] {name} 预期: {expect}, 实际: {res}")
    except Exception as e:
        FAIL_N += 1
        print(f"[FAIL] {name} 接口异常: {e}")

if __name__ == "__main__":
    print("=== 开始执行接口测试 ===")
    test_api("登录接口-成功", BASE+"/login", {"username":"user1","password":"123456"}, "登录成功")
    test_api("登录接口-失败", BASE+"/login", {"username":"user1","password":"wrong"}, "用户名或密码错误")
    test_api("订单接口-正常", BASE+"/order", {"pid":101,"qty":1}, "下单成功")
    test_api("订单接口-异常", BASE+"/order", {"pid":101,"qty":0}, "数量至少为1")
    print(f"=== 接口测试汇总: PASS {PASS_N}, FAIL {FAIL_N} ===")