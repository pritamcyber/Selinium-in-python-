from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.action_chains import ActionChains 

# for wait for an element to occure in page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get("https://play.typeracer.com/")
driver.implicitly_wait(10)
action = ActionChains(driver) 
 


# /div/div/table/tbody/tr/td/table/tbody/tr/td[2]/div

# /html/body/div[4]/div/table/tbody/tr/td/table/tbody/tr/td[2]
# /html/body/div[4]/div/table/tbody/tr/td/table/tbody/tr/td[3]/div/span
try:
    enter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="gwt-uid-1"]/a[1]'))
    )
except:
    print('error')

finally:
    print(enter.text)
    enter.click()
    
# /div/div/table/tbody/tr/td/table/tbody/tr/td[2]/div
try:
    textt = WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, 'lightLabel'),'Go!')
    )
    print('done')
    span1 =  WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]'))
    )
    print('done')
    
    span2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]'))
    )
    print('done')
    
    print(span1.text+span2.text)
    
    span3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]'))
    )
    list_of_text = []
    alfa = span3.text
    list_of_text  = alfa.split()
    list_of_text.insert(0,span1.text+span2.text)
    print(list_of_text)
    
    input_things = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input'))
    )
    
    clicked = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a'))
    )
    for i in list_of_text:
        time.sleep(0.8)
        input_things.send_keys(i)
        action.send_keys(Keys.SPACE).perform()
        
    
except:
    print('error')

finally:
    
    print('ok done text founded')
    
# //*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]
# //*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1] first div
# second div
# //*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]
# //*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]
# //*[@id="gwt-uid-20"]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a

# //*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]
# //*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[4]
# //*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]
# txtInput//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input
time.sleep(10)
driver.close()