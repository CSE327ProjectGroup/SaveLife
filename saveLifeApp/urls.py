from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from saveLifeApp import views

urlpatterns = (
    [
        path('', views.login, name="login"),
        path('login', views.login, name="login"),

        path('tpcenter', views.tpcenter, name="tpcenter"),
        path('tpcenterp', views.tpcenterp, name="tpcenterp"),

    ]
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
