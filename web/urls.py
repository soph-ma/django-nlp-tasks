from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path('frequencies/', views.frequencies, name='frequencies'),
    path('get_freq_dict/', views.get_freq_dict, name='get_freq_dict'),
    path('summarization/', views.summarization, name='summarization'),
    path('get_summary/', views.get_summary, name='get_summary'),
    path('lang_detection/', views.lang_detection, name='lang_detection'),
    path('get_language/', views.get_language, name='get_language'),
    path('keywords/', views.keywords, name='keywords'),
    path('get_keywords/', views.get_keywords, name='get_keywords'),

]