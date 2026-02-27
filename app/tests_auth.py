from rest_framework.test import APIClient, APITestCase
from rest_framework import status

class DjoserAuthTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/auth/users/'  # Djoser default name for registration
        self.login_url = '/auth/token/login/'   # Djoser token login endpoint
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'TestPass123',
            're_password': 'TestPass123'
        }

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Ensure user is created
        self.assertIn('id', response.data)
        self.assertEqual(response.data['username'], self.user_data['username'])

    def test_token_login(self):
        # First register the user
        self.client.post(self.register_url, self.user_data, format='json')
        login_data = {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        }
        response = self.client.post(self.login_url, login_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', response.data)
