# Generated by Django 3.2.16 on 2022-11-02 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0012_permissions_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slgeneric',
            options={'ordering': ['name', 'id']},
        ),
        migrations.AlterField(
            model_name='letter',
            name='transcription_is_public',
            field=models.BooleanField(default=False, help_text='Tick to make this letter available for general users to transcribe through the public website', verbose_name='available for public transcription'),
        ),
    ]
