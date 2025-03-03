from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)
    no_of_classes = models.IntegerField(default=0, blank=True)
    total_area_of_classes = models.FloatField(default=0.0, blank=True)

    def __str__(self):
        return self.name
    
class Class(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=30)
    
    length = models.FloatField(default=0.0)
    width = models.FloatField(default=0.0)

    @property
    def area(self):
        return self.length * self.width

    def __str__(self):
        return self.name