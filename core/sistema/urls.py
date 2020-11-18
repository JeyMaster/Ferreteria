from django.urls import path
from core.sistema.views.products import views
urlpatterns=[
    path('',views.Inicio.as_view()),
]