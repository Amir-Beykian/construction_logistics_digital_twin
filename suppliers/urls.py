from django.urls import path
from .views import SupplierListCreateView, supplier_locations

urlpatterns = [
    path('', SupplierListCreateView.as_view(), name='suppliers'),
    path('locations/', supplier_locations, name='supplier-locations'),

]
