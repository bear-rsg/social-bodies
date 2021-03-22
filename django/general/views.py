from django.views.generic import TemplateView


class WelcomeTemplateView(TemplateView):
    """
    Welcome-based view to show the welcome template
    """
    template_name = 'general/welcome.html'


class AboutTemplateView(TemplateView):
    """
    Class-based view to show the aboutrsno template
    """
    template_name = 'general/about.html'


class BlogTemplateView(TemplateView):
    """
    Class-based view to show the blog template
    """
    template_name = 'general/blog.html'


class CookiesTemplateView(TemplateView):
    """
    Class-based view to show the cookies template
    """
    template_name = 'general/cookies.html'
