# Django
from django.urls import path, re_path
# views
from .views import ExtractApiView


urlpatterns = [
    path('extract/', ExtractApiView.as_view(), name='extract'),
    path('db_data/', ExtractApiView.as_view(), name='db_data'),
]