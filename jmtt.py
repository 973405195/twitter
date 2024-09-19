from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://18comic.org/albums?o=mv'



options = webdriver.ChromeOptions()

options.add_argument("--disable-blink-features=AutomationControlled")  # 就是这一行告诉chrome去掉了webdriver痕迹
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 可以去掉提示受到自动软件控制
driver = webdriver.Chrome(options=options)



driver.get(url)
sleep(2)
driver.find_element(By.XPATH,'//*[@id="footer-text"]/a').click()
sleep(2)
all_handles = driver.window_handles

# 切换到索引为1的窗口（第二个窗口）
driver.switch_to.window(all_handles[1])
sleep(2)
driver.get(url)
sleep(25)
window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])
driver.refresh()

# 等待reCAPTCHA验证完成
sleep(5)  # 假设验证需要5秒
list1 = driver.find_elements(By.XPATH,'//*[@id="wrapper"]/div[5]/div[2]/div[1]/div[2]/div/div/div[1]/a/img')
zuozhe = driver.find_elements(By.XPATH,'//*[@id="wrapper"]/div[5]/div[2]/div[1]/div[2]/div/div/div[2]')
biaoqian = driver.find_elements(By.XPATH,'//*[@id="wrapper"]/div[5]/div[2]/div[1]/div[2]/div/div/div[3]')
for i,z,b in zip(list1, zuozhe, biaoqian):
    print(i.get_attribute('title'))
    print(i.get_attribute('src'))
    print(z.text)
    print(b.text)

sleep(10000)


