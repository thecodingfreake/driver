from django.urls import path
from . import views
urlpatterns=[
    path("",views.index),
    path("login",views.login),
    path('addition',views.addition),
    path('addition2',views.formapp),
    path('additions',views.addition2),
    path('additions2',views.formapp2),
]