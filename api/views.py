from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from ext.auth import BaseAuthentication


class USerView(APIView):
    # authentication_classes = []

    def get(self, request):
        return Response("USerView")


class LoginView(APIView):
    # authentication_classes = [MyAuthentication, ]

    def get(self, request):
        return Response("LoginView")


class OrderView(APIView):
    # authentication_classes = [MyAuthentication, ]

    def get(self, request):
        return Response("OrderView")
