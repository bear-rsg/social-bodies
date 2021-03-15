from django.db import migrations
from researchdata import models


def insert_slpersongender(apps, schema_editor):
    """
    Inserts select list objects for SlPersonGender
    """

    names = [
        "male",
        "female",
        "other",
        "unknown"
    ]

    for name in names:
        models.SlPersonGender(name=name).save()


def insert_slpersonmaritalstatus(apps, schema_editor):
    """
    Inserts select list objects for SlPersonMaritalStatus
    """

    names = [
        "married",
        "unmarried",
        "widowed"
    ]

    for name in names:
        models.SlPersonMaritalStatus(name=name).save()


def insert_slpersonrank(apps, schema_editor):
    """
    Inserts select list objects for SlPersonRank
    """

    names = [
        "aristocracy",
        "gentry",
        "professional"
        "upper middling",
        "established middling",
        "lower middling",
        "labouring",
        "dependent poor"
    ]

    for name in names:
        models.SlPersonRank(name=name).save()


def insert_slpersonreligion(apps, schema_editor):
    """
    Inserts select list objects for SlPersonReligion
    """

    names = [
        "catholic",
        "jewish",
        "protestant (conforming)",
        "protestant (non-conforming)",
        "methodist",
        "baptist",
        "unitarian"
    ]

    for name in names:
        models.SlPersonReligion(name=name).save()


def insert_slpersontitle(apps, schema_editor):
    """
    Inserts select list objects for SlPersonTitle
    """

    names = [
        "Duke/Duchess",
        "Marquees/Marchioness",
        "Earl/Countess",
        "Viscount/Viscountess",
        "Baron/Baroness",
        "Baronets",
        "Knight/Dame"
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


def insert_slletterpersonbodypart(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonBodyPart
    """

    names = [
        "leg",
        "arm",
        "head",
        "eyes",
        "brain",
        "teeth",
        "cheeks",
        "hair",
        "ears",
        "stomach",
        "body",
        "whole-body",
        "mind",
        "mouth",
        "face",
        "hands",
        "constitution",
        "teeth",
        "gizzard",
        "lips",
        "nerves",
        "spirits (body part)"
    ]

    for name in names:
        models.SlLetterPersonBodyPart(name=name).save()


def insert_slletterpersonbodilyactivity(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonBodilyActivity
    """

    names = [
        "walking",
        "writing",
        "accident",
        "violence / assault",
        "travel",
        "childbirth",
        "breastfeeding",
        "work",
        "incapacitated",
        "confinement",
        "dancing",
        "death",
        "dining",
        "eating",
        "crying",
        "reading",
        "listening",
        "looking",
        "looking",
        "resting",
        "in bed",
        "sleeping",
        "breathing",
        "smiling",
        "drinking",
        "acting",
        "singing",
        "devotional practice",
        "meditating",
        "fasting",
        "thinking",
        "digesting",
        "cleaning",
        "exercise",
        "kissing",
        "licking",
        "shooting",
        "fishing",
        "horse-riding",
        "sight-seeing",
        "theatre-going",
        "visiting",
        "embracing",
        "gifting"
    ]

    for name in names:
        models.SlLetterPersonBodilyActivity(name=name).save()


def insert_slletterpersonemotion(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonEmotion
    """

    names = [
        "feeling",
        "shame",
        "anger",
        "resentment",
        "happy",
        "pleasure",
        "amused",
        "shock",
        "distress",
        "sorrow",
        "low",
        "regret",
        "apprehension",
        "worried",
        "grief",
        "sympathy",
        "grateful",
        "love",
        "love (romantic)",
        "love (parental)",
        "love (familial)",
        "love (neighbourly)",
        "desire",
        "spirit (immaterial)",
        "affection",
        "unmoved",
        "lack of feeling"
    ]

    for name in names:
        models.SlLetterPersonEmotion(name=name).save()


def insert_slletterpersonimmaterial(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonImmaterial
    """

    names = [
        "mind",
        "distraction",
        "peace",
        "education",
        "thought",
        "slow of mind",
        "confused",
        "memory",
        "soul",
        "sinful",
        "virtuous",
        "duty",
        "personal blessings",
        "faith",
        "self",
        "disposition"
    ]

    for name in names:
        models.SlLetterPersonImmaterial(name=name).save()


def insert_slletterpersonconditionspecificstate(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonConditionSpecificState
    """

    names = [
        "pregnancy",
        "illness",
        "sea-sickness",
        "home-sick",
        "fatigue",
        "fever",
        "scarred",
        "smallpox",
        "cough",
        "gout",
        "insensible",
        "a cold",
        "tired",
        "melancholy",
        "separation"
    ]

    for name in names:
        models.SlLetterPersonConditionSpecificState(name=name).save()


def insert_slletterpersonconditionspecificlifestage(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonConditionSpecificLifeStage
    """

    names = [
        "childhood",
        "youth",
        "ageing",
        "longevity",
        "old age"
    ]

    for name in names:
        models.SlLetterPersonConditionSpecificLifeStage(name=name).save()


def insert_slletterpersonconditiongeneralizedstate(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonConditionGeneralizedState
    """

    names = [
        "well",
        "unwell",
        "health",
        "ill-health",
        "order",
        "disorder",
        "uneasy",
        "easy",
        "safe",
        "fatigue",
        "strong",
        "weak",
        "hurried",
        "active",
        "recovery"
    ]

    for name in names:
        models.SlLetterPersonConditionGeneralizedState(name=name).save()


def insert_slletterpersontreatment(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonTreatment
    """

    names = [
        "medical",
        "care provided by family/kin/household",
        "recipe",
        "regimen",
        "religion",
        "doctor",
        "nurse",
        "midwife",
        "surgery",
        "apothecary",
        "rest",
        "air",
        "exercise",
        "consolation"
    ]

    for name in names:
        models.SlLetterPersonTreatment(name=name).save()


def insert_slletterpersonsensation(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonSensation
    """

    names = [
        "pain",
        "smell",
        "taste",
        "sight",
        "touch",
        "hearing",
        "hot",
        "cold"
    ]

    for name in names:
        models.SlLetterPersonSensation(name=name).save()


def insert_slletterpersoncontext(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonContext
    """

    names = [
        "environment",
        "space",
        "weather",
        "winter",
        "summer",
        "autumn",
        "spring",
        "prison",
        "school",
        "in bed",
        "at home",
        "travel",
        "work",
        "urban",
        "rural"
    ]

    for name in names:
        models.SlLetterPersonContext(name=name).save()


def insert_slletterpersonlocation(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonLocation
    """

    names = [
        "opening",
        "main body",
        "closing",
        "throughout (consistent)",
        "throughout (inconsistent)"
    ]

    for name in names:
        models.SlLetterPersonLocation(name=name).save()


def insert_slletterpersontype(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonType
    """

    names = [
        "reporting",
        "enquiry",
        "advising",
        "response"
    ]

    for name in names:
        models.SlLetterPersonType(name=name).save()


def insert_slletterpersonappearance(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonAppearance
    """

    names = [
        "large",
        "small",
        "shape",
        "build",
        "comportment",
        "complexion",
        "aesthetics",
        "clothing",
        "active",
        "smell",
        "status"
    ]

    for name in names:
        models.SlLetterPersonAppearance(name=name).save()


def insert_slletterpersonrole(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonRole
    """

    names = [
        "motherhood",
        "fatherhood",
        "parenthood",
        "widowhood",
        "courting",
        "marriage",
        "family",
        "siblings",
        "God",
        "business",
        "congregation",
        "apprentice"
    ]

    for name in names:
        models.SlLetterPersonRole(name=name).save()


def insert_slletterpersonestimatedproportionofletter(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonEstimatedProportionOfLetter
    """

    names = [
        "0-20%",
        "21-40%",
        "41-60%",
        "61-80%",
        "81-100%"
    ]

    for name in names:
        models.SlLetterPersonEstimatedProportionOfLetter(name=name).save()


def insert_slletterpersoncommentary(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonCommentary
    """

    names = [
        "happy",
        "humorous",
        "positive",
        "negative",
        "neutral",
        "concerned",
        "apologetic",
        "conflictual",
        "religious",
        "moral",
        "metaphorical",
        "resigned",
        "hopeful"
    ]

    for name in names:
        models.SlLetterPersonCommentary(name=name).save()


def insert_slletterpersonstate(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonState
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
        models.SlLetterPersonState(name=name).save()


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


def insert_slletterpersonrelationshiptype(apps, schema_editor):
    """
    Inserts select list objects for SlLetterPersonRelationshipType
    """

    names = [
        "primary author",
        "secondary author",
        "primary addressee",
        "other"
    ]

    for name in names:
        models.SlLetterPersonRelationshipType(name=name).save()


def insert_slm2mpersonpersonrelationshiptype(apps, schema_editor):
    """
    Inserts select list objects for SlM2MPersonPersonRelationshipType
    """

    names = [
        "parent - child",
        "step-parent - step-child"
        "grandparent - grandchild",
        "siblings",
        "cousins",
        "aunt/uncle - nephew/neice",
        "extended family",
        "neighbours",
        "colleagues",
        "friend",
        "courting",
        "landlord - lodger",
        "master - servant",
        "employer - employee"
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
        migrations.RunPython(insert_slpersonmaritalstatus),
        migrations.RunPython(insert_slpersonrank),
        migrations.RunPython(insert_slpersonreligion),
        migrations.RunPython(insert_slpersontitle),
        # Letter SL tables
        migrations.RunPython(insert_sllettercollection),
        # Letter Person related tables
        migrations.RunPython(insert_slletterpersonlocation),
        migrations.RunPython(insert_slletterpersontype),
        # Letter Person SL tables
        migrations.RunPython(insert_slletterpersonbodypart),
        migrations.RunPython(insert_slletterpersonbodilyactivity),
        migrations.RunPython(insert_slletterpersonemotion),
        migrations.RunPython(insert_slletterpersonimmaterial),
        migrations.RunPython(insert_slletterpersonconditionspecificstate),
        migrations.RunPython(insert_slletterpersonconditionspecificlifestage),
        migrations.RunPython(insert_slletterpersonconditiongeneralizedstate),
        migrations.RunPython(insert_slletterpersontreatment),
        migrations.RunPython(insert_slletterpersonsensation),
        migrations.RunPython(insert_slletterpersoncontext),
        migrations.RunPython(insert_slletterpersonappearance),
        migrations.RunPython(insert_slletterpersonrole),
        migrations.RunPython(insert_slletterpersonestimatedproportionofletter),
        migrations.RunPython(insert_slletterpersoncommentary),
        migrations.RunPython(insert_slletterpersonstate),
        # Many to Many SL tables
        migrations.RunPython(insert_slm2mletterletterrelationshiptype),
        migrations.RunPython(insert_slletterpersonrelationshiptype),
        migrations.RunPython(insert_slm2mpersonpersonrelationshiptype)
    ]
