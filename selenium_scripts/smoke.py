# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(
    service=Service(EdgeChromiumDriverManager().install())
)
driver.get("http://www.baidu.com")
print("Smoke 测试通过：", driver.title)
driver.quit()
