from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Files, Bussiness
from .serializers import FileSerializer, BusinessSerializer
from django.http import HttpResponse
from rest_framework import settings, viewsets, filters, generics, permissions
from rest_framework.response import Response
import pandas as pd
from django.conf import settings

from .documents import *
from .serializers import *

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)
# Create your views here.

@api_view(['GET'])
def getBusinesses(request):
  Businesses = Bussiness.objects.all()
  serializer = BusinessSerializer(Businesses, many=True)
  return Response(serializer.data)



@api_view(['GET'])
def getFiles(request):
  files = Files.objects.all()
  serializer = FileSerializer(files, many=True)
  return Response(serializer.data)


class fileUpload(APIView):
  
  def post(self, request):
 
    file = Files.objects.create(file_name=request.FILES['files'])

    df = pd.read_excel(f"{settings.BASE_DIR}/media/{file.file_name}")

    #print(df.values.tolist())

    for NAME, INDUSTRY, ADDRESS, CITY, STATE, ZIP, COUNTY, PHONE, FAX, WEBSITE, TITLE, CONTACT, NUMBER, EMPLOYEE, SALES, RANGE, SIC, DESCRIPTION , CODE, LATITUDE, LONGITUDE in zip(df.name,
    df.industry, df.address, df.city, df.state, df.zip, df.county, df.phone, df.fax, df.website, df.title, df.contact, df.number, df.employee, df.sales, 
    df.range, df.sic, df.description, df.code, df.latitude, df.longitude):

      models = Bussiness(name=NAME, industry=INDUSTRY, address=ADDRESS, city=CITY, state=STATE, zip=ZIP, county=COUNTY, phone=PHONE, fax=FAX, website=WEBSITE,
        title=TITLE, contact=CONTACT, number=NUMBER, employee=EMPLOYEE, sales=SALES, range=RANGE, sic=SIC, description=DESCRIPTION, code=CODE, latitude=LATITUDE, longitude=LONGITUDE)
      models.save()

    serializer = FileSerializer(file, many=False)
    return Response(serializer.data)

  # def post(self, request, format=None):
  #   if request.method == 'POST':
  #       form = ExcelModelForm(request.POST or None, request.FILES or None)
  #       if form.is_valid():
  #           instance = Files(file_name=request.FILES['file'])
  #           df = pd.read_excel(form)

  #           for i in (df.values.tolist()):
  #             print(i)

            # for NAME, INDUSTRY, ADDRESS, CITY, STATE, ZIP, COUNTY, PHONE, FAX, WEBSITE, TITLE, CONTACT, NUMBER, EMPLOYEE, SALES, RANGE, SIC, DESCRIPTION , CODE, LATITUDE, LONGITUDE in zip(df.name,
            #   df.industry, df.address, df.city, df.state, df.zip, df.county, df.phone, df.fax, df.website, df.title, df.contact, df.number, df.employee, df.sales, 
            #   df.range, df.sic, df.description, df.code, df.latitude, df.longitude):

            #   models = Bussiness(name=NAME, industry=INDUSTRY, address=ADDRESS, city=CITY, state=STATE, zip=ZIP, county=COUNTY, phone=PHONE, fax=FAX, website=WEBSITE,
            #     title=TITLE, contact=CONTACT, number=NUMBER, employee=EMPLOYEE, sales=SALES, range=RANGE, sic=SIC, description=DESCRIPTION, code=CODE, latitude=LATITUDE, longitude=LONGITUDE)
            #   models.save()
  #           return HttpResponse({'message': 'file uploaded'}, status=200)
class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer

    # lookup_field = 'first_name'
    # fielddata=True
    
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
   
    search_fields = (
        'name', 'industry', 'address', 'city', 'state', 'zip', 'county', 
        'phone', 'fax', 'website', 'title', 'contact', 'number', 'employee', 'sales', 
        'range', 'sic', 'description', 'code', 'latitude', 'longitude'
    )
    multi_match_search_fields = (
        'name', 'industry', 'address', 'city', 'state', 'zip', 'county', 
        'phone', 'fax', 'website', 'title', 'contact', 'number', 'employee', 'sales', 
        'range', 'sic', 'description', 'code', 'latitude', 'longitude'
    )
    filter_fields = {
        'name' : 'name',
        'industry' : 'industry',
        'address' : 'address',
        'city' : 'city',
        'state' : 'state',
        'zip' : 'zip',
        'county' : 'county',
        'phone' : 'phone',
        'fax' : 'fax',
        'website' : 'website',
        'title' : 'title',
        'contact' : 'contact',
        'number' : 'number',
        'employee' : 'employee',
        'sales' : 'sales',
        'range' : 'range',
        'sic' : 'sic',
        'description' : 'description',
        'code' : 'code',
        'latitude' : 'latitude',
        'longitude' : 'longitude',
        
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ( 'id'  ,)
        
  