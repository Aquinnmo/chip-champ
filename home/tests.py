from django.test import TestCase
from django.urls import reverse
from .models import Page

class HomeViewTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get(reverse('home:about'))
        self.assertEqual(response.status_code, 200)

class PageModelTests(TestCase):
    def test_page_creation(self):
        page = Page.objects.create(
            title="Test Page",
            slug="test-page",
            content="This is a test page."
        )
        self.assertEqual(str(page), "Test Page")
        self.assertTrue(page.is_active)
