from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.views.decorators.http import require_POST
from .models import Message, CustomUser, Contact,Subscribe
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from rest_framework.views import APIView
from .serializers import AccountSerializer
from .models import CustomUser
from rest_framework.response import Response
from django.http import JsonResponse
import json


@require_POST
def register(request):
    user = json.loads(request.body.decode('utf8'))
    serialized = AccountSerializer(data=user)
    if serialized.is_valid():
        CustomUser.objects.create_user(
            serialized.initial_data['username'],
            serialized.initial_data['email'],
            serialized.initial_data['password'],
        )
        return JsonResponse({'Message': 'Account created successfully !!!!'})

    return JsonResponse({'Message': 'Account not created please try again!!!'})


@require_POST
def post_login(request):
    user_data = json.loads(request.body.decode('utf8'))
    data = user_data
    email = data.get('email')
    password = data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
        token, get_or_create = Token.objects.get_or_create(user=user)
        if user.is_active:
            login(request, user)
            print(request.user)
            return JsonResponse({'Message': 'Login successfully !!!!', 'token': token.key})
        else:
            return JsonResponse({'Message': 'Login fail please try again!!!'})


@require_POST
def send_message(request):
    message_of_user = json.loads(request.body.decode('utf8'))

    if isinstance(message_of_user, dict):
        message_of_user = [message_of_user]

    try:

        for msg in message_of_user:
            message = Message(**msg)
            message.save()
        return JsonResponse({"Message": 'Message send successfully'})

    except Exception as error:
        return JsonResponse({'Message': 'Message not sent', 'error': str(error)})


@require_POST
def send_contact(request):
    message_of_user = json.loads(request.body.decode('utf8'))

    if isinstance(message_of_user, dict):
        message_of_user = [message_of_user]

    try:

        for msg in message_of_user:
            message = Contact(**msg)
            message.save()
        return JsonResponse({"Message": 'Contact_form send successfully'})

    except Exception as error:
        return JsonResponse({'Message': 'Contact_form not sent', 'error': str(error)})


@require_POST
def subscribe(request):
    message_of_user = json.loads(request.body.decode('utf8'))

    if isinstance(message_of_user, dict):
        message_of_user = [message_of_user]

    try:

        for msg in message_of_user:
            message = Subscribe(**msg)
            message.save()
        return JsonResponse({"Message": 'Message send successfully'})

    except Exception as error:
        return JsonResponse({'Message': 'Message not sent', 'error': str(error)})