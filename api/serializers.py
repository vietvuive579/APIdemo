from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):

    # valid_name = serializers.SerializerMethodField(read_only=False)

    class Meta:
        model = Item
        fields = [
            'uuid',
            'name',
            'desciption',
            'created_date',
            'update_date'
        ]

    # def get_valid_name(self, obj):
    #     condition_name = obj.name.length
    #     if(condition_name < 20 & condition_name > 25):
    #         return obj.name
        

    