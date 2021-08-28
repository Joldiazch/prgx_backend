# Django
from django.urls import path, re_path
# views
from .views import ExtractFromPathApiView, ExtractFromFileApiView, DbDataApiView


urlpatterns = [
    path('extract/', ExtractFromPathApiView.as_view(), name='extract'),
    path('db_data/', DbDataApiView.as_view(), name='db_data'),
    path('extract/file', ExtractFromFileApiView.as_view(), name='extract_from_file')
]