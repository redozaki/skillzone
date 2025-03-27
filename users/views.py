from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Profile
# Create your views here.
def users(request):
	Profiles = Profile.objects.all()
	return render(request , 'users.html' ,{'profiles' : Profiles})
def create(request) :
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()  # This saves the new user to the database
			return redirect('users') 
	else:
		form = UserForm()
	return render(request, 'create.html', {'form': form})