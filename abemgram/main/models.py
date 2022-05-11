from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# A Class Message model
class Message(models.Model):
    # user is the person sending the message as a foreign key 
    # sent_to is the person recieving the message as a foreign key
    # message_text is the text message
    # timestamp is the timestamp of the message

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_sender")
    sent_to = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="message_reciever", null=True)
    message_text = models.TextField(max_length=4000)
    timestamp = models.DateTimeField("time sent")
    
    def __str__(self):
        return self.message_text
