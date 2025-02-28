from django.db import models

# Create your models here.
class Classroom(models.Model):
    day = models.CharField(verbose_name='Class name', max_length=50, unique=True)
    subject = models.CharField(verbose_name='Subject', max_length=50)
    year = models.IntegerField(verbose_name='Year')

    length = models.FloatField(verbose_name='Length')
    width = models.FloatField(verbose_name='Width')

    @property
    def area(self):
        return self.length * self.width