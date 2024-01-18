from django.urls import re_path as url
from django.urls import path, include
from invoiceapp import views


urlpatterns = [
    path('invoice/', views.InvoiceApiView.as_view()),
    path('invoice/<str:id>', views.InvoiceApiView.as_view()),
    path('invoice_detail/', views.InvoiceDetailApiView.as_view()),
    path('invoice_detail/<str:id>', views.InvoiceDetailApiView.as_view()),
]