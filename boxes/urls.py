from django.urls import path
from .views import recommend_box

urlpatterns = [
    path('recommend-box/', recommend_box, name='recommend-box'),
]