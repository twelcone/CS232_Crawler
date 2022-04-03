import pickle
from selenium import webdriver
from time import sleep
import pandas as pd
import os

def readData(fileName):
    f = open(fileName, 'r', encoding='utf-8')
    data = []
    for i, line in enumerate(f):
        try:
            line = repr(line)
            line = line[1:len(line) - 3]
            data.append(line)
        except:
            print("error write line")
    return data

def writeFileTxt(fileName, content):
    with open(fileName, 'a') as f1:
        if os.stat(fileName).st_size == 0:
            f1.write(content)
        else:
            f1.write("\n")
            f1.write(content)

def getPostIds(driver, filePath):
    allPosts = readData(filePath)
    sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    shareBtn = driver.find_elements_by_xpath('//a[contains(@href, "/sharer.php")]')
    if (len(shareBtn)):
        for link in shareBtn:
            postId = link.get_attribute('href').split('sid=')[1].split('&')[0]
            if postId not in allPosts:
                print(postId)
                writeFileTxt(filePath, postId)


def getnumOfPostFanpage(driver, pageId, amount, filePath):
    driver.get("https://touch.facebook.com/" + pageId)
    while len(readData(filePath)) < amount:
        getPostIds(driver, filePath)

browser = webdriver.ChromiumEdge(executable_path="D:/CS232_Crawler/msedgedriver.exe")

browser.get("https://mbasic.facebook.com")

cookies = pickle.load(open("my_cookie.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

browser.get("https://mbasic.facebook.com")
sleep(5)

getnumOfPostFanpage(browser, 'FcThuyTien', 10, 'D:/CS232_Crawler/facebook/posts.csv')

sleep(1)
browser.close()