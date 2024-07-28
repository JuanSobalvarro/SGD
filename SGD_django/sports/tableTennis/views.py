from django.shortcuts import render
import models as tableTennisModels
import serializers as tableTennisSerializers

from rest_framework import permissions, viewsets


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = tableTennisModels.Player.objects.all()
    serializer_class = tableTennisSerializers.PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        player = serializer.save(user=self.request.user)
        return player


class DuoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = tableTennisModels.Duo.objects.all()
    serializer_class = tableTennisSerializers.DuoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        duo = serializer.save(user=self.request.user)
        return duo


def tableTennisHome(request):
    return render(request, 'tableTennis/tableTennis_home.html')
