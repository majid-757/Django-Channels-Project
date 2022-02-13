from django.shortcuts import render, HttpResponse
from django.utils.safestring import mark_safe 
import json


def index(request):

    return render(request, 'echo/index.html')


def echo_image(request):
    return render(request, 'echo/echo_image.html')



def join_chat(request, username):
    return render(request, 'echo/join_chat.html', {'username_json': mark_safe(json.dumps(username))})











