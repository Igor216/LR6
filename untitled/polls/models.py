from django.db import models

# Create your models here.
class UserModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)

class BankModel(models.Model):
    idbank = models.IntegerField(primary_key=True)
    director = models.CharField(max_length=30)
    address = models.CharField(max_length=255)

class TransactionModel(models.Model):
    idtran = models.IntegerField(primary_key=True)
    sum = models.IntegerField()
    type = models.CharField(max_length=50)
    user = models.ForeignKey('UserModel')
    bank = models.ForeignKey('BankModel')
    date = models.DateTimeField()
