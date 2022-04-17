from django.contrib import admin
from admissions.models import Students
from admissions.models import StaffList


class columns(admin.ModelAdmin):
    list_display=['name','father_Name','gender','id']
# Register your models here.
admin.site.register(Students,columns)

class columns1(admin.ModelAdmin):
    list_display=['name','subject','phone_No','experience','id']

admin.site.register(StaffList,columns1)
