from django.http import HttpResponseBadRequest, HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import MethodNotAllowed
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from todo import settings 
from todo.models import Task
from todo.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    model = Task
    queryset = Task.objects.all()
    filter_backends = (DjangoFilterBackend, )
    

def ping(request):
    return HttpResponse("pong")

def status(request): 
    return JsonResponse({
        "status": "ok",
        "environment": settings.MODE,
        "name": settings.SERVICE_NAME
    })
