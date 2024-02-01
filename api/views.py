from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView


def home(request):
    return HttpResponse("Hello World")


class USerView(APIView):
    def get(self, request):
        return Response("Hello World")
