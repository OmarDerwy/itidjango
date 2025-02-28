from django.urls import path
from .views import home, class_retrieve

urlpatterns = [
    path('<str:param>/', home, name='home'),
    path('class/<str:class_name>/', class_retrieve, name='class_retrieve'),
]