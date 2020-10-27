from django.shortcuts import render

from rest_framework import generics, viewsets
from user_account.serializers import *
# from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
# from user_account.utils.permissions import IsOwnerProfileOrReadOnly, CurrentUserOrAdmin
from user_account.models import  *
from user_account.serializers import *
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework.response import Response
from rest_framework import status, filters
from django.contrib.auth.models import User
import django_filters.rest_framework



# https://stackoverflow.com/questions/57382779/how-to-make-swagger-schema-for-file-upload-api-in-django-rest-framework-using-dr
# @swagger_auto_schema(operation_description='Upload file...',)
class ProfileData(viewsets.ModelViewSet):
	"""
	test endpints profile
	"""
	# #permission_classes = (permissions.IsAuthenticated,)
	# parser_classes = (FileUploadParser,)
	
	parser_classes = (MultiPartParser,)
	permission_classes = [AllowAny]
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	http_method_names = ['get', 'put',"delete","patch"]
	# filter_backends = (filters.SearchFilter,)
	# filter_backends = [rest_framework.DjangoFilterBackend,]
	# lookup_field = 'lang'