from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Course, YearLevel, Student

class SequentialAuthTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/auth/users/'
        self.login_url = '/auth/token/login/'
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'TestPass123',
            're_password': 'TestPass123'
        }
        # Create some data
        self.course = Course.objects.create(coursename="Test Course", units=3)
        self.yearlevel = YearLevel.objects.create(yearlevel="1st Year")
        Student.objects.create(studentname="Test Student", age=20, course=self.course, yearlevel=self.yearlevel)

    def test_sequential_requests(self):
        # 1. Register and Login
        self.client.post(self.register_url, self.user_data, format='json')
        login_data = {'username': 'testuser', 'password': 'TestPass123'}
        response = self.client.post(self.login_url, login_data, format='json')
        token = response.data['auth_token']
        
        # Set the token for subsequent requests
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        
        # 2. Hit Students
        print("\nTesting Students...")
        res_stu = self.client.get('/students/')
        self.assertEqual(res_stu.status_code, status.HTTP_200_OK)
        
        # 3. Hit Courses
        print("Testing Courses...")
        res_crs = self.client.get('/courses/')
        self.assertEqual(res_crs.status_code, status.HTTP_200_OK)
        
        # 4. Hit YearLevels
        print("Testing YearLevels...")
        res_yl = self.client.get('/yearlevels/')
        self.assertEqual(res_yl.status_code, status.HTTP_200_OK)
        
        print("All sequential requests passed!")
