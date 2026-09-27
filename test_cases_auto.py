# -*- coding: utf-8 -*-
import time
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
        print(f"[PASS] {tag}  expect[{expect}] got[{got}]")
    else:
        FAIL_N += 1
        print(f"[FAIL] {tag}  expect[{expect}] got[{got}]")

def get_body():
    return driver.find_element(By.TAG_NAME, "body").text

def t_login():
    print("\n===== 登录组执行开始 =====")
    driver.get(BASE); driver.find_element(By.NAME,"username").send_keys("user1")
    driver.find_element(By.NAME,"password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
    time.sleep(1) # 等待页面刷新
    report("LOGIN_001", "登录成功", get_body())

    driver.get(BASE); driver.find_element(By.NAME,"username").send_keys("user1")
    driver.find_element(By.NAME,"password").send_keys("wrong")
    driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
    time.sleep(1)
    report("LOGIN_002", "用户名或密码错误", get_body())

    driver.get(BASE); driver.find_element(By.NAME,"username").send_keys("nosuchuser")
    driver.find_element(By.NAME,"password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
    time.sleep(1)
    report("LOGIN_003", "用户名不存在", get_body())

    driver.get(BASE); driver.find_element(By.NAME,"username").clear()
    driver.find_element(By.NAME,"password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
    time.sleep(1)
    report("LOGIN_004", "用户名不存在", get_body())

    driver.get(BASE); driver.find_element(By.NAME,"username").send_keys("user1")
    driver.find_element(By.NAME,"password").clear()
    driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
    time.sleep(1)
    report("LOGIN_005", "用户名或密码错误", get_body())

    driver.get(BASE); driver.find_element(By.NAME,"username").clear()
    driver.find_element(By.NAME,"password").clear()
    driver.find_element(By.CSS_SELECTOR,"input[type=submit]").click()
    time.sleep(1)
    report("LOGIN_006", "用户名不存在", get_body())

def t_products():
    print("\n===== 商品组执行开始 =====")
    driver.get(BASE+"/products")
    time.sleep(1)
    report("PRODUCT_001", "华为手机", get_body())
    report("PRODUCT_002", "苹果充电器", get_body())
    report("PRODUCT_003", "¥", get_body())

def t_order():
    print("\n===== 订单组执行开始 =====")
    from urllib.parse import urlencode
    import urllib.request
    
    data = urlencode({"pid":101,"qty":1}).encode()
    req = urllib.request.Request(BASE+"/order", data=data)
    body = urllib.request.urlopen(req).read().decode()
    report("ORDER_006", "下单成功", body)

if __name__ == "__main__":
    print("=== 开始执行自动化测试，请勿关闭浏览器 ===")
    try:
        t_login()
        t_products()
        t_order()
    except Exception as e:
        print(f"\n执行过程中发生错误: {e}")
    finally:
        print(f"\n===== 汇总: PASS {PASS_N} 条, FAIL {FAIL_N} 条 =====")
        print("=== 测试结束，5秒后关闭浏览器 ===")
        time.sleep(5)
        driver.quit()