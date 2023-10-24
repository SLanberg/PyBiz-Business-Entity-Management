from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import LimitedLiabilityCompany
from .forms import LimitedLiabilityCompanyForm

def home(request):
    return render(request, 'home.html')

class CompanyCreateView(CreateView):
    model = LimitedLiabilityCompany
    form_class = LimitedLiabilityCompanyForm
    template_name = 'pages/establish.html'  # Create this HTML template for rendering the form
    success_url = '#'  # Redirect to a view for displaying company data


def company_list(request):
    search_query = request.GET.get('q', '')  # Get the search query from the URL

    # Implement your search logic here using the search_query
    # For example, you can filter the Company model based on the search_query
    companies = LimitedLiabilityCompany.objects.filter(name__icontains=search_query)

    context = {
        'search_query': search_query,
        'companies': companies,
    }

    return render(request, 'pages/company_list.html', context)