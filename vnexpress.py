import random
from turtle import title
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
# 1. Khai báo browser
browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get("https://vnexpress.net/")
sleep(3)

 
title_news_links = []    
title_news_list = browser.find_elements(By.CLASS_NAME, "title-news")
for title_news in title_news_list:
    title_news_links.append(title_news.find_element(By.TAG_NAME,'a').get_attribute("href"))
print(len(title_news_links))
browser.close()
#3. Lấy thông tin trong bài 
# entire_title_news, entire_date, entire_comment = [], [], []
i = 0
for title_news_link in title_news_links:
    df1 = pd.DataFrame({"Author": [],
                        "Comment": []})

    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    browser.get(title_news_link)
    #Lấy title
    try:
        show_title = browser.find_element(By.CLASS_NAME, 'title-detail').text
    except:
        show_title = browser.find_element(By.CLASS_NAME,'title-news').text
    #Lấy ngày đăng bài
    show_date = browser.find_element(By.CLASS_NAME,'date').text
    # Lấy nội dung tóm tắt
    show_description = browser.find_element(By.CLASS_NAME,'description').text
    with open("results/" + str(i).zfill(3) + ".txt", "w+", encoding="utf-8") as f:
        f.write("Title: " + show_title)
        f.write("\n\n")
        f.write("Date: " + show_date)
        f.write("\n\n")
        f.write("Description :" + show_description)
    #4.Lay showmore_cmt
    try:
        browser.find_element(By.CSS_SELECTOR, "#box_comment_vne > div > div.view_more_coment.width_common.mb10 > a").click()
        exist_show_more_cmt = True
    except:
        exist_show_more_cmt = False
    sleep(3)
    while exist_show_more_cmt:
        list1 = browser.find_elements(By.CSS_SELECTOR, "#show_more_coment")
        try:
            list1[-1].click()
        except:
            pass
        sleep(3)

        list2 = browser.find_elements(By.CSS_SELECTOR, "#show_more_coment")
        try:
            list2[-1].click()
        except:
            pass    
        sleep(3)
        if len(list2) == len(list1):
            break
    #Tìm tất cả các author_comment, commemnt và ghi ra màn hình (hoặc file)
    comments = browser.find_elements(By.CLASS_NAME,'full_content')
    content_comments, author_comments = [], []
    for comment in comments:
        author_comment = comment.find_element(By.TAG_NAME, 'b').text
        content_comment = comment.text
        content_comment = content_comment[len(author_comment) + len('\n'):]
        df2 = pd.DataFrame({"Author": [author_comment],
                            "Comment": [content_comment]})
        df1 = pd.concat([df1, df2], axis=0, ignore_index=True)
        
    df1.to_csv("results/" + str(i).zfill(3) + ".csv", index_label="No.")
    i += 1
    sleep(1)
    browser.close()
