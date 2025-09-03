from django.contrib import admin

# Register your models here.
from .models import Employee,Contact

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'facebook', 'twitter', 'linkedin', 'instagram')
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Contact)