import time
import pytest
from selenium.webdriver.common.by import By

BASE = "http://127.0.0.1:5000"

login_data = [
    ("user1", "123456", "登录成功", "LOGIN_001"),
    ("user1", "wrong", "用户名或密码错误", "LOGIN_002"),
    ("nosuchuser", "123456", "用户名不存在", "LOGIN_003"),
    ("", "123456", "用户名不存在", "LOGIN_004"),
    ("user1", "", "用户名或密码错误", "LOGIN_005"),
    ("", "", "用户名不存在", "LOGIN_006"),
    ("user1", "123456", "登录成功", "LOGIN_007"),
    ("user1", "12345", "用户名或密码错误", "LOGIN_008"),
    (" user1 ", "123456", "用户名不存在", "LOGIN_009"),
    ("user2", "123456", "登录成功", "LOGIN_010"),
    ("USER1", "123456", "用户名不存在", "LOGIN_011"),
    ("user1", "123456 ", "用户名或密码错误", "LOGIN_012"),
    ("user3", "123456", "用户名不存在", "LOGIN_013"),
    ("user1", "1234567", "用户名或密码错误", "LOGIN_014"),
    ("nosuchuser", "wrong", "用户名不存在", "LOGIN_015"),
    ("test", "test", "用户名不存在", "LOGIN_016"),
    ("admin", "admin", "用户名不存在", "LOGIN_017"),
    ("user2", "wrong", "用户名或密码错误", "LOGIN_018"),
]

@pytest.mark.parametrize("u, p, expect, tag", login_data)
def test_login(driver, u, p, expect, tag):
    driver.get(BASE)
    if u: driver.find_element(By.NAME, "username").send_keys(u)
    if p: driver.find_element(By.NAME, "password").send_keys(p)
    
    driver.find_element(By.CSS_SELECTOR, "input[type=submit]").click()
    time.sleep(1) # 关键修复：强制等待1秒，给网页刷新时间
    
    body = driver.find_element(By.TAG_NAME, "body").text
    assert expect in body, f"用例 {tag} 失败：预期[{expect}]，实际[{body}]"