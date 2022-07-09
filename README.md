# **Douban Web Scrapyer & Mobile Automation**
## **Why create this app ?** 
Douban is a community website. The site provides a variety of services such as book and video recommendations, offline crosstown activities, and group topic exchanges. In this application, Selenium, BeautifulSoup are used to crawl all information of Douban group.

Douban mobile APP has the feature of generating post’s long diagram. The generated post long diagram has a suitable layout for mobile reading, and contains post’s content, popular comments and QR code for accessing that post.

However, this feature is not available in douban web. So the client automation tool Appium is used for this program. 


## **Module/Library/Frameowrk**
* [os](https://docs.python.org/3/library/os.html)
* [time](https://docs.python.org/3/library/time.html)
* [pandas](https://pandas.pydata.org/docs/user_guide/index.html)       
* [selenium](https://selenium-python.readthedocs.io/)  
* [requests](https://docs.python-requests.org/en/latest/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Appium](https://appium.io/)   
                                                                                                                                    
## **1. DoubanGroupMemberScraper.ipynb**
Scrapying all group member informationi acoording to Douban Group ID
* User's ID
* User's Name
* User's Home Page URL
* User's Location 


## **2. DoubanPostInfosScraper.ipynb**
Scrapying all elite post information (request)
* post's text conetnent (txt)
* post's link（csv txt）
* post's content images / gifs (named by the order in the post)
* post's comment information (commenter‘s ID, text content)


## **3. DoubanScraper-Selenium.ipynb**‘
Scrapying all elite post information (selenium)
* post's text content (txt)
* post's links (txt)
* post's images / gifs (named by the order in the post)
* post's screenshot (pdf)

1. Solve the anti-crawl problem through Selenium
2. Login problem can be resolved by manually 
3. scanning the QR code or find_element_by_class_name().click 
4. There will be no anti-crawl problems once logged in


## **4. Group712168 Folder**
* Demo Result 
* Create a path according to the title of the post, collate the data information

## **5. Copyright**
proxy usded in DoubanPostCollector.ipynb from
> https://www.kuaidaili.com/free/


## **6. Some Important Notes about Environment Setup (MacOS)**
#### 1. Enviroment Setup after downloading Android Studio, JDK
Step1: Enter the following command
> open .bash_profile </br>

Step2: Add following three commands in to bash_profile
> export JAVA_HOME=$(/usr/libexec/java_home)

> export ANDROID_HOME=${HOME}/Library/Android/sdk

> export PATH="${JAVA_HOME}/bin:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools:${PATH}"

#### 2. If uiautomatorviewer is opened and the GUI is incomplete the following problem occurs
> https://github.com/android/android-test/issues/911

> Refer to the above link for the solution, download swt.jar and copy and paste it into the path of uiautomatorviewer   </br>
Notice：The path described in the link above may not be the path to uiautomatorviewer on your own computer，</br>
Just add swt.jar to the x86_64 folder in your own uiautomatorviewer path, then maximize the window, then change the window size to see the phone icon recovered.

> swt.jar Download links for different versions https://download.eclipse.org/eclipse/downloads/index.html </br>
If adding the latest version still doesn't work, change to lower version and repeat the same steps</br>
My system is macOS Monterey 12.2. 4.20 version can run successfully

#### 3. How to find appPackage and appActivity
> adb shell dumpsys window | grep -E 'mCurrentFocus' 

