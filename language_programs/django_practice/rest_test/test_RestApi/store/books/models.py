from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Books(models.Model):
    
    name = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    publication = models.CharField(max_length=200, blank=True, null=True)
    max_print = models.IntegerField(default=0)
    
    is_active = models.IntegerField(default=1,validators=[MinValueValidator(0),MaxValueValidator(1)])
    
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False) 

    def __str__(self):
        return str(self.id)
