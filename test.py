from selenium import webdriver
from time import sleep

browser = webdriver.ChromiumEdge(executable_path='msedgedriver.exe')
browser.get('https://google.com')
sleep(5)
browser.close()