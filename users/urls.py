from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
	path('create/',views.create, name='create'),
	path('<str:username>',views.profile),
	path('create_profile',views.create_profile),
	path('get_all_profiles',views.get_profiles),
	path('get_profile',views.get_profile),
	path('update_profile',views.update_profile)
]
