from django.urls import path
from . import views

urlpatterns = [
    path('', views.jop_list),
    path('<int:id>', views.jop_detail),
]