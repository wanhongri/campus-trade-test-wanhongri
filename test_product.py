import pytest
from selenium.webdriver.common.by import By

BASE = "http://127.0.0.1:5000"

product_data = [
    ("华为手机", "PRODUCT_001"), ("苹果充电器", "PRODUCT_002"), ("高数教材", "PRODUCT_003"),
    ("¥", "PRODUCT_004"), ("库存10", "PRODUCT_005"), ("库存5", "PRODUCT_006"),
    ("缺货", "PRODUCT_007"), ("101", "PRODUCT_008"), ("102", "PRODUCT_009"),
    ("103", "PRODUCT_010"), ("2990.00", "PRODUCT_011"), ("149.00", "PRODUCT_012"),
    ("39.90", "PRODUCT_013"), ("数码", "PRODUCT_014"), ("教材", "PRODUCT_015"),
    ("华为", "PRODUCT_016"), ("苹果", "PRODUCT_017"), ("高数", "PRODUCT_018"),
    ("充电器", "PRODUCT_019"), ("手机", "PRODUCT_020"),
]

@pytest.mark.parametrize("text, tag", product_data)
def test_product(driver, text, tag):
    driver.get(BASE + "/products")
    body = driver.find_element(By.TAG_NAME, "body").text
    assert text in body, f"用例 {tag} 失败：商品页未找到[{text}]"