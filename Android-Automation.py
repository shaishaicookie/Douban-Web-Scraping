import time 
import pandas       
from bs4 import BeautifulSoup     
from selenium import webdriver                                                                                                                                                  

from appium import webdriver as appiumWebdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey


# 爬取一个豆瓣小组所有精华帖
driver = webdriver.Chrome()
loginURL = "https://accounts.douban.com/passport/login"
driver.get(loginURL)
time.sleep(5)
# 如果爬取次数过度，这里手动扫描二维码登录豆瓣

def findElitePostPageNumber(groupID):
    startURL = "https://www.douban.com/group/" + str(groupID) + "/discussion?start=0&type=elite"
    driver.get(startURL)
    html = driver.page_source
    soup = BeautifulSoup(html, features='lxml')
    pageNumber = int(soup.find("span", {"class":"thispage"}).attrs["data-total-page"])
    return pageNumber

def findElitePostURLs(groupID):
    ElitePostURLs = []
    baseURL = "https://www.douban.com/group/" + str(groupID) + "/discussion?start="
    pageNumber = findElitePostPageNumber(groupID)
    for page in range(0, pageNumber*25, 25):
        currentPageURL = baseURL + str(page) + "&type=elite"
        driver.get(currentPageURL)
        html = driver.page_source
        soup = BeautifulSoup(html, features='lxml')
        all = soup.find_all("td", {"class":"title"})
        for item in all:
            postInfo = {}
            # find post url
            elitePostURL = item.find("a").attrs["href"]
            postInfo["postURL"] = elitePostURL
            # find post title                                 
            postInfo["postTitle"] = item.find("a").attrs["title"]

            ElitePostURLs.append(postInfo)
            
    df = pandas.DataFrame(ElitePostURLs)
    df = df.drop_duplicates("postURL")
    df = df.reset_index(drop=True)
    return df


def postImageGenerator(postTitle):
    # open Douban App
    driver = appiumWebdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # Skip advs time
    time.sleep(6) 

    # find search bar
    driver.find_element_by_id('search_hint').click()
    searchBox = driver.find_element_by_id('search')

    #  post title & search
    searchBox.send_keys(postTitle)
    driver.press_keycode(AndroidKey.ENTER)
    driver.find_element_by_id('text').click()
    driver.find_element_by_xpath('//android.widget.TextView[@text="小组"]').click()

    # to certain post
    driver.find_element_by_id('title').click()

    # click share buttion
    driver.find_element_by_id('ic_share').click()

    # click generating poster [the feature only available in mobile app]
    driver.find_element_by_xpath('//android.widget.TextView[@text="生成海报"]').click()

    # time to generate poster
    time.sleep(5)

    # save picture 
    driver.find_element_by_id('to_save').click()
    time.sleep(2)
    
    driver.quit()


def doubanGroupPostLongImage(groupID):
     elitePostInfos = findElitePostURLs(groupID)
     for i in range(len(elitePostInfos)):
         postTitle = elitePostInfos["postTitle"][i]
         postImageGenerator(postTitle)