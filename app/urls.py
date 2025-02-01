from django.urls import path
from .views import *

# Create Urls here

urlpatterns = [
    path('', index, name = 'index'),
    path('list', DestinationListView.as_view(), name='list'),
    path('details/<int:id>', DestinationDetailsView.as_view(), name='details/<int:id>'),
]