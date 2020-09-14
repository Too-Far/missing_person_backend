from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import MissingPersonSerializer
from rest_framework.exceptions import MethodNotAllowed
from scraper.models import MissingPerson

class MissingPersonViewSet(viewsets.ModelViewSet):
    queryset = MissingPerson.objects.all()
    serializer_class = MissingPersonSerializer
    http_method_names = ['get', 'options']

    # def post(self, request, *args, **kwargs):
    #     if request.method == 'POST':
    #         return MethodNotAllowed('GET')
