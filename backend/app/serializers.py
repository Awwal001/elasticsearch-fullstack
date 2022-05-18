from rest_framework import serializers
from .models import Files, Bussiness
import json
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *

class FileSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Files
    fields = ['file_name', 'title']

class BusinessSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bussiness
    fields = '__all__'

class NewsDocumentSerializer(DocumentSerializer):

    class Meta(object):
        """Meta options."""
        model = Bussiness
        document = NewsDocument
        fields = '__all__'
        def get_location(self, obj):
            """Represent location value."""
            try:
                return obj.location.to_dict()
            except:
                return {}
