import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

browser_path = 'D:/CS232_Crawler/msedgedriver.exe'
browser = webdriver.ChromiumEdge(executable_path=browser_path)

browser.get("http://mbasic.facebook.com")

txtUser = browser.find_element(By.NAME, "email")
txtUser.send_keys("0865926082")

txtPass = browser.find_element(By.NAME, "pass")
txtPass.send_keys("dangle0000")

txtPass.send_keys(Keys.ENTER)
sleep(90)

pickle.dump(browser.get_cookies(), open("my_cookie.pkl", "wb"))

browser.close()