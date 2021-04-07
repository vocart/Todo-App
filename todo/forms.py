from .models import Todo
from django.forms import ModelForm, TextInput


class TodoForm(ModelForm):
	class Meta:
		model = Todo
		fields = ['title']
		#widgets = {'name': TextInput(attrs={'class':'input', 'placeholder':'Todo Name'})}