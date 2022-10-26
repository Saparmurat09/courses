from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from coursesapp.models import Course

class CourseTest(APITestCase):
    def test_create_course(self):
        url = reverse('courses')

        data = {
            "name": "Coffee making course",
            "description": "learn how to make a coffee",
            "category": {
                "name": "serving",
                "imgpath": ""
            },
            "logo": "",
            "contacts": {
                "type_of": 1,
                "value": "+996222429866"
            },
            "branches": {
                "latitude": "233143543",
                "longitude": "562345344",
                "address": "Asanbay, 520"
            }
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.get().name, "Coffee making course")