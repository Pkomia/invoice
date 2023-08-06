from rest_framework import serializers

from .models import *

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceDeatailSerializer(serializers.ModelSerializer):
    invoice = InvoiceSerializer(read_only=True)
    class Meta:
        model = InvoiceDetail
        fields = ('invoice', 'description', 'quantity', 'unit_price', 'price')

   
    

 
 