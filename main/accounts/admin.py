from django.contrib import admin
from .models import LimitedLiabilityCompany, NaturalPerson, LegalEntity, Shareholder


class ShareholderInline(admin.TabularInline):
    model = Shareholder
    extra = 0


class LimitedLiabilityCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'establishment_date',
                    'total_capital_size', 'registration_code')
    inlines = [ShareholderInline]


class NaturalPersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id_code', 'related_companies')

    def related_companies(self, obj):
        return "\n".join([share.company.name for share in Shareholder.objects.filter(natural_person=obj)])

    related_companies.short_description = "Related Companies"

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'id_code'),
        }),
        ('Related Companies', {
            'fields': ('related_companies',),
        }),
    )

    readonly_fields = ('related_companies',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('related_companies',) + self.readonly_fields
        return self.readonly_fields


class LegalEntityAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_code', 'related_companies')

    def related_companies(self, obj):
        return "\n".join([share.company.name for share in Shareholder.objects.filter(legal_entity=obj)])

    related_companies.short_description = "Related Companies"

    fieldsets = (
        (None, {
            'fields': ('name', 'registration_code'),
        }),
        ('Related Companies', {
            'fields': ('related_companies',),
        }),
    )

    readonly_fields = ('related_companies',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('related_companies',) + self.readonly_fields
        return self.readonly_fields


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
