from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('consult/<int:patient_id>/', views.consult_patient, name='consult_patient'),
    path('hospitalize/<int:consultation_id>/', views.hospitalize_patient, name='hospitalize_patient'),
    path('examinations/', views.examination_list, name='examination_list'),
    path('sell/<int:product_id>/', views.sell_product, name='sell_product'),
    path('register_admin/', views.register_admin, name='register_admin'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_room/', views.add_room, name='add_room'),
    path('product_list/', views.product_list, name='product_list'),  # Assuming you have a product list view
    path('room_list/', views.room_list, name='room_list'),
]
