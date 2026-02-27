import requests

BASE_URL = "http://127.0.0.1:8000/"
USERNAME = "dev"
# Note: In a real scenario, we'd need the password. 
# For verification, I'll attempt to get a token or check if one exists in the DB.

def test_endpoint(endpoint, token=None):
    headers = {}
    if token:
        headers["Authorization"] = f"Token {token}"
    
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
        print(f"GET {endpoint} (Token: {'Yes' if token else 'No'}): {response.status_code}")
        if response.status_code == 200:
            print("  Success!")
        else:
            print(f"  Failed: {response.text[:100]}")
    except Exception as e:
        print(f"Error connecting to {endpoint}: {e}")

if __name__ == "__main__":
    # This script assumes the server is running.
    # Since I don't have the user's password, I'll rely on the manual check or
    # try to use a dummy token to see if it rejects with 401 (expected) vs 403 or other.
    # Actually, the best way is to ask the user to verify since I don't have their credentials.
    print("Testing endpoints...")
    test_endpoint("students/")
    test_endpoint("courses/")
    test_endpoint("yearlevels/")
