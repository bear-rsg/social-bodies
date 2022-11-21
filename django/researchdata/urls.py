from django.urls import path
from .views.letter import (LetterListView,
                           LetterDetailView,
                           TranscribeSubmitRedirectView,
                           TranscribeSuccessTemplateView,
                           TranscribeFailTemplateView)
from .views.person import PersonListView, PersonDetailView

app_name = 'researchdata'

urlpatterns = [

    # Letters
    path('letters/', LetterListView.as_view(), name='letter-list'),
    path('letters/<pk>/', LetterDetailView.as_view(), name='letter-detail'),

    # Transcribe
    path('transcribe/submit/', TranscribeSubmitRedirectView.as_view(), name='transcribe-submit'),
    path('transcribe/success/', TranscribeSuccessTemplateView.as_view(), name='transcribe-success'),
    path('transcribe/fail/', TranscribeFailTemplateView.as_view(), name='transcribe-fail'),

    # People
    path('people/', PersonListView.as_view(), name='person-list'),
    path('people/<pk>/', PersonDetailView.as_view(), name='person-detail'),

]
