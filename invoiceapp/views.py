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
    def get(self, request, id=None, format=None) -> Response:
        """ For listing out the posts, HTTP method: GET """
        if id is not None:
            post= Invoice.objects.get(id=id)
            serializer = InvoiceSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)

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
    
    def put(self, request, id=None, format=None):
        
        invoice=Invoice.objects.get(id=id)
        serializer= InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):

        invoice= Invoice.objects.get(id=id)
        invoice.delete()
        return Response(status= status.HTTP_200_OK)


class InvoiceDetailApiView(APIView):
    """
    View class for listing all, and creating a new post, endpoint: /posts/
    """
    def get(self, request, id=None, format=None) -> Response:
        """ For listing out the posts, HTTP method: GET """

        if id is not None:
            invoc= Invoice.objects.get(id=id)
            post= InvoiceDetail.objects.get(invoice=invoc)
            serializer = InvoiceDeatailSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
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
    
    def put(self, request, id, format=None):

        invoc= Invoice.objects.get(id=id)
        invocDetail= InvoiceDetail.objects.get(invoice= invoc)
        serializer= InvoiceDeatailSerializer(invocDetail, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):

        invoc= Invoice.objects.get(id=id)
        invoicDetail= InvoiceDetail.objects.get(invoice= invoc)

        invoicDetail.delete()
        return Response(status= status.HTTP_200_OK)



 


    
 