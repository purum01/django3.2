from django.shortcuts import render
from .models import User

def profile(request):
    user = User.objects.get(id=1)
    return render(request, 'account/profile.html', {'user':user})

