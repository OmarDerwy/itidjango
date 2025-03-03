from django.forms import ModelForm
from .models import School, Class

class SchoolForm(ModelForm):
    class Meta:
        model = School
        fields = ['name']
        
class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'school', 'length', 'width']