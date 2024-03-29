from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
#直接访问邮件系统
url = 'https://i.qzoiedu.com/message_pocket_web/inboxpc/pc.html#/messageDetail'
driver.get(url)

wait = WebDriverWait(driver, 10)  # 等待最多10秒

#直接访问会需要重新登录
def login():
    input_username = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]')))  
    input_userpassword = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
    input_username.send_keys('xxx')
    input_userpassword.send_keys('xxx')
    input_submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login_submit"]')))
    input_submit.click()
    time.sleep(5)

#处理“其他服务”
def otherServer():
    other_part = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@title="其他服务"]')))
    other_part.click()
    time.sleep(5)

#先让邮件列表滚动至最底部，便于获取所有的邮件
def scrollEmailList():
    scroll_email = driver.find_element(By.XPATH,'//div[@class="message-list"]')
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scroll_email)
    time.sleep(5)

#获取邮件列表
def getEmailList():
    message_list = driver.find_elements(By.XPATH,'//span[@title="您收到一条消息提醒"]')
    for i in range(len(message_list)):
        message_list[i].click()
        time.sleep(2)
#正式开始
login()
otherServer()
scrollEmailList()
getEmailList()

driver.quit()