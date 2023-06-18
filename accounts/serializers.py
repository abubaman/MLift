#accounts/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ('username','clg_start','clg_end','clg_type','clg_iter','attend','success_fail',)