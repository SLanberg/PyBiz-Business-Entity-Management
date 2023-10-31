from accounts.models import LimitedLiabilityCompany
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
        search_filter |= Q(shareholder__natural_person__first_name__icontains=term) | Q(shareholder__natural_person__last_name__icontains=term) | Q(
            shareholder__legal_entity__name__icontains=term) | Q(shareholder__legal_entity__registration_code__icontains=term)

    # Use the Q object to filter the LimitedLiabilityCompany model and order by a specific field (e.g., name)
    companies = LimitedLiabilityCompany.objects.filter(
        search_filter).distinct().order_by('name')

    # Pagination
    # Get the current page number from the request
    page = request.GET.get('page', 1)
    per_page = 10  # Number of items to display per page
    paginator = Paginator(companies, per_page)

    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, show the first page
        companies = paginator.page(1)
    except EmptyPage:
        # If the page is out of range (e.g., 9999), show the last page
        companies = paginator.page(paginator.num_pages)

    context = {
        'search_query': search_query,
        'companies': companies,
    }

    return render(request, 'pages/company_list.html', context)
