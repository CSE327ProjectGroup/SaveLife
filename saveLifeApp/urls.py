from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from saveLifeApp import views

urlpatterns = (
    [
        path('volunteer', views.volunteer, name="volunteer"),
        path('search', views.search, name="search"),

    ]
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
