from django.urls import path
from .views import home, CityDetailView

urlpatterns = [
    path('details/<int:pk>/', CityDetailView.as_view(), name='details'),
    path('', home, name='home'),
    # path('<int:pk>/', CityDetailView.as_view(), name='home'),
]
