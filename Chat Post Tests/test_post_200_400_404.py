import requests
from datetime import datetime

def test_post_200():
    url = 'http://localhost:8080/api/posts'
    response = requests.get(url)
    
    assert response.status_code == 200

def test_post_400():
    posts_url = 'http://localhost:8080/api/posts'
    message = 'Hello World'
 
    #send invalid post request to ../api/posts 
    invalidPostRequest = requests.post(posts_url, json={
    "invalid1": str(datetime.now()), 
    "invalid2": 'client',
    "invalid3": f"{message}",
    "invalid4": str(datetime.now())})

    assert invalidPostRequest.status_code == 400

def test_post_404():
    #invalid url
    posts_url = 'http://localhost:8080/api/invalid'
    message = 'Hello World'
 
    #send post request to ../api/posts 
    response = requests.post(posts_url, json={
    "id": str(datetime.now()), 
    "user": 'client',
    "message": f"{message}",
    "ts": str(datetime.now())})

    assert response.status_code == 404