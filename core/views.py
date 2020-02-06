from django.shortcuts import render
from mongo_auth.permissions import AuthenticatedOnly 
from rest_framework.decorators import permission_classes,api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET","POST"])



def checkAuth(request):
    return StreamingHttpResponse('Hello World')
