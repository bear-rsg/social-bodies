from django.db import models
from django.contrib.auth.models import User
from . import apps



"""

Letter
Person
Location
Letter content

m2m - letter, letter (custom fields: relationship type)
m2m - letter, person (custom fields: relationship type)
m2m - person, person (custom fields: relationship type)


SL - relationship type (for different m2ms...)
SL - person_religion
SL - person_gender
SL - person_title (mr, ...)
SL - body_subject
SL - letter_collection

"""



# Select List models


class SlPersonGender(models.Model):
    """
    Select List table: person's gender (e.g. Male, Female)
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SlPersonReligion(models.Model):
    """
    Select List table: person's religion (e.g. Catholic, Protestant)
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SlPersonTitle(models.Model):
    """
    Select List table: person's title (e.g. Mr, Mrs, Dr)
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SlLetterCollection(models.Model):
    """
    Select List table: letter collection
    """
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



# Main models


class Letter(models.Model):
    """
    Letter model
    """
    
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    description_dynamic = models.TextField(blank=True, null=True)
    image_of_letter = models.ImageField(upload_to='researchdata/letters', blank=True, null=True)
    repository = models.CharField(max_length=255, blank=True, null=True)
    shelfmark = models.CharField(max_length=255, blank=True, null=True)
    permission_produce_text = models.BooleanField(blank=True, null=True)
    permission_produce_text = models.BooleanField(blank=True, null=True)
    transcription_original = models.TextField(blank=True, null=True)
    transcription_corrected = models.TextField(blank=True, null=True)
    sent_date = models.CharField(max_length=255, blank=True, null=True)
    sent_time = models.TimeField(blank=True, null=True)

    # sent_from = (location)
    # sent_to = (location)
    
    # Foreign key fields
    collection = models.ForeignKey(SlLetterCollection, on_delete=models.SET_NULL, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="letter_created_by",
                                        on_delete=models.PROTECT, blank=True, null=True)
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    lastupdated_by = models.ForeignKey(User, related_name="letter_lastupdated_by",
                                            on_delete=models.PROTECT, blank=True, null=True)
    lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    # Many to many relationship fields
    related_name = "letter"
    author = models.ManyToManyField("self", related_name=related_name, blank=True, db_table="{}_m2m_letter_letter".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    """
    Person model
    """
    
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    informal_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    date_of_death = models.CharField(max_length=100)    
    # Foreign key fields
    title = models.ForeignKey(SlPersonTitle, on_delete=models.SET_NULL, blank=True, null=True)
    religion = models.ForeignKey(SlPersonReligion, on_delete=models.SET_NULL, blank=True, null=True)
    gender = models.ForeignKey(SlPersonGender, on_delete=models.SET_NULL, blank=True, null=True)
    # Many to many relationship fields
    related_name = "person"
    author = models.ManyToManyField("self", related_name=related_name, blank=True, db_table="{}_m2m_author_author".format(apps.app_name))
    author = models.ManyToManyField("Letter", related_name=related_name, blank=True, db_table="{}_m2m_author_text".format(apps.app_name))
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
