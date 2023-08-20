import requests

# Base URL of the API
base_url = 'http://localhost:5000'  # Replace with the actual URL where your API is running

# Test data
user_data = {
    "username": "optimalxai user1",
    "email": "optimalxaiuser1@example.com"
}

# Test the create_user endpoint
def test_create_user():
    endpoint = '/user'
    url = base_url + endpoint

    response = requests.post(url, json=user_data)
    print(response.json())
    # Check if the response status code is 201 (Created)
    assert response.status_code == 201
    
    # Check if the response data matches the test data
    assert response.json() == user_data
    
    print(f"Test for {endpoint} passed!")

if __name__ == '__main__':
    test_create_user()
