from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Game
from .serializers import GameSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def games_list(request, format=None):
    # View to retrieve all created games    
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    

    # View to create a new game
    if request.method == 'POST':
        serializer = GameSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# A View for the games details

@api_view(['PUT', 'GET', 'DELETE'])
def game_detail(request,id, format=None):
    try:
        game = Game.objects.get(pk=id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = GameSerializer(game)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)