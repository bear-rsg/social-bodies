from django.urls import path
from . import views

app_name = 'researchdata'

urlpatterns = [

    # Letters
    path('letters/', views.LetterListView.as_view(), name='letter-list'),
    path('letters/<pk>/', views.LetterDetailView.as_view(), name='letter-detail'),

    # People
    path('people/', views.PersonListView.as_view(), name='person-list'),
    path('people/<pk>/', views.PersonDetailView.as_view(), name='person-detail'),

]
