from django.urls import path
from . import views
urlpatterns = [
    path('', views.display),
    path('contact/', views.contact),
    path('about/', views.about),

    path('python/', views.python),
    path('java/', views.java),

    path('web/', views.web),
    path('android/', views.android),
    path('prog/', views.prog),

    path('htcss/', views.htcss),

    path('quiz/', views.quiz),

    path('cc/', views.c),
    path('cj/', views.j),

    path('index/', views.index, name = "index"),
    path('runcode', views.runcode, name = "runcode"),
]
