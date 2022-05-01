from django import forms
from app.models import Empdata
from app.models import News
from app.models import Calender

class EmployeeForm(forms.ModelForm):
	class Meta:
		model=Empdata
		fields='__all__'    

class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = '__all__'
	
class CalenderForm(forms.ModelForm):
	class Meta:
		model = Calender
		fields = '__all__'
	

