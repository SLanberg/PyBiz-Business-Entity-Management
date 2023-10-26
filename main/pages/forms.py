from django import forms
from .models import LimitedLiabilityCompany, Shareholder
from django.forms import inlineformset_factory


class ShareholderForm(forms.ModelForm):
    class Meta:
        model = Shareholder
        fields = ['natural_person', 'legal_entity', 'share_count', 'is_founder']



ShareholderFormSet = inlineformset_factory(
    LimitedLiabilityCompany,  # Parent model
    Shareholder,              # Child model
    form=ShareholderForm,
    extra=1,                  # Number of empty forms to display
    can_delete = False,
)


class LimitedLiabilityCompanyForm(forms.ModelForm):
    class Meta:
        model = LimitedLiabilityCompany
        fields = ['name', 'registration_code', 'establishment_date', 'total_capital_size']

        widgets = {
            'establishment_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }


class CompanySearchForm(forms.Form):
    q = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Search for companies...'}))

    def clean_q(self):
        q = self.cleaned_data.get('q')
        if not q or q.strip() == "":
            raise forms.ValidationError("Please enter data to search.")
        return q
    
