from django.urls import path
from .views import BouwhubListCreateView, bouwhub_locations

urlpatterns = [
    path('', BouwhubListCreateView.as_view(), name='bouwhubs'),
    path('locations/', bouwhub_locations, name='bouwhub-locations'),

]
