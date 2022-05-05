from django_elasticsearch_dsl import (
    Document ,
    fields,
    Index,
)
from .models import Bussiness
PUBLISHER_INDEX = Index('business')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1,
    
)




@PUBLISHER_INDEX.doc_type
class NewsDocument(Document):
    
    id = fields.IntegerField(attr='id')
    fielddata=True
    name = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    industry = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
    address = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    city = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
    state = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    zip = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
    county = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    phone = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
    fax = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    website = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
    contact = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    title = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
    number = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    employee = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
    sales = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    range = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
    sic = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    description = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
    code = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    latitude = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
    longitude = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    
   

    class Django(object):
        model = Bussiness
