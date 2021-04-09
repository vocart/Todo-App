from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

def home(request):
	form = TodoForm()

	todos = Todo.objects.all()

	todo_data = []
	for todo in todos:

		todo_list = {
			'name': todo.title, 
			'message': todo.message
			}
		todo_data.append(todo_list)

	return render(request, 'todo/todo.html', {'todos':todos, 'todo_list':todo_list})


def delete_todo(request, todo_title):
    Todo.objects.filter(title=todo_title).delete()
    return redirect('home')