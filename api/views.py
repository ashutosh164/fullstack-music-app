from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer


class RoomView(generics.ListAPIView):  #here actual not rendering the view its creating the view
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


