from accounts.models import LimitedLiabilityCompany
from django.shortcuts import render
from django.db.models import Q


def company_list(request):
    # Get the search query from the URL
    search_query = request.GET.get('q', '')

    # Split the search query into words to search across multiple fields
    search_terms = search_query.split()

    # Create a Q object for searching across multiple fields
    search_filter = Q()

    for term in search_terms:
        # Search company name or registration code
        search_filter |= Q(name__icontains=term) | Q(
            registration_code__icontains=term)

        # Search shareholder name or shareholder code
        # search_filter |= Q(shareholders__name__icontains=term) | Q(shareholders__code__icontains=term)

    # Use the Q object to filter the LimitedLiabilityCompany model
    companies = LimitedLiabilityCompany.objects.filter(
        search_filter).distinct()

    context = {
        'search_query': search_query,
        'companies': companies,
    }

    return render(request, 'pages/company_list.html', context)
