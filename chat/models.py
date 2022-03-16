from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
import random



def UniqueGenerator(length=10):
    source = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for _ in range(length):
        result += source[random.randint(0, length)]

    return result




class GroupChat(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    unique_code = models.CharField(max_length=10, default=UniqueGenerator)
    date_created = models.DateTimeField(default=timezone.now)




class Member(models.Model):
    chat = models.ForeignKey(to=GroupChat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.user.username




class Message(models.Model):
    chat = models.ForeignKey(to=GroupChat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default="")
    date_created = models.DateTimeField(default=timezone.now)







status_list = {
    0: 'Contacting',
    1: 'Not available',
    2: 'Accepted',
    3: 'Rejected',
    4: 'Busy',
    5: 'Proccessing',
    6: 'Ended',
}


class VideoThread(models.Model):
    caller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='caller_user')
    callee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='callee_user')
    status = models.IntegerField(default=0)
    date_started = models.DateTimeField(default=datetime.now)
    date_ended = models.DateTimeField(default=datetime.now)
    date_created = models.DateTimeField(default=datetime.now)


    @property
    def status_name(self):
        return status_list[self.status]



    @property
    def duration(self):
        return self.date_ended - self.date_created


