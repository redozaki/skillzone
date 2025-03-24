from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from.models import User
# Create your views here.
def users(request):
	users = User.objects.all()
	return render(request , 'users.html' ,{'users' : users})
def create(request) :
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()  # This saves the new user to the database
			return redirect('users') 
	else:
		form = UserForm()
	return render(request, 'create.html', {'form': form})