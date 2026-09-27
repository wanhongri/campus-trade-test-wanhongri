import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

print("=== 1. 开始启动 Edge 浏览器，首次运行需要匹配驱动，请耐心等待 ===")
options = webdriver.EdgeOptions()
# 关键修复：使用 Edge 驱动，解决找不到 Chrome 二进制文件的问题
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
print("=== 2. 浏览器启动成功，准备开始执行测试用例 ===\n")

def login(u, p, expect):
    print(f"-> 正在执行: 账号=[{u}] 密码=[{p}]")
    
    # 每次执行用例前，重新打开登录页
    driver.get("http://127.0.0.1:5000")
    
    # 寻找输入框并输入内容
    driver.find_element(By.NAME, "username").send_keys(u)
    driver.find_element(By.NAME, "password").send_keys(p)
    
    # 寻找登录按钮并点击
    driver.find_element(By.CSS_SELECTOR, "input[type=submit]").click()
    
    # 获取页面返回的提示信息
    msg = driver.find_element(By.TAG_NAME, "body").text
    
    # 判断预期结果是否在页面提示中
    ok = expect in msg
    
    # 打印执行结果
    print(("PASS" if ok else "FAIL"), f"LOGIN: {u}/{p} -> expect[{expect}] got[{msg}]")

# ================= 测试用例 =================
login("user1", "123456", "登录成功")      # LOGIN_001
login("user1", "wrong", "用户名或密码错误") # LOGIN_002
login("nosuch", "123456", "用户名不存在")  # LOGIN_003
login("", "123456", "用户名")             # LOGIN_004
login("user1", "", "密码")                # LOGIN_005
# ============================================

print("\n=== 3. 所有测试用例执行完毕！5秒后自动关闭浏览器 ===")
time.sleep(5)
driver.quit()