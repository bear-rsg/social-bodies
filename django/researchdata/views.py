from django.views.generic import (DetailView, ListView)
from . import models


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
    paginate_by = 50


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
    paginate_by = 50
