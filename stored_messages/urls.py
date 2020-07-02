"""
At the moment this module does something only when restframework is available
"""
from django.conf import settings

app_name = "stored_messages"


if 'rest_framework' in settings.INSTALLED_APPS:
    from rest_framework.routers import DefaultRouter
    from django.conf.urls import url, include
    from . import views

    router = DefaultRouter()
    router.register(r'inbox', views.InboxViewSet, base_name='inbox')

    urlpatterns = [
        url(r'^', include(router.urls)),
        url(r'^mark_all_read/$', views.mark_all_read, name='mark_all_read'),
    ]
