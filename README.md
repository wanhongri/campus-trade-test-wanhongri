# 校园二手交易系统核心模块测试

本项目配合开发完成校园二手交易系统的质量保障工作，覆盖登录、商品管理、订单交易三大核心模块。

## 技术栈
- Python + Selenium：核心模块自动化回归
- Python urllib：接口测试（参数与返回值校验）
- MySQL：数据存储一致性校验（sql_verify/目录）

## 目录说明
- `testcases/`    # 测试用例设计（等价类、边界值）
- `selenium_scripts/` # Selenium 自动化脚本
- `postman/`      # 接口测试脚本及截图
- `sql_verify/`   # MySQL 数据校验语句
- `defects/`      # 缺陷跟踪
- `reports/`      # 测试报告与截图
- `docs/`         # 需求、接口文档

## 环境搭建
1. 安装 Python
2. 安装依赖库：`pip install selenium flask webdriver-manager`
3. 确保本地已安装 Edge 浏览器（脚本已适配 Edge 驱动自动配置）

## 运行方法
1. 启动 Flask 模拟商城（终端1）：
   ```bash
   python app.py