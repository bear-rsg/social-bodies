from django.views.generic import (DetailView, ListView)
from django.db.models.functions import Concat
from django.db.models import CharField, Value, Q
from django.urls import reverse
from .. import models
from . import common


class PersonDetailView(DetailView):
    """
    Class-based view for person detail template
    """
    template_name = 'researchdata/detail-person.html'
    queryset = models.Person.objects.filter(admin_published=True)\
        .prefetch_related('person', 'letterperson_set',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Admin URL
        context['admin_url'] = reverse('admin:researchdata_person_change', args=[self.object.id])

        # Details
        context['details'] = common.details_section_visibility([
            [
                {'label': 'First Name', 'value': self.object.first_name},
                {'label': 'Middle Name', 'value': self.object.middle_name},
                {'label': 'Last Name', 'value': self.object.last_name},
                {'label': 'Alternative Spelling of Name Number', 'value': self.object.alternative_spelling_of_name},
                {'label': 'Alternative Names', 'value': self.object.alternative_names},
                {'label': 'Year of Birth', 'value': self.object.year_of_birth},
                {'label': 'Year of Death', 'value': self.object.year_of_death},
                {'label': 'Years Active (from)', 'value': self.object.year_active_start},
                {'label': 'Years Active (to)', 'value': self.object.year_active_end},
                {'label': 'Gender', 'value': self.object.gender},
                {'label': 'Title', 'value': common.html_details_list_items(self.object.title.all())},
                {'label': 'Marital Status', 'value': common.html_details_list_items(self.object.marital_status.all())},
                {'label': 'Religion', 'value': common.html_details_list_items(self.object.religion.all())},
                {'label': 'Rank', 'value': common.html_details_list_items(self.object.rank.all())},
                {'label': 'Occupation', 'value': self.object.occupation},
            ],
        ])

        context['letterperson_details'] = common.letterperson_details(self.object)

        return context


class PersonListView(ListView):
    """
    Class-based view for person list template
    """
    template_name = 'researchdata/list-person.html'
    model = models.Person
    paginate_by = 60

    def get_queryset(self):
        # Start with all published objects
        queryset = self.model.objects.filter(admin_published=True)
        # Add annotations for improved searching
        # name_first_last
        queryset = queryset.annotate(
            name_first_last=Concat('first_name', Value(' '), 'last_name',
                                   output_field=CharField()))
        # name_full
        queryset = queryset.annotate(
            name_full=Concat('first_name', Value(' '), 'middle_name', Value(' '), 'last_name',
                             output_field=CharField()))

        # Search
        search = self.request.GET.get('search', '')
        if search != '':
            queryset = queryset.filter(
                Q(first_name__icontains=search) |
                Q(middle_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(alternative_spelling_of_name__icontains=search) |
                Q(alternative_names__icontains=search) |
                Q(year_of_birth__icontains=search) |
                Q(year_of_death__icontains=search) |
                Q(year_active_start__icontains=search) |
                Q(year_active_end__icontains=search) |
                Q(occupation__icontains=search) |

                # Annotation fields
                Q(name_first_last__icontains=search) |
                Q(name_full__icontains=search) |

                # FK
                Q(gender__name__icontains=search) |

                # M2M
                Q(title__name__icontains=search) |
                Q(marital_status__name__icontains=search) |
                Q(religion__name__icontains=search) |
                Q(rank__name__icontains=search) |

                # M2M via LetterPerson
                Q(letterperson__body_part__name__icontains=search) |
                Q(letterperson__bodily_activity__name__icontains=search) |
                Q(letterperson__appearance__name__icontains=search) |
                Q(letterperson__emotion__name__icontains=search) |
                Q(letterperson__sensation__name__icontains=search) |
                # Following are commented out for performance reasons (too many = too slow)
                # Q(letterperson__condition_specific_state__name__icontains=search) |
                # Q(letterperson__immaterial__name__icontains=search) |
                # Q(letterperson__condition_specific_life_stage__name__icontains=search) |
                # Q(letterperson__condition_generalized_state__name__icontains=search) |
                # Q(letterperson__treatment__name__icontains=search) |
                # Q(letterperson__roles__name__icontains=search) |
                # Q(letterperson__context__name__icontains=search) |
                # Q(letterperson__state__name__icontains=search) |

                # M2M via LetterPerson > Letter
                Q(letterperson__letter__letter_type__name__icontains=search) |
                Q(letterperson__letter__commentary__name__icontains=search) |
                Q(letterperson__letter__location__name__icontains=search)
            )
        # Filters
        queryset = common.filter(self.request, queryset)
        # Sort
        queryset = common.sort(self.request, queryset, 'first_name')
        # Return result, showing only distinct
        return queryset.distinct()\
            .prefetch_related('letterperson_set').select_related('gender')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Options: Filters
        context['filters'] = [
            {
                'filter_id': f'{common.filter_pre_mm}gender',
                'filter_name': 'Gender',
                'filter_options': models.SlPersonGender.objects.all()
            },
            {
                'filter_id': f'{common.filter_pre_mm}marital_status',
                'filter_name': 'Marital Status',
                'filter_options': models.SlPersonMaritalStatus.objects.all()
            },
            {
                'filter_id': f'{common.filter_pre_mm}religion',
                'filter_name': 'Religion',
                'filter_options': models.SlPersonReligion.objects.all()
            },
            {
                'filter_id': f'{common.filter_pre_mm}rank',
                'filter_name': 'Rank',
                'filter_options': models.SlPersonRank.objects.all()
            },
            {
                'filter_id': f'{common.filter_pre_gt}year_active_start',
                'filter_classes': common.filter_pre_gt,
                'filter_name': 'Year Active Start (from)',
                'filter_options': models.Person.objects.filter(year_active_start__gt=1000).exclude(year_active_start__isnull=True).distinct().order_by('year_active_start').values_list('year_active_start', flat=True),  # NOQA
                'valueSameAsText': True
            },
            {
                'filter_id': f'{common.filter_pre_lt}year_active_start',
                'filter_classes': common.filter_pre_lt,
                'filter_name': 'Year Active Start (to)',
                'filter_options': models.Person.objects.filter(year_active_start__gt=1000).exclude(year_active_start__isnull=True).distinct().order_by('year_active_start').values_list('year_active_start', flat=True),  # NOQA
                'valueSameAsText': True
            },
            {
                'filter_id': f'{common.filter_pre_gt}year_active_end',
                'filter_classes': common.filter_pre_gt,
                'filter_name': 'Year Active End (from)',
                'filter_options': models.Person.objects.filter(year_active_end__gt=1000).exclude(year_active_end__isnull=True).distinct().order_by('year_active_end').values_list('year_active_end', flat=True),  # NOQA
                'valueSameAsText': True
            },
            {
                'filter_id': f'{common.filter_pre_lt}year_active_end',
                'filter_classes': common.filter_pre_lt,
                'filter_name': 'Year Active End (to)',
                'filter_options': models.Person.objects.filter(year_active_end__gt=1000).exclude(year_active_end__isnull=True).distinct().order_by('year_active_end').values_list('year_active_end', flat=True),  # NOQA
                'valueSameAsText': True
            }
        ]

        return context
