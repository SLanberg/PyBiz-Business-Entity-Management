from django import forms
from .models import LimitedLiabilityCompany

class LimitedLiabilityCompanyForm(forms.ModelForm):
    class Meta:
        model = LimitedLiabilityCompany
        fields = ['name', 'registration_code', 'establishment_date', 'total_capital_size']

        widgets = {
            'establishment_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

