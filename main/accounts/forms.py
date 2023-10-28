from django import forms
from .models import LimitedLiabilityCompany, Shareholder, NaturalPerson
from django.forms import inlineformset_factory


class ShareholderForm(forms.ModelForm):
    class Meta:
        model = Shareholder
        fields = ['natural_person', 'legal_entity', 'share_count',]


ShareholderFormSet = inlineformset_factory(
    LimitedLiabilityCompany,  # Parent model
    Shareholder,              # Child model
    form=ShareholderForm,
    extra=1,                  # Number of empty forms to display
    can_delete=False,
)


class LimitedLiabilityCompanyForm(forms.ModelForm):
    class Meta:
        model = LimitedLiabilityCompany
        fields = ['name', 'registration_code',
                  'establishment_date', 'total_capital_size']

        widgets = {
            'establishment_date': forms.widgets.DateInput(attrs={'type': 'date'}, )
        }


class CompanyEditForm(forms.ModelForm):
    class Meta:
        model = LimitedLiabilityCompany
        fields = ['name', 'registration_code', 'establishment_date', 'total_capital_size']

    # Define the Shareholder formset as an attribute of the CompanyEditForm
    shareholders = ShareholderFormSet(queryset=Shareholder.objects.none())

    def __init__(self, *args, **kwargs):
        super(CompanyEditForm, self).__init__(*args, **kwargs)

        # Check if there are instance data and update the Shareholder formset accordingly
        if 'instance' in kwargs and kwargs['instance'] is not None:
            self.shareholders = ShareholderFormSet(instance=kwargs['instance'])

    # You can add additional form field customizations if needed

    def save(self, *args, **kwargs):
        # Save the LimitedLiabilityCompany instance
        company = super().save(*args, **kwargs)

        # Save the Shareholder formset if it's valid
        if self.shareholders.is_valid():
            self.shareholders.instance = company  # Set the instance for the formset
            self.shareholders.save()

        return company
