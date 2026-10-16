# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(scope="function")
def driver():
    print("\n[Setup] 正在启动 Edge 浏览器...")
    options = webdriver.EdgeOptions()
    # 加上无头模式（后台运行），如果你想看浏览器操作画面，把这行注释掉
    # options.add_argument('--headless') 
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
    driver.implicitly_wait(5) # 智能隐式等待：找不到元素时自动等5秒
    yield driver
    print("\n[Teardown] 关闭浏览器")
    driver.quit()