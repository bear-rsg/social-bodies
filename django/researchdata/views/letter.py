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
    paginate_by = 20

    def get_queryset(self):
        # Start with all published objects
        queryset = self.model.objects.filter(admin_published=True)
        # Search
        search = self.request.GET.get('search', '')
        if search != '':
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(collection__name__icontains=search)
            )
        # Filters
        queryset = common.filter(self.request, queryset)
        # Sort
        queryset = common.sort(self.request, queryset, 'title')
        # Return result, showing only distinct and use prefetch for improved performance
        return queryset.distinct().prefetch_related('letterimage_set')

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
