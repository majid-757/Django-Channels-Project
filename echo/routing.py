from django.urls import path

from echo import consumers



websocket_urlpatterns = [
    path('ws/', consumers.EchoConsumer),
    path('ws/chat/<str:username>/', consumers.ChatConsumer),
]


