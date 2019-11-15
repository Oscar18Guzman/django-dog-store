from django.db import models
from datetime import datetime
from django import forms


class DogProduct(models.Model):
    name = models.TextField()
    product_type = models.TextField()
    dog_size = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()


class Purchase(models.Model):
    dog_product = models.ForeignKey(DogProduct, on_delete=models.PROTECT)
    purchased_at = models.DateTimeField()


class DogTag(models.Model):
    owner_name = models.TextField()
    dog_name = models.TextField()
    dog_birthday = models.DateField()


class NewDogTagForm(forms.Form):
    owner_name = forms.CharField()
    dog_name = forms.CharField()
    dog_birthday = forms.DateField()


class NewDog(models.Model):
    dog_type = models.TextField()
    dog_name = models.TextField()
    dog_birthday = models.DateField()

class NewDogForm(forms.Form):
    dog_type = forms.CharField()
    dog_name = forms.CharField()
    dog_birthday = forms.DateField()