from django.test import TestCase
from django.urls import reverse


class AccountsTestCase(TestCase):
    def test_create_limited_liability_company_url(self):
        """Test the URL for creating a limited liability company."""
        url = reverse('establish_company')  # Use the correct name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_nonexistent_company_detail_url(self):
        """Test the URL for a non-existing company's detail view."""
        url = reverse('company_detail', args=[
                      999])  # Use a non-existing company ID
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class SearchTestCase(TestCase):
    def test_company_list_url(self):
        """Test the URL for the company list view."""
        url = reverse('company_list')  # Use the correct name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class MainTestCase(TestCase):
    def test_home_url(self):
        """Test the URL for the home view."""
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
