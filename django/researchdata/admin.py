from django.contrib import admin
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Material Identities, Social Bodies: Admin Dashboard'


class SlGenericAdminView(admin.ModelAdmin):
    list_display = ('name', 'description')
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


class LetterContentAdminView(admin.ModelAdmin):
    """
    Customise the Letter section of the Django admin
    """
    list_display = ('id',
                    'body_part',
                    'bodily_activity',
                    'emotion',
                    'immaterial',
                    'condition',
                    'treatment',
                    'sensation',
                    'context',
                    'appearance',
                    'roles',
                    'estimated_proportion_of_letter',
                    'commentary',
                    'state')
    list_filter = ('body_part',
                   'bodily_activity',
                   'emotion',
                   'immaterial',
                   'condition',
                   'treatment',
                   'sensation',
                   'context',
                   'appearance',
                   'roles',
                   'estimated_proportion_of_letter',
                   'commentary',
                   'state')
    ordering = ('-id',)


class PersonAdminView(admin.ModelAdmin):
    """
    Customise the Person section of the Django admin
    """
    list_display = ('id', 'title', 'first_name', 'middle_name', 'last_name', 'informal_name', 'gender', 'religion')
    list_filter = ('title', 'religion', 'gender')
    search_fields = ('first_name', 'middle_name', 'last_name', 'informal_name')
    ordering = ('-id',)


class M2MLetterLetterAdminView(admin.ModelAdmin):
    """
    Customise the M2M Letter <-> Letter section of the Django admin
    """
    list_display = ('id', 'letter_1', 'letter_2', 'relationship_type')
    list_filter = ('relationship_type',)
    search_fields = ('letter_1', 'letter_2', 'relationship_type')
    ordering = ('-id',)


class M2MLetterPersonAdminView(admin.ModelAdmin):
    """
    Customise the M2M Letter <-> Person section of the Django admin
    """
    list_display = ('id', 'letter', 'person', 'relationship_type')
    list_filter = ('relationship_type',)
    search_fields = ('letter', 'person', 'relationship_type')
    ordering = ('-id',)


class M2MPersonPersonAdminView(admin.ModelAdmin):
    """
    Customise the M2M Person <-> Person section of the Django admin
    """
    list_display = ('id', 'person_1', 'person_2', 'relationship_type')
    list_filter = ('relationship_type',)
    search_fields = ('person_1', 'person_2', 'relationship_type')
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
admin.site.register(models.SlLetterContentRole, SlGenericAdminView)
admin.site.register(models.SlLetterContentEstimatedProportionOfLetter, SlGenericAdminView)
admin.site.register(models.SlLetterContentCommentary, SlGenericAdminView)
admin.site.register(models.SlLetterContentState, SlGenericAdminView)

# Main models
admin.site.register(models.Letter, LetterAdminView)
admin.site.register(models.LetterContent, LetterContentAdminView)
admin.site.register(models.Person, PersonAdminView)

# Many to Many models
admin.site.register(models.M2MLetterLetter, M2MLetterLetterAdminView)
admin.site.register(models.M2MLetterPerson, M2MLetterPersonAdminView)
admin.site.register(models.M2MPersonPerson, M2MPersonPersonAdminView)
