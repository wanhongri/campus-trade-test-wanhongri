# -*- coding: utf-8 -*-
import time
from urllib.parse import urlencode
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
BASE = "http://127.0.0.1:5000"

PASS_N = 0
FAIL_N = 0

def report(tag, expect, got):
    global PASS_N, FAIL_N
    ok = (expect in got)
    if ok:
        PASS_N += 1
        print(f"[PASS] {tag} expect[{expect}]")
    else:
        FAIL_N += 1
        print(f"[FAIL] {tag} expect[{expect}] got[{got}]")

def get_body():
    return driver.find_element(By.TAG_NAME, "body").text

def t_login():
    print("\n===== 登录组(18条) =====")
    cases = [
        ("user1", "123456", "登录成功", "LOGIN_001"),
        ("user1", "wrong", "用户名或密码错误", "LOGIN_002"),
        ("nosuchuser", "123456", "用户名不存在", "LOGIN_003"),
        ("", "123456", "用户名不存在", "LOGIN_004"),
        ("user1", "", "用户名或密码错误", "LOGIN_005"),
        ("", "", "用户名不存在", "LOGIN_006"),
        ("user1", "123456", "登录成功", "LOGIN_007"),
        ("user1", "12345", "用户名或密码错误", "LOGIN_008"),
        (" user1 ", "123456", "用户名不存在", "LOGIN_009"), # 空格测试
        ("user2", "123456", "登录成功", "LOGIN_010"),
        ("USER1", "123456", "用户名不存在", "LOGIN_011"), # 大小写
        ("user1", "123456 ", "用户名或密码错误", "LOGIN_012"),
        ("user3", "123456", "用户名不存在", "LOGIN_013"),
        ("user1", "1234567", "用户名或密码错误", "LOGIN_014"),
        ("nosuchuser", "wrong", "用户名不存在", "LOGIN_015"),
        ("test", "test", "用户名不存在", "LOGIN_016"),
        ("admin", "admin", "用户名不存在", "LOGIN_017"),
        ("user2", "wrong", "用户名或密码错误", "LOGIN_018"),
    ]
    for u, p, expect, tag in cases:
        driver.get(BASE)
        if u: driver.find_element(By.NAME,"username").send_keys(u)
        if p: driver.find_element(By.NAME,"password").send_keys(p)
        driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
        time.sleep(1)
        report(tag, expect, get_body())

def t_products():
    print("\n===== 商品组(20条) =====")
    driver.get(BASE+"/products")
    time.sleep(1)
    body = get_body()
    cases = [
        ("华为手机", "PRODUCT_001"),
        ("苹果充电器", "PRODUCT_002"),
        ("高数教材", "PRODUCT_003"),
        ("¥", "PRODUCT_004"),
        ("库存10", "PRODUCT_005"),
        ("库存5", "PRODUCT_006"),
        ("缺货", "PRODUCT_007"),
        ("101", "PRODUCT_008"),
        ("102", "PRODUCT_009"),
        ("103", "PRODUCT_010"),
        ("2990.00", "PRODUCT_011"),
        ("149.00", "PRODUCT_012"),
        ("39.90", "PRODUCT_013"),
        ("数码", "PRODUCT_014"),
        ("教材", "PRODUCT_015"),
        ("华为", "PRODUCT_016"),
        ("苹果", "PRODUCT_017"),
        ("高数", "PRODUCT_018"),
        ("充电器", "PRODUCT_019"),
        ("手机", "PRODUCT_020"),
    ]
    for text, tag in cases:
        report(tag, text, body)

def t_order():
    print("\n===== 订单组(18条) =====")
    cases = [
        ({"pid":101,"qty":1}, "下单成功", "ORDER_001"),
        ({"pid":101,"qty":2}, "下单成功", "ORDER_002"),
        ({"pid":102,"qty":1}, "下单成功", "ORDER_003"),
        ({"pid":102,"qty":5}, "下单成功", "ORDER_004"),
        ({"pid":103,"qty":1}, "商品缺货，无法下单", "ORDER_005"), # 缺货
        ({"pid":101,"qty":0}, "数量至少为1", "ORDER_006"),       # 数量0
        ({"pid":101,"qty":-1}, "数量至少为1", "ORDER_007"),      # 负数
        ({"pid":101,"qty":11}, "超过库存", "ORDER_008"),        # 超库存
        ({"pid":102,"qty":6}, "超过库存", "ORDER_009"),
        ({"pid":999,"qty":1}, "商品不存在", "ORDER_010"),       # 不存在的商品
        ({"pid":0,"qty":1}, "商品不存在", "ORDER_011"),
        ({"pid":101,"qty":"abc"}, "商品不存在", "ORDER_012"),  # 非法字符
        ({"pid":102,"qty":3}, "下单成功", "ORDER_013"),
        ({"pid":101,"qty":10}, "下单成功", "ORDER_014"),
        ({"pid":102,"qty":4}, "下单成功", "ORDER_015"),
        ({"pid":103,"qty":5}, "商品缺货，无法下单", "ORDER_016"),
        ({"pid":101,"qty":5}, "下单成功", "ORDER_017"),
        ({"pid":101,"qty":100}, "超过库存", "ORDER_018"),
    ]
    for data, expect, tag in cases:
        try:
            req = urllib.request.Request(BASE+"/order", data=urlencode(data).encode())
            body = urllib.request.urlopen(req).read().decode()
        except Exception as e:
            body = f"请求异常:{str(e)}"
        report(tag, expect, body)

if __name__ == "__main__":
    print("=== 开始执行自动化测试 ===")
    try:
        t_login()
        t_products()
        t_order()
    except Exception as e:
        print(f"\n执行中断: {e}")
    finally:
        print(f"\n===== 汇总: PASS {PASS_N} 条, FAIL {FAIL_N} 条 =====")
        time.sleep(5)
        driver.quit()