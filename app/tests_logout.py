from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class LogoutTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='logoutuser', password='password123')
        self.token = Token.objects.create(user=self.user)
        self.logout_url = '/auth/token/logout/'

    def test_logout_success(self):
        # Set authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # Post to logout
        response = self.client.post(self.logout_url)
        
        # Check if 204 (Djoser default for logout success) or 200
        # Djoser TokenLogoutView returns 204 NO CONTENT
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify token is deleted
        self.assertFalse(Token.objects.filter(key=self.token.key).exists())
        
        # Verify subsequent request fails
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        res_after = self.client.get('/students/')
        self.assertEqual(res_after.status_code, status.HTTP_401_UNAUTHORIZED)
        
        print("\nLogout test passed: Token successfully invalidated.")

    def test_logout_no_auth(self):
        # Post to logout without header
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print("Logout without auth test passed: Received 401 as expected.")
