from django.db import models
import datetime

from django.db.models.enums import ChoicesMeta


class BasicDetails (models.Model):
    # (Name, Sex, DOB, Annual income, Email, Mobile number, Occupation) 
    name = models.CharField(max_length = 50, default = None)
    last_name = models.CharField(max_length=50, default=None, null=True, blank=True)
    complete_name = models.CharField(max_length=150, default=None, null=True, blank=True)
    cpf = models.CharField(max_length=50, default=None, blank=True, null=True)
    sex = models.CharField(max_length = 1, default = None)
    annual_income = models.FloatField(default = None)
    email = models.EmailField(default = None)
    mobile = models.IntegerField(default = 0)
    occupation = models.CharField(max_length = 50, default = None)
    DOB = models.DateField('Date of Birthday', default = None)
    user_name = models.EmailField('username...@medbank.com', max_length = 150, default = None)

    def __str__(self):
        return self.user_name

'''
class PresentLocation (models.Model):
    # (Country, State, City, Street, Pincode) 
    country = models.CharField(max_length = 50, default = "India")
    state = models.CharField(max_length = 50)
    city = models.CharField(max_length = 50)
    street = models.CharField(max_length = 50)
    pincode = models.IntegerField()
    user_name = models.CharField(max_length = 150, default = None)
'''


class Status (models.Model):
    account_number = models.IntegerField()
    balance = models.FloatField(default=10000.00)
    user_name = models.CharField(max_length = 150, default = None)

    def __str__(self):
        return self.user_name

class MoneyTransfer(models.Model):
    enter_your_user_name = models.CharField(max_length = 150, default = None)
    enter_the_destination_account_number = models.IntegerField()
    enter_the_amount_to_be_transferred_in_INR = models.FloatField()

    def __str__(self):
        return self.enter_your_user_name