from django.urls import path
from .views import (UserListCreateAPIView,UserRetrieveUpdateDestroyAPIView,CurrencyListCreateAPIView,CurrencyRetrieveUpdateDestroyAPIView, WalletListCreateAPIView,WalletRetrieveUpdateDestroyAPIView)

urlpatterns = [
    #User
    path('users/', UserListCreateAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    #Currency
    path('currency/', CurrencyListCreateAPIView.as_view(), name='currency-list'),
    path('currency/<int:pk>/', CurrencyRetrieveUpdateDestroyAPIView.as_view(), name='currency-detail'),
    #Wallet
    path('wallet/', WalletListCreateAPIView.as_view(), name='wallet-list'),
    path('wallet/<int:pk>/', WalletRetrieveUpdateDestroyAPIView.as_view(), name='wallet-detail'),
    
    ]