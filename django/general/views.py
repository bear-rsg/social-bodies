from django.views.generic import TemplateView


class ComingSoonTemplateView(TemplateView):
    """
    Class-based view to show the coming soon template
    """

    template_name = 'general/coming-soon.html'
