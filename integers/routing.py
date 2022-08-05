from django.urls import path

from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/int_url/', WSConsumer.as_asgi())
]