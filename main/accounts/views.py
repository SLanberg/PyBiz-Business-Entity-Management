from django.shortcuts import render
from .models import LimitedLiabilityCompany
from .forms import LimitedLiabilityCompanyForm, ShareholderFormSet
from django.shortcuts import render, redirect


def create_limited_liability_company(request):
    if request.method == 'POST':
        form = LimitedLiabilityCompanyForm(request.POST)
        formset = ShareholderFormSet(request.POST, instance=LimitedLiabilityCompany())

        if form.is_valid() and formset.is_valid():
            # Save the LimitedLiabilityCompany
            limited_liability_company = form.save()

            # Associate each shareholder with the limited liability company
            for shareholder_form in formset:
                shareholder = shareholder_form.save(commit=False)
                if shareholder.natural_person or shareholder.legal_entity:
                    shareholder.company = limited_liability_company
                    shareholder.save()

            return redirect('home')  # Redirect to the company data view

    else:
        form = LimitedLiabilityCompanyForm()
        formset = ShareholderFormSet(instance=LimitedLiabilityCompany())

    return render(request, 'pages/establish.html', {'form': form, 'formset': formset})