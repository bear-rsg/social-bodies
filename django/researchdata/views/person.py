from django.views.generic import (DetailView, ListView)
from django.db.models import Q
from .. import models
from . import common


class PersonDetailView(DetailView):
    """
    Class-based view for person detail template
    """
    template_name = 'researchdata/detail-person.html'
    model = models.Person


class PersonListView(ListView):
    """
    Class-based view for person list template
    """
    template_name = 'researchdata/list-person.html'
    model = models.Person
    paginate_by = 100

    def get_queryset(self):
        # Start with all published objects
        queryset = self.model.objects.filter(admin_published=True)
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

                # FK
                Q(gender__name__icontains=search) |

                # M2M
                Q(title__name__icontains=search) |
                Q(marital_status__name__icontains=search) |
                Q(religion__name__icontains=search) |
                Q(rank__name__icontains=search) |

                # M2M via LetterPerson (limited fields, as this slows it down considerably)
                Q(letterperson__body_part__name__icontains=search) |
                Q(letterperson__bodily_activity__name__icontains=search)
            )
        # Filters
        queryset = common.filter(self.request, queryset)
        # Sort
        queryset = common.sort(self.request, queryset, 'first_name')
        # Return result, showing only distinct
        return queryset.distinct()

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
                'filter_id': f'{common.filter_pre_mm}title',
                'filter_name': 'Title',
                'filter_options': models.SlPersonTitle.objects.all()
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
                'filter_id': f'{common.filter_pre_mm}letterperson__bodily_activity',
                'filter_name': 'Bodily Activity',
                'filter_options': models.SlLetterPersonBodilyActivity.objects.all()
            },
        ]

        return context
