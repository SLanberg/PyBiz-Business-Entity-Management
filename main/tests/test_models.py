from django.test import TestCase
from accounts.models import NaturalPerson, LegalEntity, LimitedLiabilityCompany, Shareholder

class NaturalPersonTestCase(TestCase):
    def test_natural_person_creation(self):
        natural_person = NaturalPerson.objects.create(
            first_name="John",
            last_name="Doe",
            id_code="12345678901"
        )

        self.assertEqual(natural_person.first_name, "John")
        self.assertEqual(natural_person.last_name, "Doe")
        self.assertEqual(natural_person.id_code, "12345678901")

class LegalEntityTestCase(TestCase):
    def test_legal_entity_creation(self):
        legal_entity = LegalEntity.objects.create(
            name="Example Corp",
            registration_code="ABC12345678"
        )

        self.assertEqual(legal_entity.name, "Example Corp")
        self.assertEqual(legal_entity.registration_code, "ABC12345678")

class LimitedLiabilityCompanyTestCase(TestCase):
    def test_company_creation(self):
        company = LimitedLiabilityCompany.objects.create(
            name="Company XYZ",
            registration_code="XYZ123",
            establishment_date="2023-10-27",
            total_capital_size=100000
        )

        self.assertEqual(company.name, "Company XYZ")
        self.assertEqual(company.registration_code, "XYZ123")
        self.assertEqual(str(company.establishment_date), "2023-10-27")
        self.assertEqual(company.total_capital_size, 100000)

class ShareholderTestCase(TestCase):
    def test_shareholder_creation(self):
        natural_person = NaturalPerson.objects.create(
            first_name="Alice",
            last_name="Johnson",
            id_code="98765432109"
        )

        company = LimitedLiabilityCompany.objects.create(
            name="Test LLC",
            registration_code="ABCDEF1",
            establishment_date="2023-10-27",
            total_capital_size=50000
        )

        shareholder = Shareholder.objects.create(
            natural_person=natural_person,
            company=company,
            share_count=100
        )

        self.assertEqual(shareholder.natural_person.first_name, "Alice")
        self.assertEqual(shareholder.company.name, "Test LLC")
        self.assertEqual(shareholder.share_count, 100)
