from django.urls import path
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="general/coming-soon.html"), name='comingsoon'),
]
