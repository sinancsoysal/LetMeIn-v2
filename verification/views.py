from django.shortcuts import render

# Create your views here.
from random import randint

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Verification
from .serializers import VerificationSerializer


class VerificationViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = VerificationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request):
        verification_entry = Verification.objects.get(id=request.data['id'])
        serializer = VerificationSerializer(verification_entry)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request):
        verification_entry = Verification.objects.get(id=request.data['id'])
        serializer = VerificationSerializer(instance=verification_entry, data=request.data)

        if not serializer.is_valid():
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request):
        verification_entry = Verification.objects.get(id=request.data['id'])

        verification_entry.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
