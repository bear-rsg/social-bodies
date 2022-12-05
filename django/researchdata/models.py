from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image, ImageOps
from django.core.files import File
from io import BytesIO
import os
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

    @property
    def html_details_list_item_text(self):
        return str(self)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'id']


class SlCountry(SlGeneric):
    """
    Select List table: country (e.g. UK, France, Spain)
    Inherits from standard SlGeneric model
    """


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

    related_name = "related_letter"

    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    collection = models.ForeignKey(SlLetterCollection,
                                   related_name=related_name,
                                   on_delete=models.SET_NULL,
                                   blank=True, null=True)
    item_number = models.CharField(max_length=255, blank=True, null=True)
    repository = models.ForeignKey(SlLetterRepository,
                                   related_name=related_name,
                                   on_delete=models.SET_NULL,
                                   blank=True, null=True)
    copyright_holder_untraced = models.BooleanField(default=False)
    permission_reproduce_text = models.BooleanField(blank=True, null=True)
    permission_reproduce_image = models.BooleanField(blank=True, null=True)
    transcription_is_public = models.BooleanField(default=False,
                                                  verbose_name='available for public transcription',
                                                  help_text='Tick to make this letter available for general users to transcribe through the public website')  # NOQA
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
                                                       related_name=related_name,
                                                       on_delete=models.SET_NULL, blank=True, null=True)
    # Many to many relationship fields
    letter = models.ManyToManyField("self", related_name=related_name, blank=True, through='M2MLetterLetter')
    # Admin fields
    admin_notes = models.TextField(blank=True, null=True)
    admin_published = models.BooleanField(default=False)
    # Meta fields
    created_by = models.ForeignKey(User, related_name="letter_created_by",
                                   on_delete=models.PROTECT, blank=True, null=True, verbose_name="Created By")
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    lastupdated_by = models.ForeignKey(User, related_name="letter_lastupdated_by",
                                       on_delete=models.PROTECT, blank=True, null=True, verbose_name="Last Updated By")
    lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    @property
    def list_image_url(self):
        if self.permission_reproduce_image and self.letterimage_set.all():
            thumbnail = self.letterimage_set.all()[0].image_thumbnail
            if thumbnail:
                return thumbnail.url

    @property
    def list_title(self):
        return textwrap.shorten(self.title, width=90, placeholder="...")

    @property
    def list_details(self):
        details = f"<strong>People featured:</strong> {self.letterperson_set.count()}<br>"
        details += f"<strong>Collection:</strong> {self.collection.name}<br>" if self.collection else ''
        details += f"<strong>Item Number:</strong> {self.item_number}<br>" if self.item_number else ''
        details += f"<strong>Repository:</strong> {self.repository.name}<br>" if self.repository else ''
        if self.summary:
            details += f"<strong>Summary:</strong> {textwrap.shorten(self.summary, width=690, placeholder='...')}"
        return details.strip()

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

    @property
    def letter_name(self):
        return self.letter.title

    @property
    def person_name(self):
        if self.person:
            return self.person.full_name
        elif self.person_other:
            return self.person_other
        elif self.person_form_of_address:
            return self.person_form_of_address
        elif self.person_letter_relationship:
            return f"Unnamed person ({self.person_form_of_address})"
        else:
            return "Unnamed person"

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

    media_dir_letterimage = 'researchdata/letters'
    media_dir_letterimage_thumbnails = media_dir_letterimage + '-thumbnails'

    letter = models.ForeignKey(Letter, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=media_dir_letterimage)
    image_thumbnail = models.ImageField(upload_to=media_dir_letterimage_thumbnails, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    @property
    def order_in_letter(self):
        return LetterImage.objects.filter(letter=self.letter, id__lte=self.id).count()

    def __str__(self):
        if self.letter:
            try:
                return f"Image #{self.order_in_letter} of letter: {self.letter.title}"
            except Exception:
                return f"An image of letter: {self.letter.title}"
        else:
            return "An image of a letter"

    def save(self, *args, **kwargs):
        # Must save now, so image is saved before working with it
        super().save(*args, **kwargs)

        try:
            file_extension = self.image.name.split('.')[-1]
            file_format = 'PNG' if file_extension.lower() == 'png' else 'JPEG'

            # Create a thumbnail image file of original image (e.g. for use in list views)
            if self.image_thumbnail:
                self.image_thumbnail.delete(save=False)
            img_thumbnail = Image.open(self.image.path)
            img_thumbnail.thumbnail((890, 890))
            img_thumbnail = ImageOps.exif_transpose(img_thumbnail)  # Rotate to correct orientation
            blob_thumbnail = BytesIO()
            img_thumbnail.save(blob_thumbnail, file_format, optimize=True, quality=80)
            name = os.path.basename(self.image.name).rsplit('.', 1)[0]  # removes extension from main image name
            # Save thumbnail image file
            self.image_thumbnail.save(f'{name}_thumbnail.{file_extension}', File(blob_thumbnail), save=False)
            # Update the object in db - must use update() not save() to avoid unique ID error
            LetterImage.objects.filter(id=self.id).update(
                image_thumbnail=f'{self.media_dir_letterimage_thumbnails}/{name}_thumbnail.{file_extension}'
            )
        except FileNotFoundError:
            pass
        except Exception:
            pass


class LetterPublicTranscription(models.Model):
    """
    A group of letter image transcriptions (created by the public)
    """

    related_name = 'letterpublictranscription'

    letter = models.ForeignKey(Letter, related_name=related_name, on_delete=models.CASCADE)
    person_name = models.CharField(max_length=150, blank=True)
    person_email = models.EmailField(blank=True)
    person_country = models.ForeignKey(SlCountry, blank=True, null=True, on_delete=models.SET_NULL)

    # Admin fields
    approved_by_project_team = models.BooleanField(blank=True, null=True)
    admin_notes = models.TextField(blank=True, null=True)

    # Meta fields
    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    lastupdated_datetime = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    @property
    def transcription_text_full(self):
        return "\n\n\n[next page]\n\n\n".join(
            [t.transcription_text for t in self.letterimagepublictranscription.all()]
        )

    @property
    def transcription_text_brief(self):
        return textwrap.shorten(self.transcription_text_full, width=270, placeholder="...")

    @property
    def order_in_letter(self):
        return LetterPublicTranscription.objects.filter(
            letter=self.letter,
            approved_by_project_team=True,
            created_datetime__lte=self.created_datetime
        ).count()

    def __str__(self):
        text = f"Transcription #{self.order_in_letter} (Submitted "
        text += f"by {self.person_name}, " if self.person_name else ""
        text += f"{str(self.created_datetime)[:16]})"
        return text.strip()


class LetterImagePublicTranscription(models.Model):
    """
    A public transcription of an individual letter image
    """

    related_name = 'letterimagepublictranscription'

    letter_public_transcription = models.ForeignKey(LetterPublicTranscription,
                                                    related_name=related_name,
                                                    on_delete=models.CASCADE)
    letter_image = models.ForeignKey(LetterImage, related_name=related_name, on_delete=models.CASCADE)
    transcription_text = models.TextField()

    @property
    def image_order_in_letter(self):
        return self.letter_image.order_in_letter

    def __str__(self):
        return f"Public transcription of letter image: {self.letter_image}"


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
    gender = models.ForeignKey(SlPersonGender,
                               related_name=related_name,
                               on_delete=models.SET_NULL,
                               blank=True, null=True)
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
        details = f"<strong>Featured in letters:</strong> {self.letterperson_set.count()}<br>"
        details += f"<strong>Gender:</strong> {self.gender.name.capitalize()}<br>" if self.gender else ''
        details += f"<strong>Alternative Name:</strong> {self.alternative_names}<br>" if self.alternative_names else ''
        details += f"<strong>Born:</strong> {self.year_of_birth}<br>" if self.year_of_birth else ''
        details += f"<strong>Died:</strong> {self.year_of_death}<br>" if self.year_of_death else ''
        details += f"<strong>Active from:</strong> {self.year_active_start}<br>" if self.year_active_start else ''
        details += f"<strong>Active until:</strong> {self.year_active_end}<br>" if self.year_active_end else ''
        return details.strip()

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
