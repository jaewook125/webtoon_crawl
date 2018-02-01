from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('list/', views.webtoon_list, name="webtoon_list"),
]