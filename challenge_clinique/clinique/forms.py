from django import forms
from .models import Consultation, Hospitalisation, Examination, Patient, Sale,Product,Room
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['notes']


class HospitalisationForm(forms.ModelForm):
    class Meta:
        model = Hospitalisation
        fields = ['room', 'end_date']


class ExaminationForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = ['exam_type', 'results']


class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = True
        if commit:
            user.save()
        return user


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'address', 'phone_number']


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'quantity']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'stock_quantity']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['number', 'capacity']
