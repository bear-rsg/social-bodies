# Generated by Django 3.2.16 on 2022-12-05 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0017_letter_copyright_holder_untraced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letterimagepublictranscription',
            name='letter_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='letterimagepublictranscription', to='researchdata.letterimage'),
        ),
        migrations.AlterField(
            model_name='letterimagepublictranscription',
            name='letter_public_transcription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='letterimagepublictranscription', to='researchdata.letterpublictranscription'),
        ),
    ]
