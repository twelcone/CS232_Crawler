import os
import pickle
import pandas as pd
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidSessionIdException, NoSuchElementException

post_list = []

full_count = int(input("Số cmt mỗi bài viết cần lấy: "))

with open("D:/CS232_Crawler/facebook/posts.csv", "r", newline="\r\n") as f:
    for line in f: post_list.append(line.rstrip())

browser = webdriver.ChromiumEdge(executable_path="D:/CS232_Crawler/msedgedriver.exe")

browser.get("https://mbasic.facebook.com")

cookies = pickle.load(open("my_cookie.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)

##########################################################################################

for post in post_list:
    os.mkdir("D:/CS232_Crawler/facebook/status/" + str(post))

    df1 = pd.DataFrame({"Name": [],
                        "Comment": []})

    browser.get("https://mbasic.facebook.com/" + str(post))
    sleep(2)
    content = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[2]").text
    date = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/abbr").text
    with open("D:/CS232_Crawler/facebook/status/" + str(post) + "/" + str(post) + ".txt", "w+", encoding="utf-8") as f:
        f.write("Nội dung: \n")
        f.write(content)
        f.write("\n\n")
        f.write("Ngày đăng: " + date)

    # sleep(2)
    button_id = "see_next_" + str(post)

    # cmt_list = browser.find_elements(By.CLASS_NAME, "ed")
    # for cmt in cmt_list[0:len(cmt_list) -1]:

    count = 0

    for i in range(1, 11):
        if (count <= full_count) :
            xpath = "/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[5]/div" + "[" + str(i) + "]"
            cmt = browser.find_element(By.XPATH, xpath)

            name_xpath = xpath + "/div/h3/a"
            cmt_xpath = xpath + "/div/div[1]"

            name = cmt.find_element(By.XPATH, name_xpath).text
            cmt_content = cmt.find_element(By.XPATH, cmt_xpath).text

            df2 = pd.DataFrame({"Name": [name],
                                "Comment": [cmt_content]})
            df1 = pd.concat([df1, df2], axis=0, ignore_index=True)
            count +=1

    while (count <= full_count):
        try:
            button = browser.find_element(By.ID, button_id)
            button = button.find_element(By.TAG_NAME, "a")
            button.click()
            sleep(1)

            # cmt_list = browser.find_elements(By.CLASS_NAME, "ed")
            # for cmt in cmt_list[1:len(cmt_list) -1]:
            #     name = cmt.find_element(By.TAG_NAME, "a").text
            #     cmt_content = cmt.find_element(By.CLASS_NAME, "eg").text
            #     df2 = pd.DataFrame({"Name": [name],
            #                         "Comment": [cmt_content]})
            #     df1 = pd.concat([df1, df2], axis=0, ignore_index=True)

            for i in range(2, 12):
                if (count <= full_count):
                    xpath = "/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[5]/div" + "[" + str(i) + "]"
                    cmt = browser.find_element(By.XPATH, xpath)

                    name_xpath = xpath + "/div/h3/a"
                    cmt_xpath = xpath + "/div/div[1]"

                    name = cmt.find_element(By.XPATH, name_xpath).text
                    cmt_content = cmt.find_element(By.XPATH, cmt_xpath).text

                    df2 = pd.DataFrame({"Name": [name],
                                        "Comment": [cmt_content]})
                    df1 = pd.concat([df1, df2], axis=0, ignore_index=True)
                    count += 1
        except:
            sleep(1)
            break
    df1.to_csv("D:/CS232_Crawler/facebook/status/" + str(post) + "/" + str(post) + ".csv", index_label="No.")

browser.close()



