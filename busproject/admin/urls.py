from django.urls import path
from admin import views

urlpatterns=[
    path('admin',views.AdminDashboard.as_view(),name='admin_view'),
]