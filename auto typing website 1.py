from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
url = "https://play.typeracer.com/"
import time
driver = webdriver.Chrome()
driver.get(url)
action = ActionChains(driver=driver)
wa = WebDriverWait(driver,20)
driver.implicitly_wait(14)
enter_race = driver.find_element(By.XPATH ,'//*[@id="gwt-uid-1"]/a')
def typing():
    global all_text
    global first
    global all_text_list
    element = wa.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]')))
    first_text = element.text
    try:
        span3 = wa.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]')))
        span2 = wa.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]')))
    except:
        span2 = wa.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]')))
        all_text = span2.text
        print("there is no second span 3 no")
        x = all_text.split()
        all_text_list = x.copy()
        print(x)
        if all_text_list[0] == ",":
            print("yes ,,,,,,,,,,,,,,,,,")

    else:
        t = span2.text
        all_text = span3.text
        first_text = first_text+t
        first = first_text
        x = all_text.split()
        all_text_list = x.copy()        
        print(x)
        if all_text_list[0] == ",":
            print("no ,,,,,,,,,,,,,,,,,")
    finally:
        print(first_text)
        print(all_text)
def taking_time():
    min = " "
    element = wa.until(EC.presence_of_element_located((By.XPATH,'//*[@id="gwt-uid-20"]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/div/div/span')))
    print(element.text)
    actual = element.text
    if actual[0] == ':':
        q = actual[1]
        w = actual[2]
        min = q+w
        print(min)
        int(min)
        return min
    else:    
        m = actual.split(":")
        min =m[0]
        int(min)
        print(type(min))
        return min
enter_race.click()
time_display = wa.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR ,".lightLabel"),'Go!'))
all_text = " "
first = " "
all_text_list = []
ti = None
def run(i):
    element = wa.until(EC.presence_of_element_located((By.CLASS_NAME,'txtInput')))
    element.send_keys(i)
    action.send_keys(Keys.SPACE).perform()
if time_display:
    print("pritam")
    typing()
    print(all_text_list)
    try:
        e = wa.until(EC.presence_of_element_located((By.CLASS_NAME,'txtInput')))
    except:
        print("noo element")
    else:
        e.send_keys(first)
        action.send_keys(Keys.SPACE).perform()
        for i in all_text_list:
            time.sleep(1)
            run(i)
else:
    print("no")
time.sleep(90)