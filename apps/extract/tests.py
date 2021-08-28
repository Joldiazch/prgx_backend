#django
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# rest framework
from rest_framework.test import APIClient
from rest_framework import status
# utils
from apps.extract.utils import get_text_from_any_pdf, get_values_from_text

class ExtractApiTestCase(TestCase):

    def setUp(self):
        # api client
        self.client = APIClient()


    def test_extract_url(self):
        """
        test if /extract/ endpoint is work
        """
        url = reverse('extract')
        path = './uploated_files/Doc2.pdf'
        response = self.client.get(url+'?doc_path='+path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ocr2(self):
        """
        test ocr of specific file
        """
        path = './uploated_files/Doc2.pdf'
        data = get_values_from_text(path)

        self.assertEqual(data.get('vendor_name'), 'PRGX COLOMBIA LTDA')
        self.assertEqual(data.get('fiscal_number'), '1234567-2')
        self.assertEqual(data.get('contract'), '101010')
        self.assertEqual(data.get('start_date'), '01/01/2021')
        self.assertEqual(data.get('end_date'), '31/12/2021')
        self.assertEqual(data.get('comments'), 'CRAS ACCUMSAN AC PURUS ET ALIQUAM. PHASELLUS EGET CURSUS FELIS. VIVAMUS TINCIDUNT IACULIS PURUS\nAT IMPERDIET. INTEGER EGET DUI EUISMOD, DAPIBUS VELIT VEL, INTERDUM IPSUM.')

    
    def test_ocr3(self):
        """
        test ocr of specific file
        """
        path = './uploated_files/Doc3.pdf'
        data = get_values_from_text(path)

        self.assertEqual(data.get('vendor_name'), 'TESTER S.A.S')
        self.assertEqual(data.get('fiscal_number'), '987654321-0')
        self.assertEqual(data.get('contract'), '54334554')
        self.assertEqual(data.get('start_date'), '15/2/2020')
        self.assertEqual(data.get('end_date'), '3/3/2020')
        self.assertEqual(data.get('comments'), None)

    
    def test_ocr4(self):
        """
        test ocr of specific file
        """
        path = './uploated_files/Doc4.pdf'
        data = get_values_from_text(path)

        self.assertEqual(data.get('vendor_name'), 'A.B.AC')
        self.assertEqual(data.get('fiscal_number'), '121212')
        self.assertEqual(data.get('contract'), '123123')
        self.assertEqual(data.get('start_date'), '10/10/2021')
        self.assertEqual(data.get('end_date'), '10/10/2022')
        self.assertEqual(data.get('comments'), 'CRAS ACCUMSAN AC PURUS ET ALIQUAM. PHASELLUS EGET CURSUS FELIS. VIVAMUS TINCIDUNT IACULIS PURUS\nAT IMPERIAL. INTEGER EGRET DUI EULIMID, DAP BUS VALET VEL, INTERDORM IPSUM.')


    def test_db_data_endpoint(self):
        """
        test if /db-data/ endpoint is work
        """
        url = reverse('db_data')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)