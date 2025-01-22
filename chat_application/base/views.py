from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import GroupModel, ChatModel
from userauth.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your views here.

def signup(request):
    
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
            
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            
            return HttpResponse("Added")
        else:
            for field, errors in form.errors.items():
                print(f"Error in {field}: {errors}")

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)

def loginUser(request):
    User = get_user_model()
    if request.user.is_authenticated:
        return redirect('startPage')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)

        except Exception as e:
            print(e)

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('chat', groupName="default")
        
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def startPage(request):
    User = get_user_model()
    try:
        users = User.objects.filter(~Q(email=request.user.email))
    except Exception as e:
        users = []
        print(e)

    context = {
        "users" : users,
    }

    return render(request, 'default.html', context=context)

def startChat(request, email):
    User = get_user_model()
    other_user = User.objects.get(email=email)

    usernames = sorted([request.user.username, other_user.username])
    
    group_name = f"chat_{usernames[0]}_{usernames[1]}"

    group = GroupModel.objects.filter(users__in=[request.user, other_user]).distinct().first()

    if not group:
        group = GroupModel.objects.create(name=group_name)
        group.users.add(request.user, other_user)

    return redirect('chat', groupName=group.name)

def chat(request, groupName):
    User = get_user_model()
    users = User.objects.filter(~Q(email=request.user.email))

    group = GroupModel.objects.filter(name=groupName).first()
    chats = []
    if group:
        chats = ChatModel.objects.filter(group = group)
        for chat in chats:
            print(chat)
    else:
        return HttpResponse("No Such Available!")

    context = {
        'groupName': groupName,
        'chats': chats,
        'users': users
    }

    return render(request, 'chat.html', context)

