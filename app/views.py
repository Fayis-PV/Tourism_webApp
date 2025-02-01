from django.shortcuts import render,redirect
from rest_framework.generics import ListCreateAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser,MultiPartParser
from .forms import DestinationForm
from .models import Destination, Image
from .serializers import DestinationSerializer, ImageSerializer

# Create your views here.

def index(request):
    return redirect('/list')

class DestinationListView(ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
