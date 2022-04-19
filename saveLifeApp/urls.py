from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from saveLifeApp import views

urlpatterns = (
    [
        path('', views.login, name="login"),
        path('login', views.login, name="login"),
        path('register', views.register, name="register"),
        path('patient', views.patient, name="patient"),
        path('patientlist', views.patientList, name="patientlist"),
        path('donor', views.donor, name="donor"),
        path('donation', views.donation, name="donation"),
        path('afterlifedonation', views.afterDeath, name="afterdeathdonation"),
        path('volunteer', views.volunteer, name="volunteer"),
        path('search', views.search, name="search"),
        path('tpcenter', views.tpCenter, name="tpcenter"),
        path('tpcenterp', views.tpCenterPatient, name="tpcenterp"),
        path('organreq', views.organRequest, name="organreq"),
        path('fundraise', views.fundRaise, name="fundraise"),
        path('forgetpass', views.forgetPass, name="forgetpass"),
        path('cashpay', views.cashPayment, name="cashpay"),
        path('payment', views.payment, name="payment"),
        path('pay', views.paymentPatient, name="paymentp"),
        path('paypal', views.paypal, name="paypal"),
        path('about', views.about, name="about"),
        path('aboutus', views.aboutPatient, name="aboutp"),
        path('contact', views.contact, name="contact"),
        path('contactus', views.contactPatient, name="contactp"),
    ]
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
