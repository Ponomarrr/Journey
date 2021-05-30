from django.urls import path
from .views import (
    home, TrainCreateView, TrainDeleteView, TrainUpdateView, TrainDetailView,
)

urlpatterns = [
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('add/', TrainCreateView.as_view(), name='add'),
    path('details/<int:pk>/', TrainDetailView.as_view(), name='details'),
    path('', home, name='home'),
]
