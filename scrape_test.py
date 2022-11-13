from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait as web_wait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome( service=Service(ChromeDriverManager().install()))
driver.get('https://perfumancebd.com/product-category/perfume/refreshing/')
src=[]
for i in range(1, 12):
    x_path = '//*[@id="rig-adpr"]/div['+str(i)+']/p[1]'
    x2_path = '//*[@id="rig-adpr"]/div[' + str(i) + ']/p[2]'
    value = '//*[@id="rig-adpr"]/div['+str(i)+']/a/img'
    title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, x_path)))
    price = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, x2_path)))
    image = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, value)))

    src.append(title.text)
    src.append(price.text)
    src.append(image.get_attribute('src'))



print(src)
time.sleep(50)
driver.quit()