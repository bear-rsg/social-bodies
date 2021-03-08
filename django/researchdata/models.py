from django.db import models
from django.contrib.auth.models import User

# Select List models


class SlGeneric(models.Model):
    """
    Select List table: person's gender (e.g. Male, Female)
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


class SlLetterContentSubject(SlGeneric):
    """
    Select List table: letter content - subject
    Inherits the standard SlGeneric model
    """


class SlLetterContentBodyPart(SlGeneric):
    """
    Select List table: letter content - body part
    Inherits the standard SlGeneric model
    """


class SlLetterContentBodilyActivity(SlGeneric):
    """
    Select List table: letter content - bodily activity
    Inherits the standard SlGeneric model
    """


class SlLetterContentEmotion(SlGeneric):
    """
    Select List table: letter content - emotion
    Inherits the standard SlGeneric model
    """


class SlLetterContentImmaterial(SlGeneric):
    """
    Select List table: letter content - immaterial
    Inherits the standard SlGeneric model
    """


class SlLetterContentConditionSpecificState(SlGeneric):
    """
    Select List table: letter content - condition (specific state)
    Inherits the standard SlGeneric model
    """


class SlLetterContentConditionSpecificLifeStage(SlGeneric):
    """
    Select List table: letter content - condition (specific life stage)
    Inherits the standard SlGeneric model
    """


class SlLetterContentConditionGeneralizedState(SlGeneric):
    """
    Select List table: letter content - condition (generalised state)
    Inherits the standard SlGeneric model
    """


class SlLetterContentTreatment(SlGeneric):
    """
    Select List table: letter content - treatment
    Inherits the standard SlGeneric model
    """


class SlLetterContentSensation(SlGeneric):
    """
    Select List table: letter content - sensation
    Inherits the standard SlGeneric model
    """


class SlLetterContentContext(SlGeneric):
    """
    Select List table: letter content - context
    Inherits the standard SlGeneric model
    """


class SlLetterContentLocation(SlGeneric):
    """
    Select List table: letter content - location
    Inherits the standard SlGeneric model
    """


class SlLetterContentType(SlGeneric):
    """
    Select List table: letter content - type
    Inherits the standard SlGeneric model
    """


class SlLetterContentAppearance(SlGeneric):
    """
    Select List table: letter content - appearance
    Inherits the standard SlGeneric model
    """


class SlLetterContentRole(SlGeneric):
    """
    Select List table: letter content - role
    Inherits the standard SlGeneric model
    """


class SlLetterContentEstimatedProportionOfLetter(SlGeneric):
    """
    Select List table: letter content - estimated proportion of letter
    Inherits the standard SlGeneric model
    """


class SlLetterContentCommentary(SlGeneric):
    """
    Select List table: letter content - commentary
    Inherits the standard SlGeneric model
    """


class SlLetterContentState(SlGeneric):
    """
    Select List table: letter content - state
    Inherits the standard SlGeneric model
    """


class SlM2MLetterLetterRelationshipType(SlGeneric):
    """
    Select List table: type of many to many relationship (letter <-> letter)
    Inherits the standard SlGeneric model
    """


class SlM2MLetterPersonRelationshipType(SlGeneric):
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
    sent_date = models.CharField(max_length=255, blank=True, null=True)
    sent_time = models.CharField(max_length=255, blank=True, null=True)
    sent_from_location = models.TextField(blank=True, null=True)
    sent_to_location = models.TextField(blank=True, null=True)
    content_type = models.ManyToManyField(SlLetterContentType, related_name=related_name, blank=True)
    state = models.ManyToManyField(SlLetterContentState, related_name=related_name, blank=True)
    commentary = models.ManyToManyField(SlLetterContentCommentary, related_name=related_name, blank=True)
    location = models.ManyToManyField(SlLetterContentLocation, related_name=related_name, blank=True)
    estimated_proportion_of_letter = models.ForeignKey(SlLetterContentEstimatedProportionOfLetter,
                                                       on_delete=models.SET_NULL, blank=True, null=True)


    # Meta
    created_by = models.ForeignKey(User, related_name="letter_created_by",
                                   on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    lastupdated_by = models.ForeignKey(User, related_name="letter_lastupdated_by",
                                       on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    # Many to many relationship fields
    letter = models.ManyToManyField("self", related_name=related_name,
                                    blank=True, through='M2MLetterLetter')
    # person = models.ManyToManyField("Person", related_name=related_name,
                                    # blank=True, through='M2MLetterPerson')
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class LetterContent(models.Model):
    """
    A Letter can have multiple 'contents' aka instances of interest that are worth recording
    """

    letter = models.ForeignKey(Letter, on_delete=models.CASCADE)

    person = models.ForeignKey("Person", on_delete=models.CASCADE, blank=True, null=True)
    person_other = models.CharField(max_length=255, blank=True, null=True, verbose_name='Person (other)')
    person_form_of_address = models.CharField(max_length=255, blank=True, null=True)
    person_letter_relationship = models.ForeignKey(SlM2MLetterPersonRelationshipType,
                                                   on_delete=models.SET_NULL,
                                                   blank=True, null=True)

    # subject = models.ForeignKey(SlLetterContentSubject, on_delete=models.SET_NULL, blank=True, null=True)

    # Many to many relationship fields
    related_name = "lettercontent"

    body_part = models.ManyToManyField(SlLetterContentBodyPart, related_name=related_name, blank=True)
    bodily_activity = models.ManyToManyField(SlLetterContentBodilyActivity, related_name=related_name, blank=True)
    appearance = models.ManyToManyField(SlLetterContentAppearance, related_name=related_name, blank=True)
    condition_specific_state = models.ManyToManyField(SlLetterContentConditionSpecificState,
                                                      related_name=related_name, blank=True)
    condition_specific_life_stage = models.ManyToManyField(SlLetterContentConditionSpecificLifeStage,
                                                           related_name=related_name, blank=True)
    condition_generalized_state = models.ManyToManyField(SlLetterContentConditionGeneralizedState,
                                                         related_name=related_name, blank=True)
    emotion = models.ManyToManyField(SlLetterContentEmotion, related_name=related_name, blank=True)
    immaterial = models.ManyToManyField(SlLetterContentImmaterial, related_name=related_name, blank=True)
    sensation = models.ManyToManyField(SlLetterContentSensation, related_name=related_name, blank=True)
    treatment = models.ManyToManyField(SlLetterContentTreatment, related_name=related_name, blank=True)
    context = models.ManyToManyField(SlLetterContentContext, related_name=related_name, blank=True)
    roles = models.ManyToManyField(SlLetterContentRole, related_name=related_name, blank=True)

    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)

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

    title = models.ForeignKey(SlPersonTitle, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    alternative_spelling_of_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.CharField(max_length=255, blank=True, null=True)
    date_of_death = models.CharField(max_length=255, blank=True, null=True)
    date_active = models.CharField(max_length=255, blank=True, null=True)
    gender = models.ForeignKey(SlPersonGender, on_delete=models.SET_NULL, blank=True, null=True)
    marital_status = models.ForeignKey(SlPersonMaritalStatus, on_delete=models.SET_NULL, blank=True, null=True)
    religion = models.ForeignKey(SlPersonReligion, on_delete=models.SET_NULL, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    rank = models.ForeignKey(SlPersonRank, on_delete=models.SET_NULL, blank=True, null=True)
    # Many to many relationship fields
    related_name = "related_person"
    person = models.ManyToManyField("self", related_name=related_name,
                                    through='M2MPersonPerson', blank=True)
    # letter = models.ManyToManyField("Letter", related_name=related_name,
                                    # through='M2MLetterPerson', blank=True)
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=True)

    def __str__(self):
        if self.first_name and self.middle_name and self.last_name:
            return "{} {} {}".format(self.first_name, self.middle_name, self.last_name)
        elif self.first_name and self.last_name:
            return "{} {}".format(self.first_name, self.last_name)
        elif self.first_name:
            return "{} ({})".format(self.first_name, self.id)


# Many to Many Relationships

# Letter > Letter (relationship type: conversation, event, familial, ...)
# Letter > Person (relationship type: primary author, secondary author, addressee)
# Person > Person


class M2MLetterLetter(models.Model):
    letter_1 = models.ForeignKey(Letter, related_name='letter_1', on_delete=models.CASCADE)
    letter_2 = models.ForeignKey(Letter, related_name='letter_2', on_delete=models.CASCADE)
    relationship_type = models.ForeignKey(SlM2MLetterLetterRelationshipType, on_delete=models.CASCADE)


# class M2MLetterPerson(models.Model):
#     letter = models.ForeignKey(Letter, on_delete=models.CASCADE)
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     relationship_type = models.ForeignKey(SlM2MLetterPersonRelationshipType, on_delete=models.CASCADE)
#     person_form_of_address = models.CharField(max_length=255, blank=True, null=True)


class M2MPersonPerson(models.Model):
    person_1 = models.ForeignKey(Person, related_name='person_1', on_delete=models.CASCADE)
    person_2 = models.ForeignKey(Person, related_name='person_2', on_delete=models.CASCADE)
    relationship_type = models.ForeignKey(SlM2MPersonPersonRelationshipType, on_delete=models.CASCADE)
