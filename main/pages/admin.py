from django.contrib import admin
from .models import LimitedLiabilityCompany, NaturalPerson, LegalEntity, Shareholder


class LimitedLiabilityCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'establishment_date', 'total_capital_size', 'registration_code')


class NaturalPersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id_code')


class LegalEntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_code')



admin.site.register(LimitedLiabilityCompany, LimitedLiabilityCompanyAdmin)
admin.site.register(NaturalPerson, NaturalPersonAdmin)
admin.site.register(LegalEntity, LegalEntityAdmin)
