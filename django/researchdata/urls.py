from django.urls import path
from .views.letter import LetterListView, LetterDetailView
from .views.person import PersonListView, PersonDetailView

app_name = 'researchdata'

urlpatterns = [

    # Letters
    path('letters/', LetterListView.as_view(), name='letter-list'),
    path('letters/<pk>/', LetterDetailView.as_view(), name='letter-detail'),

    # People
    path('people/', PersonListView.as_view(), name='person-list'),
    path('people/<pk>/', PersonDetailView.as_view(), name='person-detail'),

]
