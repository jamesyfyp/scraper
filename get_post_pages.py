from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from utils import wait_for_page_load, to_snake

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
user_urls = []
with open('urls.txt') as file:
    user_urls = file.readlines()

# for user_page in user_urls: <-- make it do all of them
driver.get(user_urls[0])
wait_for_page_load(driver, 10)
#get user name
h1_user_name = driver.find_element(By.XPATH, '//h1[@class="heading text-center"]')
user_name = to_snake(h1_user_name.text)

#getLinksToPosts
post_div = driver.find_element(By.ID, 'entrylist-inner')
post_links = post_div.find_elements("xpath", "//a[@href]")
post_urls = []
for url in post_links:
    url = url.get_attribute("href")
    post_urls.append(url)  


post_url_pattern = '/read/e/'
with open(f'data/user_post_urls/user{user_name}.txt', 'a') as file:
    for url in post_urls: 
        if post_url_pattern in url: 
            file.write(f'{url}\n')