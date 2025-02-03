from django.urls import path
from .views import *

# Create Urls here

urlpatterns = [
    path('', index, name = 'index'),
    path('list', DestinationListView.as_view(), name='list'),
    path('details/<int:pk>', DestinationDetailsView.as_view(), name='detail'),

    path('list_destination', list_destinations, name= 'list_destination'),
    path('create_destination', create_destination, name='create_destination'),
    path('details_destination/<int:pk>', details_destination, name ='details_destination')
]