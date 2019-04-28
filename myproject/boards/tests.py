from django.test import TestCase

# Create your tests here.
from .views import home
from django.urls import resolve
from django.urls import reverse
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


