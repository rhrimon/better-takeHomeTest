import string
import random
import requests
from datetime import datetime
class TestChatPost:
    url = 'http://localhost:8080'
    postUrl = 'http://localhost:8080/api/posts'
    message = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))

    #Check for 
    def test_post_200(self):
        response = requests.get(self.url)
        
        assert response.status_code == 200

    def test_post_400(self):    
        #Send invalid post request to ../api/posts 
        invalidPostRequest = requests.post(self.postUrl, json={
        "invalid1": str(datetime.now()), 
        "invalid2": 'client',
        "invalid3": f"{self.message}",
        "invalid4": str(datetime.now())})

        assert invalidPostRequest.status_code == 400

    def test_post_404(self):
        #Invalid url
        invalidPostUrl = 'http://localhost:8080/api/invalid'
    
        #Send post request to ../api/posts 
        response = requests.post(invalidPostUrl, json={
        "id": str(datetime.now()), 
        "user": 'client',
        "message": f"{self.message}",
        "ts": str(datetime.now())})

        assert response.status_code == 404