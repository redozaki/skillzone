from os import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProfileSerializer

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

def profile(request, username) :
	profile = Profile.objects.get(name = username)
	return HttpResponse(f'{profile.name } : points : { profile.points }  , completed :  {profile.courses_completed}')

@api_view(['GET'])
def get_profiles(request) :
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_profile(request) :
	serializer = ProfileSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def get_profile(request) :
	username = request.data.get('username')
	profile = Profile.objects.get(name = username)
	return Response(ProfileSerializer(profile).data)

@api_view(['POST'])
def update_profile(request) :
	username = request.data.get('username')
	profile = Profile.objects.get(name = username)
	serializer = ProfileSerializer(profile , data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)