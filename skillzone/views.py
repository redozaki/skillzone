from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("You're at the skillzone index.")