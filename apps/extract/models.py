from django.db import models

# Create your models here.

class ExtractedData(models.Model):

    vendor_name = models.CharField(max_length=25, null=True)
    fiscal_number = models.CharField(max_length=20, null=True)
    contract = models.CharField(max_length=25, null=True)
    start_date = models.CharField(max_length=20, null=True)
    end_date = models.CharField(max_length=20, null=True)
    comments = models.CharField(max_length=500, null=True)
    doc_path = models.CharField(max_length=500, null=True)


    def __str__(self):
        return "{} : {}".format(self.vendor_name, self.fiscal_number)

    class Meta:
        verbose_name = 'ExtractedData'
        verbose_name_plural = 'ExtractedDatas'