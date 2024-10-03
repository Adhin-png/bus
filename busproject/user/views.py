from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView,FormView,DetailView,ListView
from django.urls import reverse_lazy
from user.forms import RegisterForm,SearchBusForm,BookTicketForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View
from owner.models import Bus,Tickets
from django.core.mail import send_mail,settings
from user.forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.db.models import F
# from  owner .models import Route






# Create your views here.
# class Home(TemplateView):
#     template_name='index.html'

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context["bus"]=Bus.objects.all()
#         return context


class UserHome(View):
    def get(self,request):
        # bus=Bus.objects.all()
        return render(request,'index.html')
    def post(self,request):
        if not request.user.is_authenticated:
            messages.error(request, "You need to log in first")
            return redirect('login_view') 
        source=request.POST.get("source")
        destination=request.POST.get("destination")
        date=request.POST.get("date")
        if not source or not destination or not date:
            messages.error(request, 'Please select source, destination, and date')
            return redirect('hom_view')
        


        bus=Bus.objects.filter(source=source,destination=destination,date=date)
        return render(request, 'filter_bus.html', {'buses': bus})
      

class RegisterView(CreateView):
    template_name='user_reg.html'
    form_class=RegisterForm
    success_url=reverse_lazy('hom_view')

    def form_valid(self, form):
        messages.success(self.request, "You have registered successfully!")
        return super().form_valid(form)
        
    


    
    

class LoginView(FormView):
    template_name='log.html'
    form_class=LoginForm

    def post(self,request):
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            messages.success(request,"login succesful")
            return redirect("hom_view")
        else:
            messages.warning(request,"invalid credentials")
            return redirect("hom_view")
  


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, "Logout Successful")
        else:
            messages.error(request, "You are not logged in.")
        return redirect('hom_view')
    
class About(TemplateView):    
    template_name='about.html'


class BusListView(ListView):
    model=Bus
    template_name="bus_list.html"
    context_object_name="bus"

    def get(self,request):
        if not request.user.is_authenticated:
            messages.error(request, "You need to log in first")
            return redirect('login_view') 
        else:
            return super().get(request)

 
    
   


class PaymentView(TemplateView):
    # template_name='payment.html'
    def post(self, request, *args, **kwargs):
       

        bus_id = request.POST.get('bus_id')
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        seats = request.POST.get('seats')

        # Validate that none of the values are missing
        if not all([bus_id, name, phone_number, email, seats]):
            messages.error(request, "Some fields are missing in the payment form.")
            return redirect('book_ticket_view', bus_id=bus_id)

        bus = Bus.objects.get(id=bus_id)


        form_data = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'seats': seats,
            'bus': bus_id,
            'source': bus.source,
            'destination': bus.destination,
            'date': bus.date,
            'time': bus.time,
            'fare': bus.bus_fare,
            # 'total_fare': bus.bus_fare*seats
        }

        form = BookTicketForm(data=form_data)

        # Validate the form before saving
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # Attach the user
            ticket.bus = bus  # Attach the bus
            ticket.fare = bus.bus_fare  # Set fare per seat

            # Check if enough seats are available
            seats = int(seats)  # Convert seats to integer
            
            if bus.seat_remaining < seats:
                messages.error(request, "Not enough seats available!")
                return redirect('book_ticket_view', bus_id=bus_id)

            # Save the ticket
            ticket.save()

            # Update remaining seats
            bus.seat_remaining -= seats
            bus.save()

            # Send confirmation email
            subject = 'Ticket Booking Confirmation'
            message = (
                f'Dear {request.user.username},\n\nYour ticket has been booked successfully.\n\n'
                f'Bus Details:\nBus Name: {bus.bus_name}\nSource: {bus.source}\nDestination: {bus.destination}\n'
                f'Date: {bus.date}\nTime: {bus.time}\nFare: {bus.bus_fare}\n'
                f'Number of Tickets: {seats}\n\nThank you for booking with us.'
            )
            from_email = settings.EMAIL_HOST_USER
            to_email = request.user.email
            send_mail(subject, message, from_email, [to_email])

            # Redirect to success page
            return redirect('success_url')

        else:
            # If form is invalid, render the payment page with the validation errors
            messages.error(request, "There was an error with the data you provided.")
            return render(request, 'payment.html', {
                'form': form,
                'bus_id': bus_id,
                'ticket_data': form_data,
                # 'total_fare': bus.bus_fare*seats
            })



 
# def book_ticket(request):
#     if request.method == 'POST':
#         form = BookTicketForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             phone_number = form.cleaned_data['phone_number']
#             email = form.cleaned_data['email']
#             bus = form.cleaned_data['bus']
            
           
            
#             return redirect('success_url')  
#     else:
#         form = BookTicketForm()

#     return render(request, 'ticket_register.html', {'form': form})

class BookTicketView(CreateView):
    template_name='ticket_register.html'
    form_class=BookTicketForm
    success_url=reverse_lazy('success_url')

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "You need to log in first")
            return redirect('login_view')  
        
        bus_id = kwargs.get('bus_id')
        bus = Bus.objects.get(id=bus_id)
        
        initial_data = {
            'bus': bus,
            'source': bus.source,
            'destination': bus.destination,
            'date': bus.date,
            'time': bus.time,
            'fare': bus.bus_fare,
        }
        form = BookTicketForm(initial=initial_data)

        return render(request, "ticket_register.html", {'form': form}) 
    
    def post(self, request, *args, **kwargs):
        form = BookTicketForm(request.POST)
        
        if form.is_valid():
            bus_id = kwargs.get('bus_id')
            bus = Bus.objects.get(id=bus_id)
            seats = form.cleaned_data.get('seats')
            total_fare = seats * bus.bus_fare
           
            

            return render(request, 'payment.html', {
                'form': form,
                'bus_id': bus_id,
                'ticket_data': form.cleaned_data,
                'total_fare': total_fare 
            })

       
        return render(request, self.template_name, {'form': form})
        
    # def form_valid(self,form):
    #     tickets = form.save(commit=False)
    #     tickets.user = self.request.user  
    #     bus_id = self.kwargs.get('bus_id')
    #     bus = Bus.objects.get(id=bus_id)


    #     number_of_tickets = form.cleaned_data.get('seats')
    #     if bus.seat_remaining < number_of_tickets:
    #         messages.error(self.request, "Not enough seats available!")
    #         return redirect('book_ticket_view', bus_id=bus_id)
        
    #     tickets.bus = bus
    #     tickets.fare = bus.bus_fare
    #     tickets.save()
        
    #     # Update the seat_remaining field
    #     bus.seat_remaining = bus.seat_remaining - number_of_tickets
    #     bus.save()  
        
    #     subject = 'Ticket Booking Confirmation'
    #     message = f'Dear {self.request.user.username},\n\nYour ticket has been booked successfully.\n\n\nBus Details:\nBusname:{bus.bus_name}\nSource: {bus.source}\nDestination: {bus.destination}\nDate: {bus.date}\nTime: {bus.time}\nFare: {bus.bus_fare}\n\nNumber of Tickets: {number_of_tickets}\n\nThank you for booking with us.'
    #     from_email = settings.EMAIL_HOST_USER
    #     to_email = self.request.user.email

    #     send_mail(subject, message, from_email, [to_email])

    #     return super().form_valid(form)
    ###############################################################################################booking without paymnt
        # tickets.bus = bus 
        # tickets.fare = bus.bus_fare
        # tickets.save()
        # Bus.objects.filter(id=bus_id).update(seat_remaining=F('seat_remaining') - 1)
       
        # # messages.success(self.request, "Ticket booked successfully!")
        # return super().form_valid(form)   

       
    
class SuccessView(TemplateView):
    template_name = 'success.html'
    

class FeaturesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'features.html')
    
class BookedTicketView(LoginRequiredMixin,ListView):
    model = Tickets
    template_name = 'ticket_list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        tickets = Tickets.objects.filter(user=self.request.user)
        for ticket in tickets:
            ticket.total_fare = ticket.fare * ticket.seats
        return tickets
    

class CancelTicketView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        ticket_id = kwargs.get('ticket_id')
        tickets = Tickets.objects.get(id=ticket_id)
        if tickets.user == request.user:
            bus = tickets.bus
            
            bus.seat_remaining = bus.seat_remaining + tickets.seats
            bus.save()  #     
            tickets.delete()
            messages.success(request, "Ticket cancelled successfully!")

            subject = 'Ticket Cancellation Confirmation'
            name = tickets.name  # Get the name from the ticket
            message = f'Dear {self.request.user.username},\n\nYour ticket has been cancelled successfully.\n\nBus Details:\nSource: {bus.source}\nDestination: {bus.destination}\nDate: {bus.date}\nTime: {bus.time}\nFare: {bus.bus_fare}\n\nNumber of Tickets: {tickets.seats}\n\nThank you for using our service.'
            from_email = settings.EMAIL_HOST_USER
            to_email = request.user.email
            send_mail(subject, message, from_email, [to_email])
      
            return redirect('user_booked_tickets')
        
        
    
class CancelView(TemplateView):
    template_name = 'cancel.html'



