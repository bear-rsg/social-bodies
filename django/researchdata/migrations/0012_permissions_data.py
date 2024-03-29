from django.db import migrations
from researchdata import models


def update_letter_admin_published(apps, schema_editor):
    """
    All letters to have 'admin_published' set to False
    """

    models.Letter.objects.all().update(admin_published=False)


def update_letter_permissions(apps, schema_editor):
    """
    Both letter permission fields (permission_reproduce_text and permission_reproduce_image)
    should have values set to NULL if they were previously set to NULL
    prior to the latest migration.
    """

    permission_text_exclude = [29, 34, 35, 36, 37, 42, 43, 44, 45, 46, 47, 128, 129, 130, 163, 564, 565, 566, 567, 568, 569, 570, 573, 574, 575, 576, 578, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 651, 654, 655, 656, 657, 658, 660, 661, 662, 663, 665, 666, 668, 669, 670, 671, 673, 674, 675, 676, 677, 678, 679, 680, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 698, 699, 702, 703, 704, 705, 707, 708, 709, 710, 711, 713, 714, 715, 716, 718, 719, 720, 727, 728, 729, 730, 731, 732, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 760, 783, 784, 786, 787, 788, 790, 791, 795, 796, 797, 798, 799, 800, 801, 802, 804, 806, 807, 809, 810, 811, 813, 814, 816, 825, 827, 828, 839, 840, 841, 842, 846, 847, 851, 852, 853, 854, 855, 856, 857, 858, 863, 865, 866, 868, 869, 870, 871, 872, 873, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 899, 900, 901, 902, 920, 921, 924, 927, 928, 929, 930, 932, 934, 935, 936, 937, 938, 939, 940, 941, 942, 946, 948, 949, 950, 955, 956, 957, 958, 959, 966, 968, 970, 971, 975, 978, 979, 983, 1351, 1378, 1379, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1392, 1465, 1466, 1467, 1470, 1471, 1472, 1486, 1487, 1488, 1489, 1502, 1503, 1505, 1506, 1631, 1632, 1633, 1634, 1635, 1637, 1638, 1640, 1642, 1643, 1645, 1646, 1648, 1650, 1652, 1653, 1736, 1737, 1738, 1739, 1740, 1741, 1767, 1768, 1769, 1770, 1771, 1772, 1773, 1774, 1775, 1952, 1953, 1968, 1969, 1970, 1971]  # NOQA

    # Set permission_reproduce_text to None for all objects apart from those listed above
    models.Letter.objects.exclude(id__in=permission_text_exclude).update(
        permission_reproduce_text=None
    )

    permission_image_exclude = [29, 34, 35, 36, 37, 42, 43, 44, 45, 46, 47, 651, 655, 698, 718, 742, 743, 744, 745, 746, 747, 760, 795, 796, 797, 798, 799, 800, 801, 802, 804, 806, 807, 809, 810, 811, 813, 814, 816, 825, 827, 828, 839, 840, 841, 842, 846, 847, 851, 852, 853, 854, 855, 856, 857, 858, 863, 865, 866, 868, 869, 870, 871, 872, 873, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 899, 900, 901, 902, 920, 921, 924, 927, 928, 929, 930, 932, 934, 935, 936, 937, 938, 939, 940, 941, 942, 946, 948, 949, 950, 955, 956, 957, 958, 959, 966, 968, 970, 971, 975, 978, 979, 983, 1351, 1392, 1465, 1466, 1467, 1470, 1471, 1472, 1486, 1487, 1488, 1489, 1502, 1503, 1505, 1506, 1631, 1632, 1633, 1634, 1635, 1637, 1638, 1640, 1642, 1643, 1645, 1646, 1648, 1650, 1652, 1653, 1736, 1737, 1738, 1739, 1740, 1741, 1767, 1768, 1769, 1770, 1771, 1772, 1773, 1774, 1775, 129, 130, 163, 166, 167, 168, 169, 170, 171, 172, 173, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 654, 656, 657, 658, 660, 661, 662, 663, 665, 666, 668, 669, 670, 671, 673, 674, 675, 676, 677, 678, 679, 680, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 699, 702, 703, 704, 705, 707, 708, 709, 710, 711, 713, 714, 715, 716, 719, 720, 727, 728, 729, 730, 731, 732, 737, 738, 739, 740, 741, 748, 749, 750, 751, 752, 753, 754, 755, 783, 784, 786, 787, 788, 790, 791, 1952, 1953, 1968, 1969, 1970, 1971]  # NOQA

    # Set permission_reproduce_image to None for all objects apart from those listed above
    models.Letter.objects.exclude(id__in=permission_image_exclude).update(
        permission_reproduce_image=None
    )


class Migration(migrations.Migration):

    dependencies = [
        ('researchdata', '0011_auto_20221021_1044'),
    ]

    operations = [
        migrations.RunPython(update_letter_permissions),
        migrations.RunPython(update_letter_admin_published),
    ]
