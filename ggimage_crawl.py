from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import validators
import requests
import os
import urllib.request

name = input("Image title: ")
os.mkdir('image/' + str(name))

driver = webdriver.ChromiumEdge(executable_path="msedgedriver.exe")
driver.get("https://www.google.com/imghp?hl=en") #Link gg images
elem = driver.find_element(By.NAME, "q")
elem.send_keys(name)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        # //*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img
        imgUrl = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
        valid = validators.url(imgUrl)
        if valid:
            urllib.request.urlretrieve(imgUrl, 'image/' + str(name) + "/" + str(name) + "_" + str(count).zfill(3) + ".jpg")
            count = count + 1
            # img_data = requests.get(imgUrl).content
            # with open('image/' + str(name) + "_" + str(count).zfill(3) + '.jpg', 'wb') as handler:
            #     handler.write(img_data)
    except:
        pass

driver.close()