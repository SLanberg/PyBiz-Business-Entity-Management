from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import LimitedLiabilityCompany
from .forms import LimitedLiabilityCompanyForm, ShareholderFormSet
from django.shortcuts import render, redirect

from django.db.models import Q


def home(request):
    return render(request, 'home.html')


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


def company_list(request):
    search_query = request.GET.get('q', '')  # Get the search query from the URL

    if not search_query:
        # If the query is empty, set a message to be displayed in the template
        empty_query_message = "Please enter data to search."
        companies = []
    else:
        # Split the search query into words to search across multiple fields
        search_terms = search_query.split()

        # Create a Q object for searching across multiple fields
        search_filter = Q()

        for term in search_terms:
            # Search company name or registration code
            search_filter |= Q(name__icontains=term) | Q(registration_code__icontains=term)

            # Search shareholder name or shareholder code
            # search_filter |= Q(shareholders__name__icontains=term) | Q(shareholders__code__icontains=term)

        # Use the Q object to filter the LimitedLiabilityCompany model
        companies = LimitedLiabilityCompany.objects.filter(search_filter).distinct()

        empty_query_message = None

    context = {
        'search_query': search_query,
        'companies': companies,
        'empty_query_message': empty_query_message,
    }

    return render(request, 'pages/company_list.html', context)