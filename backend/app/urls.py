from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
  path('', views.getFiles, name='files'),
  path('businesses/', views.getBusinesses, name='businesses'),
  path('upload/', views.fileUpload.as_view(), name='file'),
  path('search/' , views.PublisherDocumentView.as_view({'get': 'list'})),
]
