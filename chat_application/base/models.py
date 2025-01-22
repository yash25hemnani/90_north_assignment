from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class ChatModel(models.Model):
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('GroupModel', on_delete=models.CASCADE)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE)

class GroupModel(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='custom', blank=True)