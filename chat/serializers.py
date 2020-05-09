from rest_framework import serializers
from .models import Message, Contact, CustomUser
from . import models


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['name', 'email', 'message']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'sender','subject' 'message']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'password')
