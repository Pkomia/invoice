from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
# from rest_framework import authentication, permissions
# from rest_framework.generics import get_object_or_404

from .serializers import *
from .models import *


class InvoiceApiView(APIView):
    """
    View class for listing all, and creating a new post, endpoint: /posts/
    """
    def get(self, request, format=None) -> Response:
        """ For listing out the posts, HTTP method: GET """
        posts = Invoice.objects.all()
        # Passing the queryset through the serializer
        serializer = InvoiceSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        """ For creating a new post, HTTP method: POST """

        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvoiceDetailApiView(APIView):
    """
    View class for listing all, and creating a new post, endpoint: /posts/
    """
    def get(self, request, format=None) -> Response:
        """ For listing out the posts, HTTP method: GET """
        posts = InvoiceDetail.objects.all()
        # Passing the queryset through the serializer
        serializer = InvoiceDeatailSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None) -> Response:
        """ For creating a new post, HTTP method: POST """

        serializer = InvoiceDeatailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 