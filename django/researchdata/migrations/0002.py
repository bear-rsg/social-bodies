from django.db import migrations
from researchdata import models


def insert_slpersongender(apps, schema_editor):
    """
    Inserts select list objects for SlPersonGender
    """

    names = [
        "Male",
        "Female",
        "Other",
        "Unknown"
    ]

    for name in names:
        models.SlPersonGender(name=name).save()


def insert_slpersonrank(apps, schema_editor):
    """
    Inserts select list objects for SlPersonRank
    """

    names = [
        "Aristocracy",
        "Gentry",
        "Upper middling",
        "Established middling",
        "Lower middling",
        "Labouring",
        "Dependent poor"
    ]

    for name in names:
        models.SlPersonRank(name=name).save()


def insert_slpersonreligion(apps, schema_editor):
    """
    Inserts select list objects for SlPersonReligion
    """

    names = [
        "Catholic",
        "Jewish",
        "Protestant (conforming)",
        "Protestant (non-conforming)",
        "Methodist",
        "Baptist",
        "Unitarian"
    ]

    for name in names:
        models.SlPersonReligion(name=name).save()


def insert_slpersontitle(apps, schema_editor):
    """
    Inserts select list objects for SlPersonTitle
    """

    names = [
        "Dr",
        "Miss",
        "Mr",
        "Mrs",
        "Ms"
    ]

    for name in names:
        models.SlPersonTitle(name=name).save()


def insert_sllettercollection(apps, schema_editor):
    """
    Inserts select list objects for SlLetterCollection
    """

    names = [
        "1",
        "2",
        "3",
        "4",
        "5"
    ]

    for name in names:
        models.SlLetterCollection(name=name).save()


def insert_lettercontentlocation(apps, schema_editor):
    """
    Inserts select list objects for LetterContentLocation
    """

    names = [
        "opening",
        "main body",
        "closing",
        "throughout (consistent)",
        "throughout (inconsistent)"
    ]

    for name in names:
        models.LetterContentLocation(name=name).save()



def insert_lettercontenttype(apps, schema_editor):
    """
    Inserts select list objects for LetterContentType
    """

    names = [
        "1",
        "2",
        "3",
        "4",
        "5"
    ]

    for name in names:
        models.LetterContentType(name=name).save()


def insert_sllettercontentbodypart(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentBodyPart
    """

    names = [
        "eyes",
        "brain",
        "teeth",
        "cheeks",
        "hair",
        "leg",
        "arm",
        "head",
        "body",
        "whole-body",
        "mind",
        "mouth",
        "face",
        "hands",
        "constitution",
        "nerves",
        "gizzard",
        "lips"
    ]

    for name in names:
        models.SlLetterContentBodyPart(name=name).save()


def insert_sllettercontentbodilyactivity(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentBodilyActivity
    """

    names = [
        "walking",
        "writing",
        "accident",
        "violence",
        "assault",
        "dining",
        "eating",
        "crying",
        "reading",
        "hearing",
        "seeing",
        "breastfeeding",
        "work",
        "incapacitated",
        "confinement",
        "lying-down",
        "dying",
        "being in bed",
        "sleeping",
        "breating",
        "smiling",
        "drinking"
    ]

    for name in names:
        models.SlLetterContentBodilyActivity(name=name).save()


def insert_sllettercontentemotion(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentEmotion
    """

    names = [
        "spirit",
        "love",
        "shame",
        "anger",
        "resentment",
        "amused",
        "shock",
        "sorrow",
        "cherishing",
        "lamenting",
        "low",
        "happy",
        "peace",
        "regret",
        "sincere",
        "dejected",
        "melancholy",
        "apprehension"
    ]

    for name in names:
        models.SlLetterContentEmotion(name=name).save()


def insert_sllettercontentimmaterial(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentImmaterial
    """

    names = [
        "mind",
        "soul",
        "self",
        "unmoved",
        "feeling",
        "settled",
        "distressed",
        "countenance",
        "uneasy",
        "safe",
        "pleasure",
        "charity",
        "duty",
        "gloomy",
        "consolation"
    ]

    for name in names:
        models.SlLetterContentImmaterial(name=name).save()


def insert_sllettercontentcondition(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentCondition
    """

    names = [
        "pregnancy",
        "childhood",
        "illness",
        "health",
        "death"
    ]

    for name in names:
        models.SlLetterContentCondition(name=name).save()


def insert_sllettercontenttreatment(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentTreatment
    """

    names = [
        "medical",
        "care",
        "recipe",
        "regimen"
    ]

    for name in names:
        models.SlLetterContentTreatment(name=name).save()


def insert_sllettercontentsensation(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentSensation
    """

    names = [
        "pain",
        "smell",
        "taste",
        "sight",
        "touch"
    ]

    for name in names:
        models.SlLetterContentSensation(name=name).save()


def insert_sllettercontentcontext(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentContext
    """

    names = [
        "environment",
        "space",
        "weather"
    ]

    for name in names:
        models.SlLetterContentContext(name=name).save()


def insert_sllettercontentappearance(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentAppearance
    """

    names = [
        "size",
        "shape",
        "build",
        "complexion",
        "aesthetics"
    ]

    for name in names:
        models.SlLetterContentAppearance(name=name).save()


def insert_sllettercontentrole(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentRole
    """

    names = [
        "motherhood",
        "widowhood",
        "apprentice"
    ]

    for name in names:
        models.SlLetterContentRole(name=name).save()


def insert_sllettercontentestimatedproportionofletter(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentEstimatedProportionOfLetter
    """

    names = [
        "0-20%",
        "21-40%",
        "41-60%",
        "61-80%",
        "81-100%"
    ]

    for name in names:
        models.SlLetterContentEstimatedProportionOfLetter(name=name).save()


def insert_sllettercontentcommentary(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentCommentary
    """

    names = [
        "worried",
        "happy",
        "humorous",
        "sympathetic"
    ]

    for name in names:
        models.SlLetterContentCommentary(name=name).save()


def insert_sllettercontentstate(apps, schema_editor):
    """
    Inserts select list objects for SlLetterContentState
    """

    names = [
        "health - improving",
        "health - worsening",
        "health - unchanged",
        "body - improving",
        "body - worsening",
        "body - unchanged",
        "mind - improving",
        "mind - worsening",
        "mind - unchanged"
    ]

    for name in names:
        models.SlLetterContentState(name=name).save()


def insert_slm2mletterletterrelationshiptype(apps, schema_editor):
    """
    Inserts select list objects for SlM2MLetterLetterRelationshipType
    """

    names = [
        "conversation",
        "event",
        "familial"
    ]

    for name in names:
        models.SlM2MLetterLetterRelationshipType(name=name).save()


def insert_slm2mletterpersonrelationshiptype(apps, schema_editor):
    """
    Inserts select list objects for SlM2MLetterPersonRelationshipType
    """

    names = [
        "primary author",
        "secondary author",
        "primary addressee",
        "other"
    ]

    for name in names:
        models.SlM2MLetterPersonRelationshipType(name=name).save()


def insert_slm2mpersonpersonrelationshiptype(apps, schema_editor):
    """
    Inserts select list objects for SlM2MPersonPersonRelationshipType
    """

    names = [
        "parent - child",
        "grandparent - grandchild",
        "siblings",
        "cousins",
        "aunt/uncle - nephew/neice",
        "extended family",
        "neighbours",
        "colleagues"
    ]

    for name in names:
        models.SlM2MPersonPersonRelationshipType(name=name).save()


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0001_initial'),
    ]

    operations = [
        # Person SL tables
        migrations.RunPython(insert_slpersongender),
        migrations.RunPython(insert_slpersonrank),
        migrations.RunPython(insert_slpersonreligion),
        migrations.RunPython(insert_slpersontitle),
        # Letter SL tables
        migrations.RunPython(insert_sllettercollection),
        # Letter Content related tables
        migrations.RunPython(insert_lettercontentlocation),
        migrations.RunPython(insert_lettercontenttype),
        # Letter Content SL tables
        migrations.RunPython(insert_sllettercontentbodypart),
        migrations.RunPython(insert_sllettercontentbodilyactivity),
        migrations.RunPython(insert_sllettercontentemotion),
        migrations.RunPython(insert_sllettercontentimmaterial),
        migrations.RunPython(insert_sllettercontentcondition),
        migrations.RunPython(insert_sllettercontenttreatment),
        migrations.RunPython(insert_sllettercontentsensation),
        migrations.RunPython(insert_sllettercontentcontext),
        migrations.RunPython(insert_sllettercontentappearance),
        migrations.RunPython(insert_sllettercontentrole),
        migrations.RunPython(insert_sllettercontentestimatedproportionofletter),
        migrations.RunPython(insert_sllettercontentcommentary),
        migrations.RunPython(insert_sllettercontentstate),
        # Many to Many SL tables
        migrations.RunPython(insert_slm2mletterletterrelationshiptype),
        migrations.RunPython(insert_slm2mletterpersonrelationshiptype),
        migrations.RunPython(insert_slm2mpersonpersonrelationshiptype)
    ]
