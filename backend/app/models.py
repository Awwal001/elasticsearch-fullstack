from django.db import models

def upload_path(instance, filename):
  return 'files/{filename}'.format(filename=filename)

# Create your models here.
class Files(models.Model):
  file_name = models.FileField(upload_to=upload_path)
  title = models.CharField(max_length=32, blank=False)
  
  def __str__(self):
    return f"File id({self.id}): {self.title}"


class Bussiness(models.Model):
  
  name = models.CharField(max_length=300, blank=True, null=True)
  industry = models.CharField(max_length=300, blank=True, null=True)
  address = models.CharField(max_length=300, blank=True, null=True)
  city = models.CharField(max_length=300, blank=True, null=True)
  state = models.CharField(max_length=300, blank=True, null=True)
  zip = models.CharField(max_length=300, blank=True, null=True)
  county = models.CharField(max_length=300, blank=True, null=True)
  phone = models.CharField(max_length=300, blank=True, null=True)
  fax = models.CharField(max_length=300, blank=True, null=True)
  website = models.CharField(max_length=300, blank=True, null=True)
  contact = models.CharField(max_length=300, blank=True, null=True)
  title = models.CharField(max_length=300, blank=True, null=True)
  number = models.CharField(max_length=300, blank=True, null=True)
  employee = models.CharField(max_length=300, blank=True, null=True)
  sales = models.CharField(max_length=300, blank=True, null=True)
  range = models.CharField(max_length=300, blank=True, null=True)
  sic = models.CharField(max_length=300, blank=True, null=True)
  description = models.CharField(max_length=300, blank=True, null=True)
  code = models.CharField(max_length=300, blank=True, null=True)
  latitude = models.CharField(max_length=300, blank=True, null=True)
  longitude = models.CharField(max_length=300, blank=True, null=True)
  


  def __str__(self):
    return  self.name
