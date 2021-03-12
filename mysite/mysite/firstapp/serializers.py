# serializers.py

from rest_framework import serializers
from .models import getdata

class getdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = getdata
        fields = ('id','Email')
