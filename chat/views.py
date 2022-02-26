from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.contrib.auth import login, logout, authenticate
import json

from .models import Member, GroupChat
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('chat:index')

            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'chat/register.html', {'form': form})



@login_required
def index(request):
    current_user = request.user
    return render(request, 'chat/index.html', {'chats': current_user.member_set.all()})










