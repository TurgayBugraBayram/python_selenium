from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.google.com")
# sleep(2)
# input = driver.find_element(By.NAME,"q")
# input.send_keys("kesifplus")
# button = driver.find_element(By.NAME,"btnK")
# sleep(2)
# button.click()
# sleep(2)
# result = driver.find_element(By.XPATH,"//*[@id='rso']/div[4]/div/div/div[1]/div/a")
# result.click()
# sleep(5)
# #/html/body/div[6]/div/div[11]/div/div[2]/div[2]/div/div/div[4]/div/div/div/div[1]/div/a
# #//*[@id="rso"]/div[4]/div/div/div/div[1]/div/a


# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.github.com")
# seaerch = driver.find_element(By.NAME,"q")
# seaerch.send_keys("python")
# sleep(2)
# seaerch.send_keys(Keys.ENTER)
# sleep(2)
# # result = driver.find_elements(By.CLASS_NAME,"repo-list")
# # for element in result:
# #     print(element.text)
#
# # result = driver.find_elements(By.CSS_SELECTOR,".repo-list")
# # for element in result:
# #     print(element)
# #
#
# source = driver.page_source
# print(source)
# driver.close()


"""
xpath : //*[@id="login_field"]
"""

class github_login:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://github.com/login")
    def login(self):
        self.driver.find_element(By.ID,"login_field").send_keys(self.username)
        sleep(2)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[1]").send_keys(self.password)
        sleep(2)
        self.driver.find_element(By.NAME,"commit").click()
        sleep(2)

user1 = github_login("abc","123")
user1.login()