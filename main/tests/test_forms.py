from django.test import TestCase
from accounts.models import LimitedLiabilityCompany, Shareholder
from accounts.forms import ShareholderForm, ShareholderFormEdit, LimitedLiabilityCompanyForm, CompanyEditForm


class FormTests(TestCase):
    def test_LimitedLiabilityCompanyForm_valid(self):
        # Create data for LimitedLiabilityCompanyForm
        data = {
            'name': 'Company Inc.',
            'registration_code': '1234567',
            'establishment_date': '2022-01-01',
            'total_capital_size': 100000,
        }

        form = LimitedLiabilityCompanyForm(data=data)
        self.assertTrue(form.is_valid())

    def test_LimitedLiabilityCompanyForm_registration_code_invalid(self):
        # Create invalid data for LimitedLiabilityCompanyForm
        data = {
            'name': 'Feel Good Inc.',
            'registration_code': '123456',
            'establishment_date': '2022-01-01',
            'total_capital_size': 100000,
        }

        form = LimitedLiabilityCompanyForm(data=data)
        self.assertFalse(form.is_valid())

    def test_LimitedLiabilityCompanyForm_establishment_date_invalid(self):
        # Create invalid data for LimitedLiabilityCompanyForm
        data = {
            'name': 'Feel Good Inc.',
            'registration_code': '1234567',
            'establishment_date': '2100-01-01',
            'total_capital_size': 100000,
        }

        form = LimitedLiabilityCompanyForm(data=data)
        self.assertFalse(form.is_valid())

    def test_LimitedLiabilityCompanyForm_capital_invalid(self):
        # Create invalid data for LimitedLiabilityCompanyForm
        data = {
            'name': 'Feel Good Inc.',
            'registration_code': '1234567',
            'establishment_date': '2000-01-01',
            'total_capital_size': 100,
        }

        form = LimitedLiabilityCompanyForm(data=data)
        self.assertFalse(form.is_valid())

    def test_LimitedLiabilityCompanyForm_name_invalid(self):
        # Create invalid data for LimitedLiabilityCompanyForm
        data = {
            'name': '',
            'registration_code': '1234567',
            'establishment_date': '2000-01-01',
            'total_capital_size': 100000,
        }

        form = LimitedLiabilityCompanyForm(data=data)
        self.assertFalse(form.is_valid())

    def test_CompanyEditForm_valid(self):
        # Create data for CompanyEditForm
        data = {
            'name': 'Company Inc.',
            'registration_code': '1234567',
            'establishment_date': '2022-01-01',
            'total_capital_size': 100000,
        }

        form = CompanyEditForm(data=data)
        self.assertTrue(form.is_valid())

    def test_CompanyEditForm_invalid(self):
        # Create invalid data for CompanyEditForm
        data = {
            'name': '',  # This field is required
            'registration_code': '1234567',
            'establishment_date': 'invalid_date',  # Invalid date format
            'total_capital_size': -100000,  # Total capital size should be positive
        }

        form = CompanyEditForm(data=data)
        self.assertFalse(form.is_valid())
