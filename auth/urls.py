
from django.contrib import admin
from django.urls import path,include
from core import url
urlpatterns = [
    path('', include(url)),
]
