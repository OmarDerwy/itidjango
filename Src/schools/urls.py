from django.urls import path
from .viewsets import SchoolViewSet, ClassViewSet

urlpatterns = [
    path('classes/', ClassViewSet.as_view(), name='class'),
    path('<int:id>/', SchoolViewSet.as_view(), name='school_detail'),
    path('', SchoolViewSet.as_view(), name='school'),
]