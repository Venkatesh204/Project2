from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from app.models import Empdata
from app.forms import EmployeeForm
from app.forms import NewsForm
from app.models import News
from app.forms import CalenderForm
from app.models import Calender



# Create your views here.
def home(request):
	return render(request,'app/home.html')

@login_required
def HR_MANAGER(request):
	return render(request,'app/hrmanager.html')

def EMPLOYEE(request):
	return render(request,'app/employee.html')

def Hr_data(request):
	return render(request,'app/hrdata.html')


def Emp_Form(request):
	form = EmployeeForm()
	if request.method =="POST":
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/employeedata')
	return render(request,'app/employeeform.html',{'form':form})

def Empdata_view(request):
	employees = Empdata.objects.all()
	return render(request,'app/employeedata.html',{'e':employees}) 

def delete_view(request,id):
	employee = Empdata.objects.get(id=id)
	employee.delete()
	return redirect('/employeedata')
	return render(request,'app/employeedata.html')

def update_view(request,id):
	employee =Empdata.objects.get(id=id)
	if request.method == "POST":
		form = EmployeeForm(request.POST,instance=employee)
		if form.is_valid():
			form.save()
			return redirect('/employeedata')
	return render(request,'app/update.html',{'e':employee})


def Add_news(request):
	 news = NewsForm()
	 if request.method =="POST":
	 	news = NewsForm(request.POST)
	 	if news.is_valid():
	 		news.save()
	 		return redirect('/news')
	 return render(request,'app/addnews.html',{'News':news})

def News_View(request):
	news = News.objects.all()
	return render(request,'app/news.html',{'n':news})

def Holiday(request):
	calender = CalenderForm()
	if request.method =="POST":
	 	calender = CalenderForm(request.POST)
	 	if calender.is_valid():
	 		calender.save()
	 		return redirect('/holidays')
	return render(request,'app/addholidays.html',{'calender':calender})


def Holidays(request):
	calender = Calender.objects.all()
	return render(request,'app/holidays.html',{'c':calender})





