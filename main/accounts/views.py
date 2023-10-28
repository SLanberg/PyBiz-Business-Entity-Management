from django.shortcuts import render, get_object_or_404
from .models import LimitedLiabilityCompany, Shareholder
from .forms import LimitedLiabilityCompanyForm, ShareholderFormSet, CompanyEditForm
from django.shortcuts import render, redirect


def company_detail(request, company_id):
    company = get_object_or_404(LimitedLiabilityCompany, pk=company_id)
    shareholders = Shareholder.objects.filter(company=company)

    return render(request, 'pages/company_detail.html', {'company': company, 'shareholders': shareholders})


def create_limited_liability_company(request):
    if request.method == 'POST':
        form = LimitedLiabilityCompanyForm(request.POST)
        formset = ShareholderFormSet(
            request.POST, instance=LimitedLiabilityCompany())

        if form.is_valid() and formset.is_valid():
            # Save the LimitedLiabilityCompany
            limited_liability_company = form.save()

            # Associate each shareholder with the limited liability company
            for shareholder_form in formset:
                shareholder = shareholder_form.save(commit=False)
                if shareholder.natural_person or shareholder.legal_entity:
                    shareholder.company = limited_liability_company
                    shareholder.save()

            return redirect('company_detail', company_id=limited_liability_company.id)

    else:
        form = LimitedLiabilityCompanyForm()
        formset = ShareholderFormSet(instance=LimitedLiabilityCompany())

    return render(request, 'pages/establish_company.html', {'form': form, 'formset': formset})


def edit_company(request, company_id):
    company = get_object_or_404(LimitedLiabilityCompany, pk=company_id)

    if request.method == 'POST':
        form = CompanyEditForm(request.POST, instance=company)

        # Create an instance of ShareholderFormSet with the POST data
        shareholder_formset = ShareholderFormSet(request.POST, instance=company)

        if form.is_valid() and shareholder_formset.is_valid():
            form.save()

            # Save Shareholder data
            shareholder_formset.save()

            # Redirect to company data view or any other desired view
            return redirect('company_detail', company_id=company_id)
    else:
        form = CompanyEditForm(instance=company)
        shareholder_formset = ShareholderFormSet(instance=company)

    return render(request, 'pages/increase_capital.html', {'form': form, 'shareholder_formset': shareholder_formset, 'company': company})

