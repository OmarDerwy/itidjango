from django.views import View
from .models import School, Class
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import SchoolForm, ClassForm


@method_decorator(csrf_exempt, name='dispatch')
class SchoolViewSet(View):
    def get(self, request):
        schools = School.objects.all()
        return HttpResponse(schools)
    
    def post(self, request):
        form = SchoolForm(json.loads(request.body))
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Data saved successfully!'})
        else:
            return JsonResponse({'message': 'Data not saved!', 'errors': form.errors})
    
    def delete(self, request, *args, **kwargs):
        try:
            school_id = self.kwargs.get('id')
            school = School.objects.get(id=school_id)
            school.delete()
            return JsonResponse({'message': 'Data deleted successfully!'})
        except School.DoesNotExist:
            return JsonResponse({'message': 'School not found!'}, status=404)

@method_decorator(csrf_exempt, name='dispatch')    
class ClassViewSet(View):
    def get(self, request):
        classes = Class.objects.all()
        return HttpResponse(classes)

    def post(self, request):
        form = ClassForm(json.loads(request.body))
        if form.is_valid():
            school_name = form.cleaned_data['school']
            try:
                school = School.objects.get(name=school_name)
                class_instance = form.save(commit=False)
                class_instance.school = school
                class_instance.save()
                
                # Update the total_area_of_classes
                school.total_area_of_classes += class_instance.length * class_instance.width
                # Increase the no_of_classes
                school.no_of_classes += 1
                school.save()
                
                return JsonResponse({'message': 'Data saved successfully!'})
            except School.DoesNotExist:
                return JsonResponse({'message': 'School not found!'}, status=404)
        else:
            return JsonResponse({'message': 'Data not saved!', 'errors': form.errors})
    
    def delete(self, request):
        try:
            class_id = json.loads(request.body).get('id')
            class_instance = Class.objects.get(id=class_id)
            school = class_instance.school
            
            # Update the total_area_of_classes
            school.total_area_of_classes -= class_instance.length * class_instance.width
            # Decrease the no_of_classes
            school.no_of_classes -= 1
            school.save()
            
            class_instance.delete()
            return JsonResponse({'message': 'Data deleted successfully!'})
        except Class.DoesNotExist:
            return JsonResponse({'message': 'Class not found!'}, status=404)