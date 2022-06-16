from django.views.generic import (DetailView, ListView)
from django.db.models import Q
from .. import models
from . import common


class LetterDetailView(DetailView):
    """
    Class-based view for letter detail template
    """
    template_name = 'researchdata/detail-letter.html'
    model = models.Letter


class LetterListView(ListView):
    """
    Class-based view for letter list template
    """
    template_name = 'researchdata/list-letter.html'
    model = models.Letter
    paginate_by = 100

    def get_queryset(self):
        # Start with all published objects
        queryset = self.model.objects.filter(admin_published=True)

        #
        # Search
        #

        search = self.request.GET.get('search', '')
        search_by = self.request.GET.get('search_by', '')

        # Search all fields and related data in a single search
        if search_by == '' and search != '':
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(collection__name__icontains=search)
            )

        # Search by specific fields, if search_by is specified
        

        #
        # Order
        #

        queryset = common.sort(self.request, queryset, 'title')

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
        ]

        return context
