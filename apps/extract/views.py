# Django
from django.shortcuts import render
from django.utils.timezone import now
from django.http import Http404
# rest framework
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
# models
from .models import ExtractedData
# serializers
from .serializers import ExtractedDataSerializer
# forms
from .forms import UploadFileForm
# utils
from .utils import get_text_from_any_pdf, get_values_from_text, handle_uploaded_file
import os

# Create your views here.

class ExtractFromPathApiView(APIView):
    """
    view to get all extractedData stored and
    to create an new extractedData from an path to file 
    """


    def get(self, request):
        """
        get all extractedData stored in db_data
        """
        extracted_data = ExtractedData.objects.all()
        serializer = ExtractedDataSerializer(extracted_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        """
        create an new extractedData from an path to file
        """

        # get doc_path and creck is not None
        doc_path = request.query_params.get('doc_path', None)
        if not doc_path:
            return Response(
                {"error": "No doc_path specified"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # check if file exists in root folder
        # (volumen of docker contarier that allows it
        # to read files from the host machine.)
        head, file_name = os.path.split(doc_path)
        path = './' + file_name
        if not os.path.isfile(path):
            return Response(
                {
                    "error":
                    "file not found, the file must be located in the root folder of this project"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        data = get_values_from_text(path)
        serializer = ExtractedDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExtractFromFileApiView(APIView):
    """
    extracted data from file in request (no path)
    """


    def post(self, request):
        """
        extracted data from file in request (no path)
        """
        # read file uploadted
        file_obj = request.FILES['file']
        # Write file locally to parse
        path = handle_uploaded_file(file_obj)
        # parse file and extract data
        data = get_values_from_text(path)
        # serialize data and save this in db
        serializer = ExtractedDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DbDataApiView(APIView):
    """
    view to get all extractedData stored in db
    """


    def get(self, request):
        """
        get all extractedData stored in db_data
        """
        extracted_data = ExtractedData.objects.all()
        serializer = ExtractedDataSerializer(extracted_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)