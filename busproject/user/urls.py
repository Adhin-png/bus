from django.urls import path
from user import views
from.views import BookedTicketView,CancelTicketView



urlpatterns=[
    path('',views.UserHome.as_view(),name='hom_view'),
    path('registration',views.RegisterView.as_view(),name='regi_view'),
    path('login',views.LoginView.as_view(),name='login_view'),
    path('logout',views.LogoutView.as_view(),name='logout_view'),
    path('about',views.About.as_view(),name='about_view'),
    path('buses',views.BusListView.as_view(),name='bus_list'),
    path('book-ticket/<int:bus_id>/',views.BookTicketView.as_view(), name='book_ticket_view'),
    path('success/', views.SuccessView.as_view(), name='success_url'),
    path('features',views.FeaturesView.as_view(),name='our_feautures'),
    path('listtickets/',BookedTicketView.as_view(), name='user_booked_tickets'),
    path('cancel_ticket/<int:ticket_id>/', CancelTicketView.as_view(), name='cancel_ticket_view'),
    path('payment',views.PaymentView.as_view(),name='payment_view'),
    


    # path('payment/', views.SuccessView.as_view(), name='payment_url'),
    
    

     






]