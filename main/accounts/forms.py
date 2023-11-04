from django import forms
from .models import LimitedLiabilityCompany, Shareholder
from django.forms import inlineformset_factory


class ShareholderForm(forms.ModelForm):

    class Meta:
        model = Shareholder
        fields = ['natural_person', 'legal_entity', 'share_count',]


class ShareholderFormEdit(forms.ModelForm):
    is_founder = forms.NullBooleanField(initial=False, required=False, widget=forms.HiddenInput)

    class Meta:
        model = Shareholder
        fields = ['natural_person', 'legal_entity', 'share_count', 'is_founder']


ShareholderFormSet = inlineformset_factory(
    LimitedLiabilityCompany,  # Parent model
    Shareholder,              # Child model
    form=ShareholderForm,
    extra=1,                  # Number of empty forms to display
    can_delete=True,
    can_delete_extra=False
)


ShareholderFormSetEdit = inlineformset_factory(
    LimitedLiabilityCompany,  # Parent model
    Shareholder,              # Child model
    form=ShareholderFormEdit,
    extra=0,                  # Number of empty forms to display
    can_delete=True,
    can_delete_extra=False
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
        fields = ['name', 'registration_code',
                  'establishment_date', 'total_capital_size']

    # Define the Shareholder formset as an attribute of the CompanyEditForm
    shareholders = ShareholderFormSetEdit(queryset=Shareholder.objects.none())

    def __init__(self, *args, **kwargs):
        super(CompanyEditForm, self).__init__(*args, **kwargs)

        # Check if there are instance data and update the Shareholder formset accordingly
        if 'instance' in kwargs and kwargs['instance'] is not None:
            self.shareholders = ShareholderFormSetEdit(instance=kwargs['instance'])
