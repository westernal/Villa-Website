from re import search
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from quickstart.models import villa
from quickstart.serializers import villaSerializer


class getAllData(APIView):
    def get(self, request):
        query = villa.objects.all()
        serializer = villaSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class updateVilla(APIView):
    def get(self, request, id):
        query = villa.objects.get(id = id)
        serializer = villaSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        query = villa.objects.get(id = id)
        serializer = villaSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class createVilla(APIView):
    def post(self, request):
        serializer = villaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class searchVilla(APIView):
    def get(self, request):
        search = request.GET['name']
        query = villa.objects.filter(name__contains=search) 
        serializer = villaSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    

class deleteVilla(APIView):
    def delete(self, request, id):
        query = villa.objects.get(id=id)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)