from django.shortcuts import render

# Create your views here.
from random import randint

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Verification, ShortenedId
from .serializers import VerificationSerializer, ShortenedIdSerializer


class VerificationViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = VerificationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

        verification_entry = serializer.save()

        return Response(verification_entry.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        verification_entry = Verification.objects.get(id=pk)
        serializer = VerificationSerializer(verification_entry)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        verification_entry = Verification.objects.get(id=pk)
        serializer = VerificationSerializer(instance=verification_entry, data=request.data)

        if not serializer.is_valid():
            return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        verification_entry = Verification.objects.get(id=pk)

        verification_entry.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
