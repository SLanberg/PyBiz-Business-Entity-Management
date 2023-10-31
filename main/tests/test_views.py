from django.test import TestCase
from django.urls import reverse
from accounts.models import LimitedLiabilityCompany


class CompanyListViewTestCase(TestCase):
    def setUp(self):
        # Create test data for LimitedLiabilityCompany model
        self.company1 = LimitedLiabilityCompany.objects.create(
            name="Fox",
            registration_code="12345678901",
            total_capital_size=5000.00,
            establishment_date="2023-10-31",
        )
        self.company2 = LimitedLiabilityCompany.objects.create(
            name="Cat",
            registration_code="12345678902",
            total_capital_size=5000.00,
            establishment_date="2023-10-31",
        )

    def test_company_list_view_with_search_results(self):
        # Perform a GET request to the company_list view with a search query
        response = self.client.get(reverse('company_list'), {'q': 'Fox'})

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the search result
        self.assertContains(response, 'Fox')
        self.assertNotContains(response, 'Cat')

    def test_company_list_view_pagination(self):
        # Perform a GET request to the company_list view
        response = self.client.get(reverse('company_list'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the view paginates the results correctly
        self.assertEqual(len(response.context['companies']), 2)  # Assuming per_page is set to 10

    def test_company_list_view_no_search_results(self):
        # Perform a GET request to the company_list view with a search query that should return no results
        response = self.client.get(reverse('company_list'), {'q': 'Non-Existent Company'})

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the view displays a message for no search results
        self.assertContains(response, 'Not found...')

    def test_company_list_view_no_search_query(self):
        # Perform a GET request to the company_list view without a search query
        response = self.client.get(reverse('company_list'))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the view displays all companies (no filtering)
