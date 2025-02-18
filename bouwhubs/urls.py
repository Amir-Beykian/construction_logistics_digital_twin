from django.urls import path
from .views import BouwhubListCreateView

urlpatterns = [
    path('', BouwhubListCreateView.as_view(), name='bouwhubs'),
]
