from django import forms


class CompanySearchForm(forms.Form):
    q = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Search for companies...'}))

    def clean_q(self):
        q = self.cleaned_data.get('q')
        if not q or q.strip() == "":
            raise forms.ValidationError("Please enter data to search.")
        return q
    
