from django.views.generic import (DetailView, ListView, RedirectView, TemplateView)
from django.urls import reverse
from django.db.models import Q, Count
from django.core.exceptions import FieldError
from .. import models
from . import common


def filter_options_limit_to_published_related_letters(objects):
    """
    Only include filter options in select lists if selecting them will show items
    E.g. if there are published letters that belong to each filter
    """

    # If has a direct relationship to Letter model (e.g. a direct FK field in Letter model)
    try:
        return objects.annotate(
            published_letters_count=Count('related_letter', filter=Q(related_letter__admin_published=True))
        ).filter(published_letters_count__gt=0)
    # If has a relationship to Letter model through LetterPerson (e.g. a direct M2M field in LetterPerson model)
    except FieldError:
        return objects.annotate(
            published_letters_count=Count('letterperson__letter', filter=Q(letterperson__letter__admin_published=True))
        ).filter(published_letters_count__gt=0)


class LetterDetailView(DetailView):
    """
    Class-based view for letter detail template
    """
    template_name = 'researchdata/detail-letter.html'
    queryset = models.Letter.objects.filter(admin_published=True)\
        .prefetch_related(
            'letter',
            'letterimage_set',
            'letterperson_set',
            'letterpublictranscription__letterimagepublictranscription')\
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

        # Related data
        context['letterperson_details'] = common.letterperson_details(self.object)
        context['related_letters'] = self.object.letter.filter(admin_published=True)
        context['countries'] = models.SlCountry.objects.all().order_by('id')
        context['letterpublictranscriptions'] = models.LetterPublicTranscription.objects.filter(
            approved_by_project_team=True
        ).order_by('-created_datetime')

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
        # Show letters to Transcribe or not
        transcribe = self.request.GET.get('transcribe', '0')
        show_transcribe = True if transcribe == '1' else False
        queryset = queryset.filter(transcription_is_public=show_transcribe)
        # Search
        search = self.request.GET.get('search', '')
        if search != '':
            queryset = queryset.prefetch_related('letterperson_set', 'letter_type', 'collection', 'location').filter(
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

                # M2M via LetterPerson > Person
                Q(letterperson__person__title__name__icontains=search) |
                Q(letterperson__person__marital_status__name__icontains=search) |
                Q(letterperson__person__religion__name__icontains=search) |
                Q(letterperson__person__rank__name__icontains=search)
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
                'filter_options': filter_options_limit_to_published_related_letters(
                    models.SlLetterCollection.objects
                )
            },
            {
                'filter_id': f'{common.filter_pre_mm}repository',
                'filter_name': 'Repository',
                'filter_options': filter_options_limit_to_published_related_letters(
                    models.SlLetterRepository.objects
                )
            },
            {
                'filter_id': f'{common.filter_pre_mm}letterperson__condition_specific_state',
                'filter_name': 'Specific State',
                'filter_options': filter_options_limit_to_published_related_letters(
                    models.SlLetterPersonConditionSpecificState.objects
                )
            },
            {
                'filter_id': f'{common.filter_pre_mm}letterperson__emotion',
                'filter_name': 'Emotion',
                'filter_options': filter_options_limit_to_published_related_letters(
                    models.SlLetterPersonEmotion.objects
                )
            },
            {
                'filter_id': f'{common.filter_pre_mm}letterperson__body_part',
                'filter_name': 'Body Part',
                'filter_options': filter_options_limit_to_published_related_letters(
                    models.SlLetterPersonBodyPart.objects
                )
            },
            {
                'filter_id': f'{common.filter_pre_mm}letterperson__bodily_activity',
                'filter_name': 'Bodily Activity',
                'filter_options': filter_options_limit_to_published_related_letters(
                    models.SlLetterPersonBodilyActivity.objects
                )
            },
            # Year
            {
                'filter_id': f'{common.filter_pre_gt}sent_date_year',
                'filter_classes': common.filter_pre_gt,
                'filter_name': 'Year Sent (from)',
                'filter_options': models.Letter.objects.filter(sent_date_year__gt=1000).exclude(sent_date_year__isnull=True).distinct().order_by('sent_date_year').values_list('sent_date_year', flat=True),  # NOQA
                'valueSameAsText': True
            },
            {
                'filter_id': f'{common.filter_pre_lt}sent_date_year',
                'filter_classes': common.filter_pre_lt,
                'filter_name': 'Year Sent (to)',
                'filter_options': models.Letter.objects.filter(sent_date_year__gt=1000).exclude(sent_date_year__isnull=True).distinct().order_by('sent_date_year').values_list('sent_date_year', flat=True),  # NOQA
                'valueSameAsText': True
            }
        ]

        return context


class TranscribeSubmitRedirectView(RedirectView):
    """
    Class-based view for letter transcribe submission
    """
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        """
        This method submits the data to the database,
        redirecting to a success/fail page accordingly
        """
        try:
            # Save LetterPublicTranscription object
            letter = models.Letter.objects.get(id=self.request.POST.get('letter-id'))
            letter_public_transcription_obj = models.LetterPublicTranscription.objects.create(letter=letter)
            # Optional fields
            letter_public_transcription_obj.person_name = self.request.POST.get('name', '')
            letter_public_transcription_obj.person_email = self.request.POST.get('email', '')
            letter_public_transcription_obj.person_country_id = self.request.POST.get('country')
            letter_public_transcription_obj.save()

            # Save related/child LetterImagePublicTranscription objects
            for letter_image in letter.letterimage_set.all():
                transcription_text = self.request.POST.get(f'transcribe-image-{letter_image.id}')
                if transcription_text:
                    models.LetterImagePublicTranscription.objects.create(
                        letter_public_transcription=letter_public_transcription_obj,
                        letter_image=letter_image,
                        transcription_text=transcription_text,
                    )

            return reverse('researchdata:transcribe-success')

        except Exception as ex:
            print(ex)
            return reverse('researchdata:transcribe-fail')


class TranscribeSuccessTemplateView(TemplateView):
    """
    Class-based view for letter transcribe success template
    """
    template_name = 'researchdata/transcribe-success.html'


class TranscribeFailTemplateView(TemplateView):
    """
    Class-based view for letter transcribe fail template
    """
    template_name = 'researchdata/transcribe-fail.html'
