from django.shortcuts import render, HttpResponse, redirect
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

            user = authenticate(username=username,password=password)
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



@login_required
def create_chat(request):
    current_user = request.user
    title = request.POST['group_name']
    chat = GroupChat.objects.create(creator_id=current_user.id, title=title)
    Member.objects.create(chat_id=chat.id, user_id=current_user.id)
    return redirect(reverse('chat:chat', args=[chat.unique_code]))




@login_required
def chat(request, chat_id):
    current_user = request.user
    try:
        chat = GroupChat.objects.get(unique_code=chat_id)
    except GroupChat.DoesNotExist:
        return render(request, 'chat/404.html',)

    if request.method == 'GET':
        if Member.objects.filter(chat_id=chat.id, user_id=current_user.id).count() == 0:
            return render(request, 'chat/join_chat.html', {'chatObject': chat})
        
        return render(request, 'chat/chat.html', {'chatObject': chat, 'chat_id_json': mark_safe(json.dumps(chat.unique_code))})

    elif request.method == 'POST':
        Member.objects.create(chat_id=chat.id, user_id=current_user.id)

        return render(request, 'chat/chat.html', {'chatObject': chat, 'chat_id_json': mark_safe(json.dumps(chat.unique_code))})





@login_required
def leave_chat(request, chat_id):
    current_user = request.user
    try:
        chat = GroupChat.objects.get(unique_code=chat_id)
    except GroupChat.DoesNotExist:
        return render(request, 'chat/404.html')

    if chat.creator_id == current_user.id:
        chat.delete()

    else:
        Member.objects.filter(chat_id=chat.id, user_id=current_user.id).delete()

    return redirect('chat:index')

