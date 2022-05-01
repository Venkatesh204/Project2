from django.db import models



# Create your models here.

class Empdata(models.Model):
	Emp_Name = models.CharField(max_length=25)
	Emp_ID = models.IntegerField()
	Emp_Designation = models.CharField(max_length=40)
	Emp_Date_Of_Joining = models.CharField(max_length=30)
	Emp_Department = models.CharField(max_length=20)
	Emp_Salary_Package = models.IntegerField()
	Emp_Experince = models.IntegerField()

class News(models.Model):
	Occations = models.CharField(max_length=180)

class Calender(models.Model):
	Date =models.CharField(max_length=30)
	Occation = models.CharField(max_length=180)
