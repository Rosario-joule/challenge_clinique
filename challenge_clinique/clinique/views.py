from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Patient, Consultation, Hospitalisation, Room, Examination, Product, Sale
from .forms import ConsultationForm, HospitalisationForm, AdminRegistrationForm, PatientForm, SaleForm, ProductForm, \
    RoomForm
from django.contrib.auth import login, authenticate


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Assuming you have a product list view
    else:
        form = ProductForm()
    return render(request, 'clinique/add_product.html', {'form': form})


def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')  # Assuming you have a room list view
    else:
        form = RoomForm()
    return render(request, 'clinique/add_room.html', {'form': form})


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'clinique/patient_list.html', {'patients': patients})


def consult_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.patient = patient
            consultation.save()
            patient.consulted = True
            patient.save()
            return HttpResponseRedirect('/')
    else:
        form = ConsultationForm()
    return render(request, 'clinique/consult_patient.html', {'form': form})


def hospitalize_patient(request, consultation_id):
    consultation = get_object_or_404(Consultation, id=consultation_id)
    if request.method == 'POST':
        form = HospitalisationForm(request.POST)
        if form.is_valid():
            hospitalisation = form.save(commit=False)
            hospitalisation.consultation = consultation
            if hospitalisation.room.is_full():
                form.add_error(None, "La salle est pleine")
            else:
                hospitalisation.save()
                return HttpResponseRedirect('/')
    else:
        form = HospitalisationForm()
    return render(request, 'clinique/hospitalize_patient.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'clinique/product_list.html', {'products': products})


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'clinique/room_list.html', {'rooms': rooms})


def examination_list(request):
    examinations = Examination.objects.all()
    return render(request, 'clinique/examination_list.html', {'examinations': examinations})


def register_admin(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('patient_list')
    else:
        form = AdminRegistrationForm()
    return render(request, 'clinique/register_admin.html', {'form': form})


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'clinique/add_patient.html', {'form': form})


def sell_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.product = product
            if sale.quantity > product.stock_quantity:
                form.add_error('quantity', 'Quantité insuffisante en stock')
            else:
                product.stock_quantity -= sale.quantity
                product.save()
                sale.save()
                return redirect('product_list')
    else:
        form = SaleForm()
    return render(request, 'clinique/sell_product.html', {'form': form, 'product': product})
