from rest_framework import serializers
import models as tableTennisModels


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = tableTennisModels.Player
        fields = '__all__'


class DuoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tableTennisModels.Duo
        fields = '__all__'
