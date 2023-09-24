from django.contrib import admin
from .models import Label, Lead, Activity ,ClientIP ,ActivityName

class LeadAdmin(admin.ModelAdmin):
    list_display = ('source' ,'name', 'mobile', 'occupation')
    search_fields = ['name', 'mobile']

admin.site.register(Label)
admin.site.register(Lead , LeadAdmin)
admin.site.register(Activity)
admin.site.register(ClientIP)
admin.site.register(ActivityName)
