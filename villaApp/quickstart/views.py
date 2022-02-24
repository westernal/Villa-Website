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
    def get(self, request, primaryKey):
        query = villa.objects.get(primaryKey = primaryKey)
        serializer = villaSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, primaryKey):
        query = villa.objects.get(primaryKey = primaryKey)
        serializer = villaSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)    

class createVilla(APIView):
    def post(self, request):
        serializer = villaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)   