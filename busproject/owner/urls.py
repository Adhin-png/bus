from django.urls import path
from . import views
from owner.views import AddBusView,BusDeleteView,BusUpdateView,BussListView

urlpatterns=[
    path('owner',views.AdminDash.as_view(),name='owner'),
    path('addbus',AddBusView.as_view(), name='add_bus'),
    path('buses/', BussListView.as_view(), name='owner_bus_list'),
    path('bus/delete/<int:pk>/', BusDeleteView.as_view(), name='bus_delete'),
    path('bus/update/<int:pk>/', BusUpdateView.as_view(), name='bus_update'),

   
    


   
    
  
   
 ]

