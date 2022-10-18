from django.views.generic import (DetailView, ListView)
from django.urls import reverse
from django.db.models import Q
from .. import models
from . import common


class LetterDetailView(DetailView):
    """
    Class-based view for letter detail template
    """
    template_name = 'researchdata/detail-letter.html'
    queryset = models.Letter.objects.filter(admin_published=True,
                                            permission_reproduce_text=True,
                                            permission_reproduce_image=True)\
        .prefetch_related('letter', 'letterimage_set', 'letterperson_set')\
        .select_related('collection', 'repository')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Admin URL
        context['admin_url'] = reverse('admin:researchdata_letter_change', args=[self.object.id])

        # Details
        context['details'] = common.details_section_visibility([
            [
                {'label': 'Title', 'value': self.object.title},
                {'label': 'Summary', 'value': self.object.summary},
                {'label': 'Collection', 'value': self.object.collection},
                {'label': 'Item Number', 'value': self.object.item_number},
                {'label': 'Repository', 'value': self.object.repository},
                {'label': 'Sent Date (year)', 'value': self.object.sent_date_year},
                {'label': 'Sent Date (month)', 'value': self.object.sent_date_month},
                {'label': 'Sent Date (day)', 'value': self.object.sent_date_day},
                {'label': 'Sent Date is Approximate', 'value': self.object.sent_date_is_approximate},
                {'label': 'Sent Date as Given', 'value': self.object.sent_date_as_given},
                {'label': 'Sent Time', 'value': self.object.sent_time},
                {'label': 'Location: Sent from', 'value': self.object.sent_from_location},
                {'label': 'Location: Sent to', 'value': self.object.sent_to_location},
                {'label': 'Letter Type', 'value': common.html_details_list_items(self.object.letter_type.all())},
                {'label': 'Commentary', 'value': common.html_details_list_items(self.object.commentary.all())},
                {'label': 'Location', 'value': common.html_details_list_items(self.object.location.all())},
                {'label': 'Estimated Proportion of the Letter', 'value': self.object.estimated_proportion_of_letter},
            ],
        ])

        context['letterperson_details'] = common.letterperson_details(self.object)

        return context


class LetterListView(ListView):
    """
    Class-based view for letter list template
    """
    template_name = 'researchdata/list-letter.html'
    model = models.Letter
    paginate_by = 60

    def get_queryset(self):
        # Start with all published objects
        queryset = self.model.objects.filter(admin_published=True)
        # Hide all letter that don't have permission to share text/images
        queryset = queryset.filter(permission_reproduce_text=True, permission_reproduce_image=True)
        # Search
        search = self.request.GET.get('search', '')
        if search != '':
            queryset = queryset.prefetch_related('letterperson_set', 'letter_type', 'collection', 'location').filter(
                Q(id=search) |
                Q(title__icontains=search) |
                Q(summary__icontains=search) |
                Q(transcription_plain__icontains=search) |
                Q(transcription_normalized__icontains=search) |
                Q(sent_date_year__icontains=search) |
                Q(sent_date_month__icontains=search) |
                Q(sent_date_day__icontains=search) |
                Q(sent_date_as_given__icontains=search) |
                Q(sent_time__icontains=search) |
                Q(sent_from_location__icontains=search) |
                Q(sent_to_location__icontains=search) |

                # FK
                Q(collection__name__icontains=search) |
                Q(repository__name__icontains=search) |
                Q(estimated_proportion_of_letter__name__icontains=search) |

                # M2M
                Q(letter_type__name__icontains=search) |
                Q(commentary__name__icontains=search) |
                Q(location__name__icontains=search) |

                # M2M via LetterPerson (limited fields, as this slows it Down considerably)
                Q(letterperson__body_part__name__icontains=search) |
                Q(letterperson__bodily_activity__name__icontains=search)
            )
        # Filters
        queryset = common.filter(self.request, queryset)
        # Sort
        queryset = common.sort(self.request, queryset, 'title')
        # Return result, showing only distinct and use prefetch for improved performance
        return queryset.distinct()\
            .prefetch_related('letterimage_set', 'letterperson_set')\
            .select_related('collection', 'repository')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filter_pre'] = common.filter_pre

        # Options: Filters
        context['filters'] = [
            {
                'filter_id': f'{common.filter_pre_mm}collection',
                'filter_name': 'Collection',
                'filter_options': models.SlLetterCollection.objects.all()
            },
            {
                'filter_id': f'{common.filter_pre_mm}repository',
                'filter_name': 'Repository',
                'filter_options': models.SlLetterRepository.objects.all()
            },
            {
                'filter_id': f'{common.filter_pre_mm}letter_type',
                'filter_name': 'Letter Type',
                'filter_options': models.SlLetterType.objects.all()
            },
            {
                'filter_id': f'{common.filter_pre_mm}commentary',
                'filter_name': 'Commentary',
                'filter_options': models.SlLetterCommentary.objects.all()
            },
            {
                'filter_id': f'{common.filter_pre_mm}location',
                'filter_name': 'Location',
                'filter_options': models.SlLetterLocation.objects.all()
            },
            {
                'filter_id': f'{common.filter_pre_mm}letterperson__bodily_activity',
                'filter_name': 'Bodily Activity',
                'filter_options': models.SlLetterPersonBodilyActivity.objects.all()
            },
        ]

        return context
