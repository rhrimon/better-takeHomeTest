import requests

def test_users_200():
    url = 'http://localhost:8080/api/users'
    response = requests.get(url)
    
    assert response.status_code == 200