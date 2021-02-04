import requests


def test_users_200():
    url = 'http://localhost:8080/api/users'
    response = requests.get(url)
    
    assert response.status_code == 200

def test_users_404():
    url = 'http://localhost:8080/api/users/id'
    response = requests.get(url)
    
    assert response.status_code == 404