from selenium import webdriver
import os
import urllib.request

def download(urldown,maxnum,startnum,dirss):
    i = startnum
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')]
    urllib.request.install_opener(opener)
    while i<=maxnum:
        try:
            driver.get(urldown)
            ttitle = driver.find_element_by_xpath('').text
            titlerp = ttitle.replace("\\"," ").replace("/"," ").replace(":"," ").replace("|"," ").replace("*"," ").replace('\"'," ").replace("<"," ").replace(">"," ").replace("?"," ")
            print(titlerp)
            dir_download = dirss + "\\" + titlerp + "\\"
            if not (os.path.isdir(dir_download)):
                os.mkdir(dir_download)
            imgurls = driver.find_elements_by_class_name("클래스 이름")
            print("총 이미지 갯수 : "+str(len(imgurls)))
            for idx,imgurl in enumerate(imgurls):
                urllib.request.urlretrieve(imgurl.get_attribute("src"),dir_download+"다운받을 아이템 형식"+".jpg")
            driver.implicitly_wait(10)
            i+=1
        except:
            print("에러발생")
            i+=1


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument("lang=ko_KR")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
#크롬드라이버 셋팅

site_id = input("아이디 : ")
site_pwd = input("비밀번호 : ")
site_maxnum = int(input("가장 최근의 숫자 : "))
site_startnum = int(input("다운 시작할 숫자 : "))

down_url = "?" #다운 받을 url

dir_path = os.getcwd()

dir_driver=dir_path +'\chromedriver.exe'

driver = webdriver.Chrome(dir_driver,chrome_options=options)

driver.get("") #크롤링할  URL

driver.implicitly_wait(10) #다운시 시작할 시간 지연

download(down_url,site_maxnum,site_startnum,dir_path)

    

