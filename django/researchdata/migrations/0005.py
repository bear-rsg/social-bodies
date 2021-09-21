from django.db import migrations
from researchdata import models


def insert_slletterpersongender(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonGender
    """

    names = [
        "male",
        "female",
        "both"
    ]

    for name in names:
        models.SlLetterPersonGender(name=name).save()


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_slletterpersongender)
    ]
