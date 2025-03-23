from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import UserForm
# Create your views here.
def users(request):
	template = loader.get_template('users.html')
	return HttpResponse(template.render())
def create(request) :
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()  # This saves the new user to the database
			return redirect('users') 
	else:
		form = UserForm()
	return render(request, 'create.html', {'form': form})