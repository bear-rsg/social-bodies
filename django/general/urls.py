from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomeTemplateView.as_view(), name='welcome'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('blog/', views.BlogTemplateView.as_view(), name='blog'),
    path('cookies/', views.CookiesTemplateView.as_view(), name='cookies'),
]
