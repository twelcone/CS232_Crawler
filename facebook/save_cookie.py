import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.ChromiumEdge(executable_path='D:/CS232_Crawler/msedgedriver.exe')

browser.get("http://mbasic.facebook.com")

txtUser = browser.find_element(By.NAME, "email")
txtUser.send_keys("0865926082")

txtPass = browser.find_element(By.NAME, "pass")
txtPass.send_keys("dangle0000")

txtPass.send_keys(Keys.ENTER)
sleep(90)

# browser.find_element(By.XPATH, "/html/body/div/div/div/div/table/tbody/tr/td/div/div[3]/a").click()
# sleep(5)

pickle.dump(browser.get_cookies(), open("my_cookie.pkl", "wb"))

browser.close()