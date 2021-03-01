from django.contrib import admin
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Material Identities, Social Bodies: Admin Dashboard'


class SlGenericAdminView(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')
    ordering = ('id',)


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
# SL models
admin.site.register(models.SlPersonGender, SlGenericAdminView)
admin.site.register(models.SlPersonRank, SlGenericAdminView)
admin.site.register(models.SlPersonReligion, SlGenericAdminView)
admin.site.register(models.SlPersonTitle, SlGenericAdminView)
admin.site.register(models.SlLetterCollection, SlGenericAdminView)
admin.site.register(models.SlLetterContentSubject, SlGenericAdminView)
admin.site.register(models.SlLetterContentBodyPart, SlGenericAdminView)
admin.site.register(models.SlLetterContentBodilyActivity, SlGenericAdminView)
admin.site.register(models.SlLetterContentEmotion, SlGenericAdminView)
admin.site.register(models.SlLetterContentImmaterial, SlGenericAdminView)
admin.site.register(models.SlLetterContentCondition, SlGenericAdminView)
admin.site.register(models.SlLetterContentTreatment, SlGenericAdminView)
admin.site.register(models.SlLetterContentSensation, SlGenericAdminView)
admin.site.register(models.SlLetterContentContext, SlGenericAdminView)
admin.site.register(models.SlLetterContentAppearance, SlGenericAdminView)
admin.site.register(models.SlLetterContentRoles, SlGenericAdminView)
admin.site.register(models.SlLetterContentEstimatedProportionOfLetter, SlGenericAdminView)
admin.site.register(models.SlLetterContentCommentary, SlGenericAdminView)
admin.site.register(models.SlLetterContentState, SlGenericAdminView)

# Main models
admin.site.register(models.Letter, LetterAdminView)
admin.site.register(models.Person, PersonAdminView)
