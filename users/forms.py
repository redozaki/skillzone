from django import forms
from django.contrib.auth.models import User
from .models import Profile
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password']) 
        if commit:
            user.save()
            profile = Profile(user=user)
            profile.save()
        return user