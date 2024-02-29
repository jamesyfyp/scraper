from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
from utils import wait_for_page_load, convert_to_epoch_time



options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

directory_path = 'data/user_post_urls'

user_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
user_id_url = "http://localhost:5000/users/get_by_name"

for user_post_links in user_list:
    username = user_post_links.replace("user", "").replace(".txt", "")
    request_data = {
        'name': username
    }
    response = requests.post(user_id_url, json=request_data)
    if response.status_code == 200:
        print("POST request was successful!")
        print("Response:", response.text)
    else:
        print("POST request failed with status code:", response.status_code)
    name_data = response.json()
    user_id = name_data["id"] 

    post_urls = []
    with open(f'{directory_path}/{user_post_links}') as file:
        post_urls = file.readlines()

    for post_page in post_urls:
        driver.get(post_page)
        wait_for_page_load(driver, 10)
        post_div = driver.find_element(By.ID, 'mainentrydiv')
        post_title = post_div.find_element(By.TAG_NAME, "h3").text
        post =  post_div.find_element(By.TAG_NAME, "p").text
        post_req_url = "http://localhost:5000/posts"
        post_data = {
            "user_id": user_id, 
            "title": post_title,
            "content": post 
        }    

        new_post = requests.post(post_req_url, json=post_data)
