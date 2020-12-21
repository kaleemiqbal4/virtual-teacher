from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from login.models import User
from login.serializers import UserSerializer
from rest_framework.decorators import api_view
from login.login_business import loginBusiness

@api_view(['POST'])
def user_list(request):

    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            name = loginBusiness.userInfo(user_data.get('first_name'))
            user_serializer.first_name = name
            print('hello called second ' + name)
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


