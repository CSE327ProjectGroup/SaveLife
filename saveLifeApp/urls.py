from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from saveLifeApp import views

urlpatterns = (
    [

        path('fundRaise', views.fundRaise, name="fundRaise"),

        path('cashPay', views.cashPayment, name="cashPay"),
        path('payment', views.payment, name="payment"),
        path('pay', views.paymentP, name="paymentP"),
        path('paypal', views.paypal, name="paypal"),

    ]
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
