from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from saveLifeApp import views

urlpatterns = (
    [
        path('register', views.register, name="register"),
        path('organreq', views.organRequest, name="organreq"),
    ]
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
