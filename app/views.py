import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
from django.contrib import messages
from .forms import DestinationForm
from .models import Destination, Image
from .serializers import DestinationSerializer, ImageSerializer


# Create your views here.

def index(request):
    return redirect('/list_destination')


class DestinationListView(ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [AllowAny]


class DestinationDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


def list_destinations(request):
    response = requests.get('http://127.0.0.1:8000/list')
    if response.status_code == 200:
        datas = response.json()
        print(datas)
    else:
        print(response.status_code)
        datas = None
    return render(request, 'index.html', {'datas':datas})


def create_destination(request):
    if request.method == "POST":
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            api_url = 'http://127.0.0.1:8000/list/'
            try:
                response = requests.post(api_url,data=data)
                if response.status_code == 200:
                    messages.success(request, 'Successfuly created')
                else:
                    messages.error(request, f'Something went wrong: {response.status_code}')
            except requests.RequestException as RE:
                messages.error(request, f'Something went wrong: {RE}')
        else:
            messages.error(request, 'Please fill the form clearly')
    else:
        form = DestinationForm()
    return render(request, 'create.html', {'form':form})


def details_destination(request,pk):
    print('Hello')
    api_url = f'http://127.0.0.1:8000/details/{pk}'
    print(api_url)
    data = None
    try:
        response = requests.get(api_url)
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            return render(request, 'details.html', {'data': data})
        else:
            messages.error(request, f'Something went wrong: {response.status_code}')
    except requests.RequestException as e:
        messages.error(request, f'Something went wrong: Error: {e}')
    return redirect('/list_destination')


def update_destination(request,pk):
    pass

def delete_destination(request,pk):
    pass