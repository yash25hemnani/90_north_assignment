from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('login/', views.loginUser, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('start/', views.startPage, name='startPage'),
    path('<str:groupName>/', views.chat, name='chat'),
    path('start-chat/<str:email>', views.startChat, name='startChat'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)