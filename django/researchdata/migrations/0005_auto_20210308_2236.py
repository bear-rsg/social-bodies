# Generated by Django 3.1.7 on 2021-03-08 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0004_auto_20210308_2127'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lettercontent',
            unique_together={('letter', 'person_other')},
        ),
    ]
