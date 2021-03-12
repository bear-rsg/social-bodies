# Generated by Django 3.1.7 on 2021-03-12 10:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.TextField(blank=True, null=True)),
                ('item_number', models.CharField(blank=True, max_length=255, null=True)),
                ('permission_reproduce_text', models.BooleanField(blank=True, null=True)),
                ('permission_reproduce_image', models.BooleanField(blank=True, null=True)),
                ('transcription_plain', models.TextField(blank=True, null=True)),
                ('transcription_normalized', models.TextField(blank=True, null=True)),
                ('sent_date_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1500), django.core.validators.MaxValueValidator(2000)])),
                ('sent_date_month', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('sent_date_day', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)])),
                ('sent_date_as_given', models.CharField(blank=True, max_length=255, null=True)),
                ('sent_time', models.CharField(blank=True, max_length=255, null=True)),
                ('sent_from_location', models.TextField(blank=True, null=True)),
                ('sent_to_location', models.TextField(blank=True, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='letter_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='letter_lastupdated_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Updated By')),
            ],
        ),
        migrations.CreateModel(
            name='M2MPersonPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SlGeneric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SlLetterCollection',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonAppearance',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonBodilyActivity',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonBodyPart',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonCommentary',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonConditionGeneralizedState',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonConditionSpecificLifeStage',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonConditionSpecificState',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonContext',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonEmotion',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonEstimatedProportionOfLetter',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonImmaterial',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonLocation',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonRelationshipType',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonRole',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonSensation',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonState',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonTreatment',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterPersonType',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlLetterRepository',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlM2MLetterLetterRelationshipType',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlM2MPersonPersonRelationshipType',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlPersonGender',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlPersonMaritalStatus',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlPersonRank',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlPersonReligion',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='SlPersonTitle',
            fields=[
                ('slgeneric_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='researchdata.slgeneric')),
            ],
            bases=('researchdata.slgeneric',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('alternative_spelling_of_name', models.CharField(blank=True, max_length=255, null=True)),
                ('alternative_names', models.CharField(blank=True, max_length=255, null=True)),
                ('year_of_birth', models.IntegerField(blank=True, null=True)),
                ('year_of_death', models.IntegerField(blank=True, null=True)),
                ('year_active_start', models.IntegerField(blank=True, null=True)),
                ('year_active_end', models.IntegerField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='person_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='person_lastupdated_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Updated By')),
                ('person', models.ManyToManyField(blank=True, related_name='_person_person_+', through='researchdata.M2MPersonPerson', to='researchdata.Person')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.slpersongender')),
                ('marital_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.slpersonmaritalstatus')),
                ('rank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.slpersonrank')),
                ('religion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.slpersonreligion')),
                ('title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.slpersontitle')),
            ],
        ),
        migrations.AddField(
            model_name='m2mpersonperson',
            name='person_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_1', to='researchdata.person'),
        ),
        migrations.AddField(
            model_name='m2mpersonperson',
            name='person_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_2', to='researchdata.person'),
        ),
        migrations.CreateModel(
            name='M2MLetterLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='letter_1', to='researchdata.letter')),
                ('letter_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='letter_2', to='researchdata.letter')),
                ('relationship_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='researchdata.slm2mletterletterrelationshiptype')),
            ],
        ),
        migrations.CreateModel(
            name='LetterImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='researchdata/letters')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('letter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='researchdata.letter')),
            ],
        ),
        migrations.AddField(
            model_name='letter',
            name='letter',
            field=models.ManyToManyField(blank=True, related_name='_letter_letter_+', through='researchdata.M2MLetterLetter', to='researchdata.Letter'),
        ),
        migrations.AddField(
            model_name='m2mpersonperson',
            name='relationship_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='researchdata.slm2mpersonpersonrelationshiptype'),
        ),
        migrations.AddField(
            model_name='letter',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.sllettercollection'),
        ),
        migrations.AddField(
            model_name='letter',
            name='commentary',
            field=models.ManyToManyField(blank=True, related_name='letter', to='researchdata.SlLetterPersonCommentary'),
        ),
        migrations.AddField(
            model_name='letter',
            name='content_type',
            field=models.ManyToManyField(blank=True, related_name='letter', to='researchdata.SlLetterPersonType'),
        ),
        migrations.AddField(
            model_name='letter',
            name='estimated_proportion_of_letter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.slletterpersonestimatedproportionofletter'),
        ),
        migrations.AddField(
            model_name='letter',
            name='location',
            field=models.ManyToManyField(blank=True, related_name='letter', to='researchdata.SlLetterPersonLocation'),
        ),
        migrations.AddField(
            model_name='letter',
            name='repository',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.slletterrepository'),
        ),
        migrations.AddField(
            model_name='letter',
            name='state',
            field=models.ManyToManyField(blank=True, related_name='letter', to='researchdata.SlLetterPersonState'),
        ),
        migrations.CreateModel(
            name='LetterPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_form_of_address', models.CharField(blank=True, max_length=255, null=True)),
                ('person_other', models.TextField(blank=True, null=True, verbose_name='Person/People (if not specified in Person table)')),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('admin_published', models.BooleanField(default=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('lastupdated_datetime', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='letterperson_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Created By')),
                ('lastupdated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='letterperson_lastupdated_by', to=settings.AUTH_USER_MODEL, verbose_name='Last Updated By')),
                ('letter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='researchdata.letter')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='researchdata.person')),
                ('appearance', models.ManyToManyField(blank=True, related_name='letterperson', to='researchdata.SlLetterPersonAppearance')),
                ('bodily_activity', models.ManyToManyField(blank=True, related_name='letterperson', to='researchdata.SlLetterPersonBodilyActivity')),
                ('body_part', models.ManyToManyField(blank=True, related_name='letterperson', to='researchdata.SlLetterPersonBodyPart')),
                ('condition_generalized_state', models.ManyToManyField(blank=True, related_name='letterperson', to='researchdata.SlLetterPersonConditionGeneralizedState')),
                ('condition_specific_life_stage', models.ManyToManyField(blank=True, related_name='letterperson', to='researchdata.SlLetterPersonConditionSpecificLifeStage')),
                ('condition_specific_state', models.ManyToManyField(blank=True, related_name='letterperson', to='researchdata.SlLetterPersonConditionSpecificState')),
                ('context', models.ManyToManyField(blank=True, related_name='letterperson', to='researchdata.SlLetterPersonContext')),
                ('emotion', models.ManyToManyField(blank=True, related_name='letterperson', to='researchdata.SlLetterPersonEmotion')),
                ('immaterial', models.ManyToManyField(blank=True, related_name='letterperson', to='researchdata.SlLetterPersonImmaterial')),
                ('person_letter_relationship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='researchdata.slletterpersonrelationshiptype')),
                ('roles', models.ManyToManyField(blank=True, related_name='letterperson', to='researchdata.SlLetterPersonRole')),
                ('sensation', models.ManyToManyField(blank=True, related_name='letterperson', to='researchdata.SlLetterPersonSensation')),
                ('treatment', models.ManyToManyField(blank=True, related_name='letterperson', to='researchdata.SlLetterPersonTreatment')),
            ],
            options={
                'unique_together': {('letter', 'person_other'), ('letter', 'person')},
            },
        ),
    ]
