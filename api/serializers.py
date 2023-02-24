from rest_framework import serializers
from projects.models import Project


class projectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
