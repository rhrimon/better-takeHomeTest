import time
import string
import random
import requests
from selenium import webdriver
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class TestChatPost:
    url = 'http://localhost:8080'
    postUrl = 'http://localhost:8080/api/posts'
    message = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

    def test_message_200(self):
        #use selenium to open app and send message
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(self.url)
        time.sleep(1)
        driver.find_element_by_id('chatInput').send_keys(self.message)
        time.sleep(1)
        driver.find_element_by_id('chatSubmit').click()
        time.sleep(3)
        driver.close()
    
        #send post request to ../api/posts 
        response = requests.post(self.postUrl, json={
        "id": str(datetime.now()), 
        "user": 'client',
        "message": f'{self.message}',
        "ts": str(datetime.now())})

        #verify that response received is valid and matches message passed
        response_message = response.json()
        assert response.status_code == 200
        assert response_message['received']['message'] == self.message

    def test_message_more_than_140_chars(self):
        response = requests.post(self.postUrl, json={
        "id": str(datetime.now()), 
        "user": 'client',
        "message": str(('a' * 145)),
        "ts": str(datetime.now())})

        #verify that response received is valid and matches message passed
        assert response.status_code == 400