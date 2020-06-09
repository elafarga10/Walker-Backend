from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.WalkEntryList.as_view(), name='walkentry_list'),
    path('<int:pk>', views.WalkEntryDetail.as_view(), name='walk_detail'),
]