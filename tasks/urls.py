from django.urls import path
from tasks.views import *
urlpatterns = [
    path('' , dashboard_view , name='dashboard')
]