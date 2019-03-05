from django.urls import path
from .views import StoreItemListView, StoreItemDetailView
from . import views

urlpatterns = [
    path('', StoreItemListView.as_view(), name='webstore-home'),
    path('item/<int:pk>/', StoreItemDetailView.as_view(), name='item-detail')
]
