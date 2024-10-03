
from django.views.generic import CreateView, UpdateView, DetailView,TemplateView,ListView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from owner.models import Bus
from django.contrib import messages
from owner.models import Bus
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from owner.forms import BusForm,BusUpdateForm
from django.views import View
from django.shortcuts import render,redirect



# Create your views here.

class AdminDash(TemplateView):
    template_name = 'admin_dash.html'

class AddBusView(CreateView):
    model = Bus
    form_class= BusForm
    
    template_name = 'add_bus.html'
    success_url = reverse_lazy('bus_list')  # Redirect to owner's bus list after adding

    def form_valid(self, form):
        messages.success(self.request, "Bus added successfully!")
        return super().form_valid(form)


class BussListView(ListView):
    model = Bus
    template_name = 'owner/bus_list.html'  # You need to create this template
    context_object_name = 'buses'

# Update a bus
class BusUpdateView(UpdateView):
    model = Bus
    form_class = BusForm
    template_name = 'owner/bus_form.html'  # You need to create this template
    success_url = reverse_lazy('owner_bus_list')

    def form_valid(self, form):
        messages.success(self.request, "Bus Updated successfully!")
        return super().form_valid(form)


# Delete a bus
class BusDeleteView(DeleteView):
    model = Bus
    template_name = 'owner/bus_confirm_delete.html'  # You need to create this template
    success_url = reverse_lazy('owner_bus_list')

    def form_valid(self, form):
        messages.error(self.request, "Bus deleted successfully!")
        return super().form_valid(form)






