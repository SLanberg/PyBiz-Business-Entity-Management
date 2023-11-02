from django.shortcuts import render, get_object_or_404
from .models import LimitedLiabilityCompany, Shareholder
from .forms import LimitedLiabilityCompanyForm, ShareholderFormSet, CompanyEditForm, ShareholderFormSetEdit
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
            total_capital_size = form.cleaned_data.get('total_capital_size')

            # Calculate the sum of share_count for all shareholders in the formset
            share_count_sum = sum(shareholder_form.cleaned_data.get(
                'share_count', 0) for shareholder_form in formset)

            # Check if the sum is equal to total_capital_size
            if share_count_sum == total_capital_size:
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
                # If the sum is not equal, return an error message or handle it as needed
                form.add_error(
                    'total_capital_size', 'The sum of the share counts must be equal to the total capital size.')

    else:
        form = LimitedLiabilityCompanyForm()
        formset = ShareholderFormSet(instance=LimitedLiabilityCompany())

    return render(request, 'pages/establish_company.html', {'form': form, 'formset': formset})


def edit_company(request, company_id):
    company = get_object_or_404(LimitedLiabilityCompany, pk=company_id)

    if request.method == 'POST':
        form = CompanyEditForm(request.POST, instance=company)

        # Create an instance of ShareholderFormSet with the POST data
        formset = ShareholderFormSetEdit(
            request.POST, instance=company)
        
        if form.is_valid() and formset.is_valid():
            total_capital_size = form.cleaned_data.get('total_capital_size')

            # Calculate the sum of share_count for all shareholders in the formset
            share_count_sum = sum(shareholder_form.cleaned_data.get(
                'share_count', 0) for shareholder_form in formset)
            
            if share_count_sum == total_capital_size:
            
                print(total_capital_size, share_count_sum)

                form.save()

                # Save Shareholder data
                formset.save()

                # Redirect to company data view or any other desired view
                return redirect('company_detail', company_id=company_id)
            else:
                # If the sum is not equal, return an error message or handle it as needed
                form.add_error(
                    'total_capital_size', 'The sum of the share counts must be equal to the total capital size.')
    else:
        form = CompanyEditForm(instance=company)
        formset = ShareholderFormSetEdit(instance=company)  # Change this line

    return render(request, 'pages/edit_company.html', {'form': form, 'formset': formset, 'company': company})

