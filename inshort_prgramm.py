from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.chrome.options import Options

option = Options()
option.headless = True

url = "https://www.inshorts.com/en/read"
driver = webdriver.Chrome(options=option)
driver.get(url=url)

news_title = []
news_headline = []
news_date = []
news_img = []
news_aurther = []
news_box = driver.find_element(By.CLASS_NAME,"card-stack")
news_card = news_box.find_elements(By.CLASS_NAME,"z-depth-1")

for i in news_card:
    tit  = i.find_element(By.CLASS_NAME,"news-card-title")
    title = tit.find_element(By.CSS_SELECTOR,'span[itemprop="headline"]')
    aru = tit.find_element(By.CSS_SELECTOR,'span[class="author"]')
    dat = tit.find_element(By.CSS_SELECTOR,'span[clas="date"]')
    # print(title.text)
    # print(dat.text)
    # print(aru.text)

    news_title.append(title.text)
    news_aurther.append(aru.text)
    news_date.append(dat.text)
    head = i.find_element(By.CLASS_NAME,'news-card-content')
    heading = head.find_element(By.CSS_SELECTOR,'div[itemprop="articleBody"]')  
    # print(heading.text)
    news_headline.append(heading.text)
    link = i.find_element(By.CSS_SELECTOR,'span[itemprop="image"]')
    li = link.find_element(By.CSS_SELECTOR,'meta[itemprop="url"]')
    image_l = li.get_attribute("content")
    # print(image_l)
    news_img.append(image_l)


    


# print(len(news_title))
# print(news_title[3])
print(len(news_aurther))
print(len(news_date))
print(len(news_headline))
print(len(news_img))
print(len(news_title))
all_data = {}
for i in range(25):

    print(i)
    
    h = news_headline[i]
    s = news_date[i]
    l = news_img[i]
    t = news_title[i]
    a = news_aurther[i]
 
    collection = {"headline": h,"date":s,"image_link":l,"title":t,"aurther":a}
    if i in all_data.keys():
        print("yes")
    else:
        print("nofffffffffffff")
    all_data[f"news{str(i)}"] = collection
    # print(collection)
    # all_data.__setitem__(str(i),collection)

# for i in range[]

# print(all_data["news9"])
import csv
field  = ["headline","date","image_link","title","aurther"]
ne = "inshort.csv"
bas = []
for i in all_data.values():
        bas.append(i)
print(bas[5])
with open(file=ne,mode="w",encoding="utf-8") as fg:
    csvwrite = csv.DictWriter(fg,fieldnames=field)
    csvwrite.writeheader()
    # print(bas)
    csvwrite.writerows(bas)
    # print(len(bas))



time.sleep(10)

