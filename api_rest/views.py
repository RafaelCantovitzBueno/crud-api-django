from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        users = User.objects.all() # Get all objects in User's database (It returns a querryset)

        serializer = UserSerializer(users, many=True) # Serialize the object data into json (Has a 'many' parameter cause it's a querryset)
        return Response(serializer.data) # Return the serialized data
    
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_nick(request, nick):
    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

# CRUD  
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):
    if request.method == 'GET':
        try:
            if request.GET['user']: # Check if there is a get parameter called 'user'
                user_nickname = request.GET['user'] # Find get parameter
                try:
                    user = User.objects.get(pk=user_nickname) # Get the object in database
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND) # User not found
                serializer = UserSerializer(user) # Serialize the object data into json
                return Response(serializer.data) # Return the serialized data
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)