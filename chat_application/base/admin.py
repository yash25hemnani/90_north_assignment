from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ChatModel)
class ChatModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'timestamp', 'group', 'sent_by']

@admin.register(GroupModel)
class GroupModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']