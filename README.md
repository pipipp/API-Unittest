# 基于Unittest搭建的接口自动化测试框架
可在其基础上进行扩展和延申。

## 目录结构

├─logs  
│      unittest_project.log  
│  
├─reports  
│  │  __init__.py  
│  │  
│  └─2021-03-04  
│          18_42_05_unittest_project.html  
│          18_43_46_unittest_project.html  
│  
├─test_case_file  
│      test_api.xlsx  
│  
├─test_scripts  
│  │  case_top.py  
│  │  test_proxy_api.py  
│  │  __init__.py  
│  
├─utils  
│  │  common_module.py  
│  │  db_module.py  
│  │  email_module.py  
│  │  load_case_file_module.py  
│  │  logger_module.py  
│  │  output_report_module.py  
│  │  request_module.py  
│  │  __init__.py  

## 技术栈

测试工具（请求接口）：
* python + requests  

测试框架（管理用例、执行用例、断言）：  
* unittest

数据驱动（参数化）：
* excel
* ddt

生成测试报告：
* HtmlTestRunner
* BeautifulReport

发送邮件：
* smtplib
* email
