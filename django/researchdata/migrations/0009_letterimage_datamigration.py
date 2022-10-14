from django.db import migrations
from researchdata import models


def trigger_save_letterimage(apps, schema_editor):
    """
    Executes the save() method on all existing LetterImages,
    as this is needed to trigger the generation of thumbnail images
    for all existing LetterImages as per the changes made in
    migration: 0008_letterimage_image_thumbnail
    """

    for obj in models.LetterImage.objects.all():
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0008_auto_20221014_1006'),
    ]

    operations = [
        migrations.RunPython(trigger_save_letterimage)
    ]
