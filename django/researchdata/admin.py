from django.contrib import admin
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Material Identities, Social Bodies: Admin Dashboard'


class LetterAdminView(admin.ModelAdmin):
    """
    Customise the Letter section of the Django admin
    """
    list_display = ('id', 'title', 'summary')
    list_filter = ('collection',)
    search_fields = ('title', 'summary')
    ordering = ('-id',)


class PersonAdminView(admin.ModelAdmin):
    """
    Customise the Person section of the Django admin
    """
    list_display = ('id', 'title', 'first_name', 'middle_name', 'last_name', 'informal_name', 'gender', 'religion')
    list_filter = ('title', 'religion', 'gender')
    search_fields = ('first_name', 'middle_name', 'last_name', 'informal_name')
    ordering = ('-id',)


# Register classes
admin.site.register(models.Letter, LetterAdminView)
admin.site.register(models.Person, PersonAdminView)
