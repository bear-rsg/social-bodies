from django.contrib import admin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Material Identities, Social Bodies: Admin Dashboard'


# Inlines

class LetterLetterImageInline(admin.TabularInline):
    model = models.LetterImage


class LetterLetterInline(admin.TabularInline):
    model = models.Letter.letter.through
    fk_name = "letter_1"


class PersonPersonInline(admin.TabularInline):
    model = models.Person.person.through
    fk_name = "person_1"


# Admin views


class SlGenericAdminView(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('id',)


class LetterAdminView(admin.ModelAdmin):
    """
    Customise the Letter section of the Django admin
    """
    list_display = ('id', 'title', 'summary')
    list_filter = (('collection', RelatedDropdownFilter),
                   ('repository', RelatedDropdownFilter),
                   ('letter_type', RelatedDropdownFilter),
                   ('commentary', RelatedDropdownFilter),
                   ('location', RelatedDropdownFilter),
                   ('estimated_proportion_of_letter', RelatedDropdownFilter))
    search_fields = ('title', 'summary', 'transcription_plain', 'transcription_normalized')
    ordering = ('-id',)
    inlines = [LetterLetterImageInline, LetterLetterInline]
    readonly_fields = ('created_by', 'created_datetime', 'lastupdated_by', 'lastupdated_datetime')
    filter_horizontal = ('letter_type', 'commentary', 'location')

    def save_model(self, request, obj, form, change):
        """
        Override default save_model, by adding values to automated fields
        """

        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.lastupdated_by = request.user
        obj.save()


class LetterPersonAdminView(admin.ModelAdmin):
    """
    Customise the Letter Person section of the Django admin
    """
    list_display = ('id',
                    'letter',
                    'person',
                    'person_other',
                    'person_letter_relationship')
    list_filter = ('letter',
                   'person',
                   ('person_letter_relationship', RelatedDropdownFilter),
                   ('body_part', RelatedDropdownFilter),
                   ('bodily_activity', RelatedDropdownFilter),
                   ('appearance', RelatedDropdownFilter),
                   ('condition_specific_state', RelatedDropdownFilter),
                   ('condition_specific_life_stage', RelatedDropdownFilter),
                   ('condition_generalized_state', RelatedDropdownFilter),
                   ('emotion', RelatedDropdownFilter),
                   ('immaterial', RelatedDropdownFilter),
                   ('sensation', RelatedDropdownFilter),
                   ('treatment', RelatedDropdownFilter),
                   ('context', RelatedDropdownFilter),
                   ('roles', RelatedDropdownFilter),
                   ('state', RelatedDropdownFilter))
    search_fields = ('letter__title',
                     'person__first_name',
                     'person__last_name',
                     'person_form_of_address',
                     'person_other',
                     'admin_notes')
    ordering = ('-id',)
    readonly_fields = ('created_by', 'created_datetime', 'lastupdated_by', 'lastupdated_datetime')
    filter_horizontal = ('body_part',
                         'bodily_activity',
                         'appearance',
                         'condition_specific_state',
                         'condition_specific_life_stage',
                         'condition_generalized_state',
                         'emotion',
                         'immaterial',
                         'sensation',
                         'treatment',
                         'context',
                         'roles',
                         'state')

    def save_model(self, request, obj, form, change):
        """
        Override default save_model, by adding values to automated fields
        """

        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.lastupdated_by = request.user
        obj.save()


class PersonAdminView(admin.ModelAdmin):
    """
    Customise the Person section of the Django admin
    """
    list_display = ('id', 'first_name', 'middle_name', 'last_name', 'year_of_birth',
                    'year_of_death', 'year_active_start', 'year_active_end')
    list_filter = (('gender', RelatedDropdownFilter),
                   ('title', RelatedDropdownFilter),
                   ('marital_status', RelatedDropdownFilter),
                   ('religion', RelatedDropdownFilter),
                   ('rank', RelatedDropdownFilter))
    search_fields = ('first_name', 'middle_name', 'last_name')
    ordering = ('-id',)
    inlines = [PersonPersonInline]
    readonly_fields = ('created_by', 'created_datetime', 'lastupdated_by', 'lastupdated_datetime')
    filter_horizontal = ('title', 'marital_status', 'religion', 'rank')

    def save_model(self, request, obj, form, change):
        """
        Override default save_model, by adding values to automated fields
        """

        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.lastupdated_by = request.user
        obj.save()


class M2MLetterLetterAdminView(admin.ModelAdmin):
    """
    Customise the M2M Letter <-> Letter section of the Django admin
    """
    list_display = ('id', 'letter_1', 'letter_2', 'relationship_type')
    list_filter = ('relationship_type',)
    search_fields = ('letter_1', 'letter_2', 'relationship_type')
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
# Person
admin.site.register(models.SlPersonGender, SlGenericAdminView)
admin.site.register(models.SlPersonMaritalStatus, SlGenericAdminView)
admin.site.register(models.SlPersonRank, SlGenericAdminView)
admin.site.register(models.SlPersonReligion, SlGenericAdminView)
admin.site.register(models.SlPersonTitle, SlGenericAdminView)
# Letter
admin.site.register(models.SlLetterCollection, SlGenericAdminView)
admin.site.register(models.SlLetterRepository, SlGenericAdminView)
# Letter Person
admin.site.register(models.SlLetterPersonBodyPart, SlGenericAdminView)
admin.site.register(models.SlLetterPersonBodilyActivity, SlGenericAdminView)
admin.site.register(models.SlLetterPersonEmotion, SlGenericAdminView)
admin.site.register(models.SlLetterPersonImmaterial, SlGenericAdminView)
admin.site.register(models.SlLetterPersonConditionSpecificState, SlGenericAdminView)
admin.site.register(models.SlLetterPersonConditionSpecificLifeStage, SlGenericAdminView)
admin.site.register(models.SlLetterPersonConditionGeneralizedState, SlGenericAdminView)
admin.site.register(models.SlLetterPersonTreatment, SlGenericAdminView)
admin.site.register(models.SlLetterPersonSensation, SlGenericAdminView)
admin.site.register(models.SlLetterPersonContext, SlGenericAdminView)
admin.site.register(models.SlLetterLocation, SlGenericAdminView)
admin.site.register(models.SlLetterType, SlGenericAdminView)
admin.site.register(models.SlLetterPersonAppearance, SlGenericAdminView)
admin.site.register(models.SlLetterPersonRole, SlGenericAdminView)
admin.site.register(models.SlLetterEstimatedProportionOfLetter, SlGenericAdminView)
admin.site.register(models.SlLetterCommentary, SlGenericAdminView)
admin.site.register(models.SlLetterPersonState, SlGenericAdminView)
# Sl M2M
admin.site.register(models.SlM2MLetterLetterRelationshipType, SlGenericAdminView)
admin.site.register(models.SlLetterPersonRelationshipType, SlGenericAdminView)
admin.site.register(models.SlM2MPersonPersonRelationshipType, SlGenericAdminView)

# Main models
admin.site.register(models.Letter, LetterAdminView)
admin.site.register(models.LetterPerson, LetterPersonAdminView)
admin.site.register(models.Person, PersonAdminView)

# Many to Many models
admin.site.register(models.M2MLetterLetter, M2MLetterLetterAdminView)
admin.site.register(models.M2MPersonPerson, M2MPersonPersonAdminView)
