import imp
from os import stat
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, status, permissions,renderers, generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated, IsAdminUser
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import filters
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from .models import Appliance, AppliancePhoto
from task.models import Task
from .serializers import ApplianceSerializer
from .permissions import AddAppliancePermissions, UpdateAppliancePermissions
from datetime import datetime

from users.models import User
from .forms import ApplianceForm, AppliancePhotoForm

# Create your views here.

class ApplianceViewSet(viewsets.ReadOnlyModelViewSet, PermissionRequiredMixin):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    # permission_classes =[IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['serial_number', 'name']
    template_name = "appliances/list.html"
    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data["appliances"] = Appliance.objects.all()
    #     return context_data

class AddApplianceViewSet(CreateModelMixin, ListModelMixin, viewsets.GenericViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer
    # permission_required = ("appliances.add_appliance", "appliances.view_appliance")

    def list(self, request):
        appliances = Appliance.objects.all()
        serializer = ApplianceSerializer(appliances, many=True)
        self.check_object_permissions(request, self.request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = ApplianceSerializer(data=request.data)
        self.check_object_permissions(request, self.request.user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get_permissions(self):
        if self.action == "list":
            permission_classes = [
                IsAuthenticated,
            ]
        elif self.action == "create":
            permission_classes = [IsAdminUser]
        else: 
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class UpdateApplianceViewSet(UpdateModelMixin, RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer

    def retrieve(self, request, pk):
        appliance = get_object_or_404(Appliance, pk=pk)
        serializer = ApplianceSerializer(appliance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        appliance = get_object_or_404(Appliance, pk=pk) 
        serializer = ApplianceSerializer(appliance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [
                IsAuthenticated,
            ]
        elif self.action == "update":
            permission_classes = [IsAdminUser]
        else: 
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    


class ApplianceView(TemplateView):
    template_name = "appliances/list.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["appliances"] = Appliance.objects.all()
        return context_data

# class ApplianceAddView(TemplateView):
#     template_name = "appliances/add_appliance.html"

#     def add_appliance(request):
#         form = ApplianceForm
#         if request.method == "POST":
#             print(request.POST)
#             form = ApplianceForm(request.POST)
#             if form.is_valid():
#                 form.save()

#         return render(request, 'appliances/add_appliance.html', {'form':form})

def add_appliance(request):
        form = ApplianceForm
        if request.method == "POST":
            form = ApplianceForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.creator = request.user
                instance.save()
                return redirect('appliance-list')

        return render(request, 'appliances/add_appliance.html', {'form':form})


def appliance_detail(request, appliance_id):
    print(appliance_id)
    appliance = Appliance.objects.get(pk=appliance_id)
    appliance_photos = AppliancePhoto.objects.filter(appliance=appliance)
    appliance_tasks = Task.objects.filter(task_appliance=appliance)
    print(appliance_photos)
    print(appliance_tasks)

    return render(request, 'appliances/appliance_detail.html', {'appliance':appliance, 'appliance_photos':appliance_photos, 'appliance_tasks': appliance_tasks})

# def upload_photo(request):
#     if request.method == 'POST' and request.FILES['upload']:
#         print(request)
#         upload = request.FILES['upload']
#         fss = FileSystemStorage()
#         file = fss.save(upload.name, upload)
#         file_url = fss.url(file)
#         return render(request, 'appliances/upload_appliance.html', {'file_url': file_url})
#     return render(request, 'appliances/upload_appliance.html')
    
def upload_photo(request, appliance_id):
    if request.method == "POST":
        form = AppliancePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.appliance = Appliance.objects.get(pk=appliance_id)
            instance.save()
            print(instance)
            # return HttpResponseRedirect(f'serviceapp/appliance/{appliance_id}')
            # return HttpResponseRedirect(f'/')
            return redirect('appliance-detail', appliance_id)

    form = AppliancePhotoForm()
    # photos= AppliancePhoto.objects.all()
    photos= AppliancePhoto.objects.filter(appliance_id=appliance_id)
    print(photos)
    return render(request=request, template_name="appliances/upload_appliance.html", context={'form':form, 'photos':photos})