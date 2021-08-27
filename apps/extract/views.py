# Django
from django.shortcuts import render
from django.utils.timezone import now
from django.http import Http404
# rest framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# utils
from .utils import get_text_from_any_pdf

# Create your views here.

class ExtractApiView(APIView):
    """
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, *args, **kwargs):
        path = '/home/joldiazch/prgx_backend/Doc2.pdf'
        text = get_text_from_any_pdf(path)
        return Response({"text": text}, status=status.HTTP_200_OK)