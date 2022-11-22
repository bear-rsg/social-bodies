from django.contrib import admin
from django.urls import reverse
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from django.utils.safestring import mark_safe
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Social Bodies: Admin Dashboard'


# Actions

admin.site.disable_action('delete_selected')


def admin_published_true(modeladmin, request, queryset):
    # Sets all objects in queryset to: admin_published = True
    queryset.update(admin_published=True)


def admin_published_false(modeladmin, request, queryset):
    # Sets all objects in queryset to: admin_published = False
    queryset.update(admin_published=False)


def permission_reproduce_text_none(modeladmin, request, queryset):
    # Sets all objects in queryset to: permission_reproduce_text = None
    queryset.update(permission_reproduce_text=None)


def permission_reproduce_text_true(modeladmin, request, queryset):
    # Sets all objects in queryset to: permission_reproduce_text = True
    queryset.update(permission_reproduce_text=True)


def permission_reproduce_text_false(modeladmin, request, queryset):
    # Sets all objects in queryset to: permission_reproduce_text = False
    queryset.update(permission_reproduce_text=False)


def permission_reproduce_image_none(modeladmin, request, queryset):
    # Sets all objects in queryset to: permission_reproduce_image = None
    queryset.update(permission_reproduce_image=None)


def permission_reproduce_image_true(modeladmin, request, queryset):
    # Sets all objects in queryset to: permission_reproduce_image = True
    queryset.update(permission_reproduce_image=True)


def permission_reproduce_image_false(modeladmin, request, queryset):
    # Sets all objects in queryset to: permission_reproduce_image = False
    queryset.update(permission_reproduce_image=False)


def approved_by_project_team_none(modeladmin, request, queryset):
    # Sets all objects in queryset to: approved_by_project_team = None
    queryset.update(approved_by_project_team=None)


def approved_by_project_team_true(modeladmin, request, queryset):
    # Sets all objects in queryset to: approved_by_project_team = True
    queryset.update(approved_by_project_team=True)


def approved_by_project_team_false(modeladmin, request, queryset):
    # Sets all objects in queryset to: approved_by_project_team = False
    queryset.update(approved_by_project_team=False)


def copy_public_transcription_to_parent_letter(modeladmin, request, queryset):
    # Copies the content of the public transcription text to the parent letter
    for public_transcription in queryset:
        public_transcription.letter.transcription_plain = public_transcription.transcription_text_full
        public_transcription.letter.save()


admin_published_true.short_description = "Admin published: Yes"
admin_published_false.short_description = "Admin published: No"
permission_reproduce_text_none.short_description = "Permission to reproduce text: Unknown"
permission_reproduce_text_true.short_description = "Permission to reproduce text: Yes"
permission_reproduce_text_false.short_description = "Permission to reproduce text: No"
permission_reproduce_image_none.short_description = "Permission to reproduce image: Unknown"
permission_reproduce_image_true.short_description = "Permission to reproduce image: Yes"
permission_reproduce_image_false.short_description = "Permission to reproduce image: No"
approved_by_project_team_none.short_description = "Approved by project team: Unknown"
approved_by_project_team_true.short_description = "Approved by project team: Yes"
approved_by_project_team_false.short_description = "Approved by project team: No"
copy_public_transcription_to_parent_letter.short_description = "Copy public transcription to parent letter"


# Functions

def fk_link(link_url, link_label):
    """
    Take a URL and a label and generate a link for foreign key fields in admin lists
    """
    if link_label is not None:
        return mark_safe('<a href="{}">{}</a>'.format(link_url, link_label))
    else:
        return '-'


# Inlines

class LetterLetterImageInline(admin.TabularInline):
    model = models.LetterImage
    readonly_fields = ('image_thumbnail',)


class LetterLetter1Inline(admin.TabularInline):
    model = models.Letter.letter.through
    fk_name = "letter_2"
    autocomplete_fields = ('letter_1', 'relationship_type')


class LetterLetter2Inline(admin.TabularInline):
    model = models.Letter.letter.through
    fk_name = "letter_1"
    autocomplete_fields = ('letter_2', 'relationship_type')


class LetterImagePublicTranscriptionInline(admin.TabularInline):
    model = models.LetterImagePublicTranscription
    fields = ('transcription_text',)


class PersonPerson1Inline(admin.TabularInline):
    model = models.Person.person.through
    fk_name = "person_2"
    autocomplete_fields = ('person_1', 'relationship_type')


class PersonPerson2Inline(admin.TabularInline):
    model = models.Person.person.through
    fk_name = "person_1"
    autocomplete_fields = ('person_2', 'relationship_type')


# Admin views


class SlGenericAdminView(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)


class LetterAdminView(admin.ModelAdmin):
    """
    Customise the Letter section of the Django admin
    """
    list_display = ('id',
                    'title',
                    'summary',
                    'permission_reproduce_text',
                    'permission_reproduce_image',
                    'admin_published',
                    'transcription_is_public')
    list_filter = ('permission_reproduce_text',
                   'permission_reproduce_image',
                   'admin_published',
                   'transcription_is_public',
                   ('collection', RelatedDropdownFilter),
                   ('repository', RelatedDropdownFilter),
                   ('letter_type', RelatedDropdownFilter),
                   ('commentary', RelatedDropdownFilter),
                   ('location', RelatedDropdownFilter),
                   ('estimated_proportion_of_letter', RelatedDropdownFilter))
    search_fields = ('title', 'summary', 'transcription_plain', 'transcription_normalized')
    ordering = ('-id',)
    inlines = [LetterLetterImageInline, LetterLetter1Inline, LetterLetter2Inline]
    readonly_fields = ('created_by', 'created_datetime', 'lastupdated_by', 'lastupdated_datetime')
    filter_horizontal = ('letter_type', 'commentary', 'location')
    autocomplete_fields = ('collection', 'repository')
    actions = (admin_published_true,
               admin_published_false,
               permission_reproduce_text_none,
               permission_reproduce_text_true,
               permission_reproduce_text_false,
               permission_reproduce_image_none,
               permission_reproduce_image_true,
               permission_reproduce_image_false)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('created_by', 'lastupdated_by')
        return queryset

    def save_model(self, request, obj, form, change):
        """
        Override default save_model, by adding values to automated fields
        """

        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
        obj.lastupdated_by = request.user
        obj.save()


class LetterPublicTranscriptionAdminView(admin.ModelAdmin):
    """
    Customise the LetterPublicTranscription section of the Django admin
    """

    list_display = ('id', 'letter', 'transcription_text_brief', 'approved_by_project_team',
                    'person_name', 'person_email', 'person_country',
                    'created_datetime')
    list_filter = ('approved_by_project_team',)
    search_fields = ('letter__title',
                     'letterimagepublictranscription__transcription_text',
                     'person_name',
                     'person_email',
                     'person_country__name')
    ordering = ('-created_datetime', 'id')
    inlines = [LetterImagePublicTranscriptionInline]
    readonly_fields = ('letter', 'created_datetime', 'lastupdated_datetime')
    actions = (approved_by_project_team_none,
               approved_by_project_team_true,
               approved_by_project_team_false,
               copy_public_transcription_to_parent_letter)


class LetterPersonAdminView(admin.ModelAdmin):
    """
    Customise the Letter Person section of the Django admin
    """
    list_display = ('id',
                    'letter_link',
                    'person_link',
                    'person_other',
                    'person_letter_relationship',
                    'admin_published')
    list_filter = (('person_letter_relationship', RelatedDropdownFilter),
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
                   ('state', RelatedDropdownFilter),
                   ('letter', RelatedDropdownFilter),
                   ('person', RelatedDropdownFilter))
    autocomplete_fields = ('person', 'letter')
    search_fields = ('letter__title',
                     'person__first_name',
                     'person__last_name',
                     'person_form_of_address',
                     'person_other',
                     'admin_notes')
    ordering = ('-id',)
    readonly_fields = ('created_by', 'created_datetime', 'lastupdated_by', 'lastupdated_datetime')
    list_select_related = ('person_letter_relationship',)
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
    actions = (admin_published_true,
               admin_published_false)

    def letter_link(self, letterperson):
        """
        Make the Letter FK reference in the list_display a clickable link, rather than plain text
        """
        url = reverse("admin:researchdata_letter_change", args=[letterperson.letter.id])
        return fk_link(url, letterperson.letter)
    letter_link.short_description = 'Letter'

    def person_link(self, letterperson):
        """
        Make the Person FK reference in the list_display a clickable link, rather than plain text
        """
        if letterperson.person is None:
            return '-'
        else:
            url = reverse("admin:researchdata_person_change", args=[letterperson.person.id])
            return fk_link(url, letterperson.person)
    person_link.short_description = 'Person'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('created_by',
                                           'lastupdated_by',
                                           'person_letter_relationship',
                                           'person',
                                           'letter')
        return queryset

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
                    'year_of_death', 'year_active_start', 'year_active_end', 'admin_published')
    list_filter = (('gender', RelatedDropdownFilter),
                   ('title', RelatedDropdownFilter),
                   ('marital_status', RelatedDropdownFilter),
                   ('religion', RelatedDropdownFilter),
                   ('rank', RelatedDropdownFilter))
    search_fields = ('first_name', 'middle_name', 'last_name')
    ordering = ('last_name', 'first_name', 'middle_name', 'id')
    inlines = [PersonPerson1Inline, PersonPerson2Inline]
    readonly_fields = ('created_by', 'created_datetime', 'lastupdated_by', 'lastupdated_datetime')
    filter_horizontal = ('title', 'marital_status', 'religion', 'rank')
    actions = (admin_published_true,
               admin_published_false)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('created_by', 'lastupdated_by')
        return queryset

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
    list_display = ('id', 'letter_1_link', 'letter_2_link', 'relationship_type')
    list_filter = (('relationship_type', RelatedDropdownFilter),
                   ('letter_1', RelatedDropdownFilter),
                   ('letter_2', RelatedDropdownFilter))
    search_fields = ('letter_1', 'letter_2', 'relationship_type')
    ordering = ('-id',)

    def letter_1_link(self, letterperson):
        """
        Make the Letter 1 FK reference in the list_display a clickable link, rather than plain text
        """
        url = reverse("admin:researchdata_letter_change", args=[letterperson.letter_1.id])
        return fk_link(url, letterperson.letter_1)
    letter_1_link.short_description = 'Letter (1)'

    def letter_2_link(self, letterperson):
        """
        Make the Letter 2 FK reference in the list_display a clickable link, rather than plain text
        """
        url = reverse("admin:researchdata_letter_change", args=[letterperson.letter_2.id])
        return fk_link(url, letterperson.letter_2)
    letter_2_link.short_description = 'Letter (2)'


class M2MPersonPersonAdminView(admin.ModelAdmin):
    """
    Customise the M2M Person <-> Person section of the Django admin
    """
    list_display = ('id', 'person_1_link', 'person_2_link', 'relationship_type')
    list_filter = ('relationship_type',)
    search_fields = ('person_1', 'person_2', 'relationship_type')
    ordering = ('-id',)

    def person_1_link(self, letterperson):
        """
        Make the Person 1 FK reference in the list_display a clickable link, rather than plain text
        """
        url = reverse("admin:researchdata_person_change", args=[letterperson.person_1.id])
        return fk_link(url, letterperson.person_1)
    person_1_link.short_description = 'Person (1)'

    def person_2_link(self, letterperson):
        """
        Make the Person 2 FK reference in the list_display a clickable link, rather than plain text
        """
        url = reverse("admin:researchdata_person_change", args=[letterperson.person_2.id])
        return fk_link(url, letterperson.person_2)
    person_2_link.short_description = 'Person (2)'


# Register classes

# SL models
admin.site.register(models.SlCountry, SlGenericAdminView)
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
admin.site.register(models.SlLetterPersonGender, SlGenericAdminView)
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
admin.site.register(models.LetterPublicTranscription, LetterPublicTranscriptionAdminView)
admin.site.register(models.LetterPerson, LetterPersonAdminView)
admin.site.register(models.Person, PersonAdminView)

# Many to Many models
admin.site.register(models.M2MLetterLetter, M2MLetterLetterAdminView)
admin.site.register(models.M2MPersonPerson, M2MPersonPersonAdminView)
