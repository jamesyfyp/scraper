from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from utils import wait_for_page_load, convert_to_epoch_time
import os

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

directory_path = 'data/user_post_urls'

user_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

post_urls = []
for user_post_links in user_list:
    with open(f'{directory_path}/{user_post_links}') as file:
        post_urls = file.readlines()

for post_page in post_urls:
    driver.get(post_page)
    post_div = driver.find_element(By.ID, 'mainentrydiv')
    post_date_outer = post_div.find_element(By.CLASS_NAME, "col")
    post_date = convert_to_epoch_time(post_date_outer.find_element(By.TAG_NAME, "div").text)
    post_title = post_div.find_element(By.TAG_NAME, "h3").text
    post =  post_div.find_element(By.TAG_NAME, "p").text

    #send data to db   
