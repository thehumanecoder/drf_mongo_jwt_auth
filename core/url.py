from django.conf.urls import url, include
from . import views
from django.urls import path
import mongo_auth

urlpatterns = [
    path('mongo_auth/', include('mongo_auth.urls')),
    path('checkUserAuth',views.checkAuth,name='checkAuth')
]
