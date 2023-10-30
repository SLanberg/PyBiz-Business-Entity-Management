from django.contrib import admin
from .models import LimitedLiabilityCompany, NaturalPerson, LegalEntity, Shareholder


class LimitedLiabilityCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'establishment_date',
                    'total_capital_size', 'registration_code')


class NaturalPersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id_code')


class LegalEntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_code')


class ShareholderAdmin(admin.ModelAdmin):
    list_display = ('natural_person', 'display_company_info',
                    'legal_entity', 'share_count', 'is_founder')

    def display_company_info(self, obj):
        return obj.company.name 
    
    display_company_info.short_description = 'Company Info'


admin.site.register(LimitedLiabilityCompany, LimitedLiabilityCompanyAdmin)
admin.site.register(NaturalPerson, NaturalPersonAdmin)
admin.site.register(LegalEntity, LegalEntityAdmin)
admin.site.register(Shareholder, ShareholderAdmin)
