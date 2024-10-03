from django import forms
from owner.models import Bus


class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_name', 'seat_available','seat_remaining', 'source', 'destination', 'bus_fare', 'date', 'time','cancellation_policy','refund_policy',]
        widgets = {
            'bus_name': forms.TextInput(attrs={'class': 'form-control'}),
            'seat_available': forms.NumberInput(attrs={'class': 'form-control'}),
            'seat_remaining':forms.NumberInput(attrs={'class':'form-control'}),
            'source': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'bus_fare': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'cancellation_policy': forms.TextInput(attrs={'class': 'form-control'}),
            'refund_policy': forms.TextInput(attrs={'class': 'form-control'}),
            

           

        }


class BusUpdateForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_name', 'source', 'destination', 'date', 'time', 'bus_fare', 'seat_available','seat_remaining','cancellation_policy','refund_policy',]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),

        }


        