from django.urls import path

from echo import consumers



websocket_urlpatterns = [
    path('ws/', consumers.EchoConsumer),
    path('ws/chat/<str:username>/', consumers.ChatConsumer),
    path('ws/chat2/<str:username>/', consumers.ChatConsumer2),

]


