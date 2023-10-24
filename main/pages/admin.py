from django.contrib import admin
from .models import LimitedLiabilityCompany

class LimitedLiabilityCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'establishment_date', 'total_capital_size', 'registration_code')

admin.site.register(LimitedLiabilityCompany, LimitedLiabilityCompanyAdmin)
