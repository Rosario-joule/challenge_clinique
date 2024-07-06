from django.db import models


# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    consulted = models.BooleanField(default=False)


class Consultation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()


class Hospitalisation(models.Model):
    consultation = models.OneToOneField(Consultation, on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)


class Examination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    results = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField()
    #price = models.DecimalField(max_digits=10, decimal_places=2,default='any_name')

    def sell(self, quantity):
        if self.stock_quantity >= quantity:
            self.stock_quantity -= quantity
            self.save()
            return True
        return False


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default='any_name')

    def save(self, *args, **kwargs):
        if self.product.sell(self.quantity):
            super().save(*args, **kwargs)
        else:
            raise ValueError("Pas assez de stock pour la vente")


class Room(models.Model):
    number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField(default=5)
    #current_occupancy = models.PositiveIntegerField(default=0)

    def is_full(self):
        return 3 >= self.capacity

    def __str__(self):
        return f"Room {self.number}"
