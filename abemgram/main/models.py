from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_sender")
    sent_to = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="message_reciever", null=True)
    message_text = models.TextField(max_length=4000)
    timestamp = models.DateTimeField("time sent")
    
    def __str__(self):
        return self.message_text
