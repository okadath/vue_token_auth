from rest_framework import serializers
from user_account.models import *
from rest_framework import permissions
# from django.contrib.auth.models import User
# para que serialize los countries como parte de sus elementos
# from django_countries.serializers import CountryFieldMixin 


class ProfileSerializer( serializers.ModelSerializer):
# class ProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    # picture = serializers.FileField(required=False)

    # username = serializers.CharField(source='user.username' ,required=True )
    user=serializers.StringRelatedField(read_only=True, required=False)
    class Meta:
        model = Profile
        fields="__all__"
        # fields = ["id", 'picture'] 