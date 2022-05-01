from django.contrib import admin
from app.models import Empdata
from app.models import News
from app.models import Calender

# Register your models here.

class EmpdataAdmin(admin.ModelAdmin):
	list_display = ['Emp_Name','Emp_ID','Emp_Designation','Emp_Date_Of_Joining','Emp_Department','Emp_Salary_Package','Emp_Experince']

admin.site.register(Empdata,EmpdataAdmin)

class NewsAdmin(admin.ModelAdmin):
	list_display = ['Occations']

admin.site.register(News,NewsAdmin)


class CalenderAdmin(admin.ModelAdmin):
	list_display = ['Date','Occation']

admin.site.register(Calender,CalenderAdmin)