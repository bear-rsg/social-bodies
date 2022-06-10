from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import textwrap


def singular_plural(count, word_singular, word_plural=None):
    """
    Returns a string of the count and either the singular or plural version of the word
    Used a lot in the model in list_details() methods, for correctly displaying counts
    E.g. 1 script instead of 1 scripts
    """
    if word_plural is None:
        # Add 's' to singular, unless singular ends in 'y' (then replace 'y' with 'ies') e.g. entity -> entities
        word_plural = f'{word_singular}s' if word_singular[-1] != 'y' else f'{word_singular[0:-1]}ies'
    return f'{count} {word_singular}' if count == 1 else f'{count} {word_plural}'


# Select List models


class SlGeneric(models.Model):
    """
    A generic Select List table
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SlPersonGender(SlGeneric):
    """
    Select List table: person's gender (e.g. Male, Female)
    Inherits the standard SlGeneric model
    """


class SlPersonMaritalStatus(SlGeneric):
    """
    Select List table: person's marital status (e.g. Married, Unmarried, Widowed)
    Inherits the standard SlGeneric model
    """


class SlPersonRank(SlGeneric):
    """
    Select List table: person's rank
    Inherits the standard SlGeneric model
    """


class SlPersonReligion(SlGeneric):
    """
    Select List table: person's religion (e.g. Catholic, Protestant)
    Inherits the standard SlGeneric model
    """


class SlPersonTitle(SlGeneric):
    """
    Select List table: person's title (e.g. Mr, Mrs, Dr)
    Inherits the standard SlGeneric model
    """


class SlLetterCollection(SlGeneric):
    """
    Select List table: letter collection
    Inherits the standard SlGeneric model
    """


class SlLetterRepository(SlGeneric):
    """
    Select List table: letter repository
    Inherits the standard SlGeneric model
    """


class SlLetterPersonBodyPart(SlGeneric):
    """
    Select List table: letter person - body part
    Inherits the standard SlGeneric model
    """


class SlLetterPersonBodilyActivity(SlGeneric):
    """
    Select List table: letter person - bodily activity
    Inherits the standard SlGeneric model
    """


class SlLetterPersonEmotion(SlGeneric):
    """
    Select List table: letter person - emotion
    Inherits the standard SlGeneric model
    """


class SlLetterPersonGender(SlGeneric):
    """
    Select List table: letter person - gender
    Inherits the standard SlGeneric model
    """


class SlLetterPersonImmaterial(SlGeneric):
    """
    Select List table: letter person - immaterial
    Inherits the standard SlGeneric model
    """


class SlLetterPersonConditionSpecificState(SlGeneric):
    """
    Select List table: letter person - condition (specific state)
    Inherits the standard SlGeneric model
    """


class SlLetterPersonConditionSpecificLifeStage(SlGeneric):
    """
    Select List table: letter person - condition (specific life stage)
    Inherits the standard SlGeneric model
    """


class SlLetterPersonConditionGeneralizedState(SlGeneric):
    """
    Select List table: letter person - condition (generalised state)
    Inherits the standard SlGeneric model
    """


class SlLetterPersonTreatment(SlGeneric):
    """
    Select List table: letter person - treatment
    Inherits the standard SlGeneric model
    """


class SlLetterPersonSensation(SlGeneric):
    """
    Select List table: letter person - sensation
    Inherits the standard SlGeneric model
    """


class SlLetterPersonContext(SlGeneric):
    """
    Select List table: letter person - context
    Inherits the standard SlGeneric model
    """


class SlLetterLocation(SlGeneric):
    """
    Select List table: letter person - location
    Inherits the standard SlGeneric model
    """


class SlLetterType(SlGeneric):
    """
    Select List table: letter person - type
    Inherits the standard SlGeneric model
    """


class SlLetterPersonAppearance(SlGeneric):
    """
    Select List table: letter person - appearance
    Inherits the standard SlGeneric model
    """


class SlLetterPersonRole(SlGeneric):
    """
    Select List table: letter person - role
    Inherits the standard SlGeneric model
    """


class SlLetterEstimatedProportionOfLetter(SlGeneric):
    """
    Select List table: letter person - estimated proportion of letter
    Inherits the standard SlGeneric model
    """


class SlLetterCommentary(SlGeneric):
    """
    Select List table: letter person - commentary
    Inherits the standard SlGeneric model
    """


class SlLetterPersonState(SlGeneric):
    """
    Select List table: letter person - state
    Inherits the standard SlGeneric model
    """


class SlM2MLetterLetterRelationshipType(SlGeneric):
    """
    Select List table: type of many to many relationship (letter <-> letter)
    Inherits the standard SlGeneric model
    """


class SlLetterPersonRelationshipType(SlGeneric):
    """
    Select List table: type of many to many relationship (letter <-> person)
    Inherits the standard SlGeneric model
    """


class SlM2MPersonPersonRelationshipType(SlGeneric):
    """
    Select List table: type of many to many relationship (person <-> person)
    Inherits the standard SlGeneric model
    """


# Main models


class Letter(models.Model):
    """
    Letter model
    """

    related_name = "letter"

    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    collection = models.ForeignKey(SlLetterCollection, on_delete=models.SET_NULL, blank=True, null=True)
    item_number = models.CharField(max_length=255, blank=True, null=True)
    repository = models.ForeignKey(SlLetterRepository, on_delete=models.SET_NULL, blank=True, null=True)
    permission_reproduce_text = models.BooleanField(blank=True, null=True)
    permission_reproduce_image = models.BooleanField(blank=True, null=True)
    transcription_plain = models.TextField(blank=True, null=True)
    transcription_normalized = models.TextField(blank=True, null=True)
    sent_date_year = models.IntegerField(blank=True, null=True,
                                         validators=[MinValueValidator(99), MaxValueValidator(2000)])
    sent_date_month = models.IntegerField(blank=True, null=True,
                                          validators=[MinValueValidator(1), MaxValueValidator(12)])
    sent_date_day = models.IntegerField(blank=True, null=True,
                                        validators=[MinValueValidator(1), MaxValueValidator(31)])
    sent_date_is_approximate = models.BooleanField(default=False)
    sent_date_as_given = models.CharField(max_length=255, blank=True, null=True)
    sent_time = models.CharField(max_length=255, blank=True, null=True)
    sent_from_location = models.TextField(blank=True, null=True)
    sent_to_location = models.TextField(blank=True, null=True)
    letter_type = models.ManyToManyField(SlLetterType, related_name=related_name, blank=True)
    commentary = models.ManyToManyField(SlLetterCommentary, related_name=related_name, blank=True)
    location = models.ManyToManyField(SlLetterLocation, related_name=related_name, blank=True)
    estimated_proportion_of_letter = models.ForeignKey(SlLetterEstimatedProportionOfLetter,
                                                       on_delete=models.SET_NULL, blank=True, null=True)
    # Many to many relationship fields
    letter = models.ManyToManyField("self", related_name=related_name, blank=True, through='M2MLetterLetter')
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Meta fields
    created_by = models.ForeignKey(User, related_name="letter_created_by",
                                   on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    lastupdated_by = models.ForeignKey(User, related_name="letter_lastupdated_by",
                                       on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    @property
    def list_image(self):
        return self.letterimage_set.first()

    @property
    def list_title(self):
        return textwrap.shorten(self.title, width=90, placeholder="...")

    @property
    def list_details(self):
        return "Details."

    def __str__(self):
        return "{} - {}".format(self.id, self.title)


class LetterPerson(models.Model):
    """
    A Letter can have multiple 'contents' aka instances of interest that are worth recording
    """

    letter = models.ForeignKey("Letter", on_delete=models.RESTRICT)
    person = models.ForeignKey("Person", on_delete=models.RESTRICT, blank=True, null=True)
    person_form_of_address = models.CharField(max_length=255, blank=True, null=True)
    person_other = models.CharField(max_length=255, blank=True, null=True,
                                    verbose_name='Person/People (if not specified in Person table)')
    person_other_gender = models.ForeignKey(SlLetterPersonGender, on_delete=models.SET_NULL, blank=True, null=True,
                                            verbose_name='Gender of person/people (if not specified in Person table)')
    person_letter_relationship = models.ForeignKey(SlLetterPersonRelationshipType,
                                                   on_delete=models.SET_NULL,
                                                   blank=True, null=True)

    # Many to many relationship fields
    related_name = "letterperson"

    body_part = models.ManyToManyField(SlLetterPersonBodyPart, related_name=related_name, blank=True)
    bodily_activity = models.ManyToManyField(SlLetterPersonBodilyActivity, related_name=related_name, blank=True)
    appearance = models.ManyToManyField(SlLetterPersonAppearance, related_name=related_name, blank=True)
    condition_specific_state = models.ManyToManyField(SlLetterPersonConditionSpecificState,
                                                      related_name=related_name, blank=True)
    condition_specific_life_stage = models.ManyToManyField(SlLetterPersonConditionSpecificLifeStage,
                                                           related_name=related_name, blank=True)
    condition_generalized_state = models.ManyToManyField(SlLetterPersonConditionGeneralizedState,
                                                         related_name=related_name, blank=True)
    emotion = models.ManyToManyField(SlLetterPersonEmotion, related_name=related_name, blank=True)
    immaterial = models.ManyToManyField(SlLetterPersonImmaterial, related_name=related_name, blank=True)
    sensation = models.ManyToManyField(SlLetterPersonSensation, related_name=related_name, blank=True)
    treatment = models.ManyToManyField(SlLetterPersonTreatment, related_name=related_name, blank=True)
    context = models.ManyToManyField(SlLetterPersonContext, related_name=related_name, blank=True)
    roles = models.ManyToManyField(SlLetterPersonRole, related_name=related_name, blank=True)
    state = models.ManyToManyField(SlLetterPersonState, related_name=related_name, blank=True)

    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Meta fields
    created_by = models.ForeignKey(User, related_name="letterperson_created_by",
                                   on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    lastupdated_by = models.ForeignKey(User, related_name="letterperson_lastupdated_by",
                                       on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    def __str__(self):
        if self.letter:
            return "Content from letter: {}".format(self.letter.title)
        else:
            return "Content from a letter"

    class Meta:
        unique_together = (('letter', 'person'), ('letter', 'person_other'))


class LetterImage(models.Model):
    """
    A Letter can have multiple images
    """

    letter = models.ForeignKey(Letter, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='researchdata/letters')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        if self.letter:
            return "Image of letter: {}".format(self.letter.title)
        else:
            return "An image of a letter"


class Person(models.Model):
    """
    Person model
    """

    related_name = "related_person"

    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    alternative_spelling_of_name = models.CharField(max_length=255, blank=True, null=True)
    alternative_names = models.CharField(max_length=255, blank=True, null=True)
    year_of_birth = models.IntegerField(blank=True, null=True)
    year_of_death = models.IntegerField(blank=True, null=True)
    year_active_start = models.IntegerField(blank=True, null=True)
    year_active_end = models.IntegerField(blank=True, null=True)
    gender = models.ForeignKey(SlPersonGender, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.ManyToManyField(SlPersonTitle, related_name=related_name, blank=True)
    marital_status = models.ManyToManyField(SlPersonMaritalStatus, related_name=related_name, blank=True)
    religion = models.ManyToManyField(SlPersonReligion, related_name=related_name, blank=True)
    rank = models.ManyToManyField(SlPersonRank, related_name=related_name, blank=True)
    occupation = models.TextField(blank=True, null=True)
    person = models.ManyToManyField("self", related_name=related_name, through='M2MPersonPerson', blank=True)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)
    # Meta fields
    created_by = models.ForeignKey(User, related_name="person_created_by",
                                   on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    lastupdated_by = models.ForeignKey(User, related_name="person_lastupdated_by",
                                       on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    @property
    def full_name(self):
        return ' '.join(n for n in [self.first_name, self.middle_name, self.last_name] if n)

    @property
    def list_title(self):
        return textwrap.shorten(self.full_name, width=90, placeholder="...")

    @property
    def list_details(self):
        return "Details."

    def __str__(self):
        # Set default value
        name = "Person of id: {}".format(self.id)
        # Set the name, if available
        if self.first_name and self.middle_name and self.last_name:
            name = "{} - {} {} {}".format(self.id, self.first_name, self.middle_name, self.last_name)
        elif self.first_name and self.last_name:
            name = "{} - {} {}".format(self.id, self.first_name, self.last_name)
        elif self.first_name:
            name = "{} - {}".format(self.id, self.first_name)
        # Append a date to help identify
        if self.year_of_birth:
            name += " (Born: {})".format(self.year_of_birth)
        elif self.year_of_death:
            name += " (Died: {})".format(self.year_of_death)
        elif self.year_active_start:
            name += " (Active: {})".format(self.year_active_start)
        return name


# Many to Many Relationships


class M2MLetterLetter(models.Model):
    letter_1 = models.ForeignKey(Letter, related_name='letter_1', on_delete=models.CASCADE)
    letter_2 = models.ForeignKey(Letter, related_name='letter_2', on_delete=models.CASCADE)
    relationship_type = models.ForeignKey(SlM2MLetterLetterRelationshipType, on_delete=models.CASCADE)


class M2MPersonPerson(models.Model):
    person_1 = models.ForeignKey(Person, related_name='person_1', on_delete=models.CASCADE)
    person_2 = models.ForeignKey(Person, related_name='person_2', on_delete=models.CASCADE)
    relationship_type = models.ForeignKey(SlM2MPersonPersonRelationshipType, on_delete=models.CASCADE)
