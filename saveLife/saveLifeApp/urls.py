from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from saveLifeApp import views

urlpatterns = (
    [
        path('', views.login, name="login"),
        path('login', views.login, name="login"),
        path('donor', views.donor, name="donor"),
        path('donation', views.donation, name="donation"),
        path('afterLifeDonation', views.afterDeath, name="afterDeathDonation"),
        path('cashPay', views.cashpayment, name="cashPay"),
        path('payment', views.payment, name="payment"),
        path('pay', views.paymentp, name="paymentP"),
        path('paypal', views.paypal, name="paypal"),

    ]
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
