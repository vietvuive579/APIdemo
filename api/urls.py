from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.getData),
    path('add/', views.addItem),
    path('detail/<uuid:pk>', views.item_detail)
]
