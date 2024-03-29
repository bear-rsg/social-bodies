# Generated by Django 3.2.15 on 2022-10-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0007_alter_letter_sent_date_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='transcription_is_public',
            field=models.BooleanField(default=False, help_text='Tick to make this letter available for the public to transcribe through the website'),
        ),
        migrations.AddField(
            model_name='letterimage',
            name='image_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='researchdata/letters-thumbnails'),
        ),
    ]
