from django.urls import path
from . import views

urlpatterns = [
    path('', views.ComingSoonTemplateView.as_view(), name='comingsoon'),
]
