from django.db import models
import uuid
from django.utils import timezone

# Create your models here.

class Invoice(models.Model):
    id            = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
    Invoice_no    = models.IntegerField()
    Date          = models.DateField(default=timezone.now)
    Customer_Name = models.CharField(max_length=255,blank=True, null=True)
    
    def __str__(self):
        return str(self.Invoice_no)

class InvoiceDetail(models.Model):
    invoice     = models.ForeignKey(Invoice, on_delete=models.CASCADE,)
    description = models.TextField()
    quantity    = models.IntegerField()
    unit_price  = models.DecimalField(max_digits=8, decimal_places=2)
    price       = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.invoice)

