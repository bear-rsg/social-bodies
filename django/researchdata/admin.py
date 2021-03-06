from django.contrib import admin
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Material Identities, Social Bodies: Admin Dashboard'


# Inlines

class LetterLetterImageInline(admin.TabularInline):
    model = models.LetterImage


class LetterLetterInline(admin.TabularInline):
    model = models.Letter.letter.through
    fk_name = "letter_1"


class LetterPersonInline(admin.TabularInline):
    model = models.Letter.person.through


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
    list_filter = ('collection',)
    search_fields = ('title', 'summary')
    ordering = ('-id',)
    inlines = [LetterLetterImageInline, LetterLetterInline, LetterPersonInline]
    readonly_fields = ('created_by', 'created_datetime', 'lastupdated_by', 'lastupdated_datetime')

    def save_model(self, request, obj, form, change):
        """
        Override default save_model, by adding values to automated fields
        """

        # Created by
        if getattr(obj, 'created_by', None) is None:
            obj.created_by = request.user
            obj.lastupdated_by = request.user
        # Last updated by
        else:
            obj.lastupdated_by = request.user
        obj.save()


class LetterContentAdminView(admin.ModelAdmin):
    """
    Customise the Letter Content section of the Django admin
    """
    list_display = ('id',
                    'letter',
                    'subject',
                    'estimated_proportion_of_letter')
    list_filter = ('letter',
                   'subject',
                   'estimated_proportion_of_letter')
    ordering = ('-id',)


class PersonAdminView(admin.ModelAdmin):
    """
    Customise the Person section of the Django admin
    """
    list_display = ('id', 'title', 'first_name', 'middle_name', 'last_name', 'gender', 'religion')
    list_filter = ('title', 'religion', 'gender')
    search_fields = ('first_name', 'middle_name', 'last_name')
    ordering = ('-id',)
    inlines = [LetterPersonInline, PersonPersonInline]


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
    list_display = ('id', 'letter', 'person', 'relationship_type', 'person_form_of_address')
    list_filter = ('relationship_type',)
    search_fields = ('letter', 'person', 'relationship_type', 'person_form_of_address')
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
# Letter Content
admin.site.register(models.SlLetterContentSubject, SlGenericAdminView)
admin.site.register(models.SlLetterContentBodyPart, SlGenericAdminView)
admin.site.register(models.SlLetterContentBodilyActivity, SlGenericAdminView)
admin.site.register(models.SlLetterContentEmotion, SlGenericAdminView)
admin.site.register(models.SlLetterContentImmaterial, SlGenericAdminView)
admin.site.register(models.SlLetterContentCondition, SlGenericAdminView)
admin.site.register(models.SlLetterContentTreatment, SlGenericAdminView)
admin.site.register(models.SlLetterContentSensation, SlGenericAdminView)
admin.site.register(models.SlLetterContentContext, SlGenericAdminView)
admin.site.register(models.SlLetterContentLocation, SlGenericAdminView)
admin.site.register(models.SlLetterContentType, SlGenericAdminView)
admin.site.register(models.SlLetterContentAppearance, SlGenericAdminView)
admin.site.register(models.SlLetterContentRole, SlGenericAdminView)
admin.site.register(models.SlLetterContentEstimatedProportionOfLetter, SlGenericAdminView)
admin.site.register(models.SlLetterContentCommentary, SlGenericAdminView)
admin.site.register(models.SlLetterContentState, SlGenericAdminView)
# Sl M2M
admin.site.register(models.SlM2MLetterLetterRelationshipType, SlGenericAdminView)
admin.site.register(models.SlM2MLetterPersonRelationshipType, SlGenericAdminView)
admin.site.register(models.SlM2MPersonPersonRelationshipType, SlGenericAdminView)

# Main models
admin.site.register(models.Letter, LetterAdminView)
admin.site.register(models.LetterContent, LetterContentAdminView)
admin.site.register(models.Person, PersonAdminView)

# Many to Many models
admin.site.register(models.M2MLetterLetter, M2MLetterLetterAdminView)
admin.site.register(models.M2MLetterPerson, M2MLetterPersonAdminView)
admin.site.register(models.M2MPersonPerson, M2MPersonPersonAdminView)
