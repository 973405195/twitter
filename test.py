# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium.webdriver.chrome.service import Service
#
#
# # 设置好你的Twitter登录凭据
# username = "harris_ann51631"
# password = "8fHMkjsm7Me5G0s"
#
# service = Service('chromedriver.exe')  # 设定chromedriver路径
#
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option('useAutomationExtension', False)
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_argument('--start-maximized')
# options.add_argument('disable-infobars')
# options.add_argument("--start-maximized")
#
# # 启动浏览器
# driver = webdriver.Chrome(options=options,service=service)
# driver.get("https://x.com/i/flow/login")
# time.sleep(10)
# # 输入用户名和密码
# username_element = driver.find_element(By.NAME, "text")
# username_element.send_keys(username+'\n')
# time.sleep(2)
# password_element = driver.find_element(By.NAME, "password")
# password_element.send_keys(password+'\n')
#
# # # 提交登录信息
# # login_button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
# # login_button.click()
# #
# # # 等待2FA页面加载
# # two_factor_page_element = WebDriverWait(driver, 10).until(
# #     EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='loginModal']"))
# # )
# #
# # # 处理2FA（以下代码假设你有一个2FA应用生成6位验证码）
# two_factor_code = input("请输入你的2FA验证码: ")
# code_element = driver.find_element(By.NAME, "text")
# code_element.send_keys(two_factor_code+'\n')
# input()
# driver_cookies = driver.get_cookies()
#
# token_cookie = next((cookie for cookie in driver_cookies if cookie['name'] == 'auth_token'), None)
#
# if token_cookie:
#     print('Token:', token_cookie['value'])
#
# else:
#     print('Token not found.')
#
# driver_cookie_str = ''
#
# for cookie in driver_cookies:
#     driver_cookie_str += f"{cookie['name']}={cookie['value']}; "
# print(driver_cookie_str)
# # 关闭浏览器
# time.sleep(5)  # 等待一会儿以便让用户看到登录成功的结果
# driver.quit()


import requests

url = 'https://x.com/i/flow/login'
headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 8.0.0; LG-H870S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36;'

}
data = {
                'auth_token': '311410cd63b50069d0195c9564017cc2ddfead01'
            }
response = requests.post(url, data=data, stream=True,headers=headers)
# 检查是否登录成功
if response.ok:
    # 获取登录后的cookies
    cookie_str = response.headers.get("set-cookie")
    # # #获取登录后的token
    # au_token = response.json().get("token")
    # test_cookies = response.cookies
    #
    # cookie_str += f"'; auth_token={data['auth_token']}"
    print(cookie_str)
else:
    print('登录失败')