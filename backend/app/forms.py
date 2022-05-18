from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from .models import Files

class ExcelModelForm(forms.ModelForm):
  class Meta:
    model = Files
    fields = ('file_name',)
