from django.urls import path
from .views import menu

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('checkout/', views.checkout_submit, name='checkout_submit'),
]
