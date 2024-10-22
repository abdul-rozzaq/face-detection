from django.urls import path
from .views import RecognizeAPIView


urlpatterns = [
    path("recognize", RecognizeAPIView.as_view()),
]
