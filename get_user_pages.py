import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from utils import wait_for_page_load

site = 

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.my-diary.org/surf/")
driver.maximize_window
#click classname  & btn btn-diary
button_adult_content = driver.find_element(By.CLASS_NAME, 'custom-control-label')
button_adult_content.click()
wait_for_page_load(driver, 10)
#find dropdown select max
dropdown_element = driver.find_element(By.ID, 'maxhits')
select = Select(dropdown_element)
select.select_by_visible_text("100")
#click search
button_search = driver.find_element(By.CLASS_NAME, 'btn-diary')
button_search.click()
wait_for_page_load(driver, 10)

links = driver.find_elements("xpath", "//a[@href]")
user_urls = []
user_url_pattern = '/read/d'
for link in links:
    url = link.get_attribute("href")
    if user_url_pattern in url:
        user_urls.append(url)  



with open('urls.txt', 'a') as file:
    for url in user_urls: 
        file.write(f'{url}\n')
