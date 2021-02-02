import time
import requests
from selenium import webdriver
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def test_post_200():
    url = 'http://localhost:8080'
    posts_url = 'http://localhost:8080/api/posts'
    message = 'Hello World'

    #use selenium to open app and send message
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_id('chatInput').send_keys(message)
    time.sleep(1)
    driver.find_element_by_id('chatSubmit').click()
    time.sleep(3)
 
    #send post request to ../api/posts 
    response = requests.post(posts_url, json={
    "id": str(datetime.now()), 
    "user": 'client',
    "message": f"{message}",
    "ts": str(datetime.now())})

    #verify that response received matches message passed
    response_message = response.json()
    print(response_message)
    assert response_message['received']['message'] == message

    driver.close()