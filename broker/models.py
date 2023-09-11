from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models


# Create your models here.
class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    email = models.CharField (max_length = 200, null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    country = models.CharField (max_length = 200, null = True)
    gender = models.CharField (max_length = 200, null = True)

    def __str__(self):
        return self.name


class Deposit (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    btc = models.CharField (max_length = 200,  null = True, default = "0.00",)
    profit_usd = models.CharField (max_length = 200,  null = True, default = "0.00",)
    usd = models.CharField (max_length = 200, default = "0.00",)
    bonus_usd = models.CharField (max_length = 200, default = "0.00",)
    gift_cards = models.CharField (max_length = 200, default = "0.00",)
    verify = models.CharField (max_length = 200, default = "Unverified",)



    def __str__(self):
        return self.name


class Profile (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    profile_pic = models.ImageField (default = "avater.png", null = True, blank = True)


    def __str__(self):
        return self.name


class Account (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    account_number = models.CharField (max_length = 200,  null = True, default = "0.00",)
    account_name = models.CharField (max_length = 200, default = "0.00",)
    bank_name = models.CharField (max_length = 200, default = "0.00",)
    swift_code = models.CharField (max_length = 200, default = "0.00",)
    bitcoin_address = models.CharField (max_length = 200,  null = True, default = "0.00",)
    ethereum_address = models.CharField (max_length = 200, default = "0.00",)
    cashapp_tag = models.CharField (max_length = 200, default = "0.00",)
    paypal_email = models.CharField (max_length = 200, default = "0.00",)


    def __str__(self):
        return self.name


class Transaction (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    number = models.CharField (max_length = 200, default = "1",)
    tf_type = models.CharField (max_length = 200, default = "-",)
    amount = models.CharField (max_length = 200, default = "-",)
    status = models.CharField (max_length = 200, default = "-",)
    date_time = models.CharField (max_length = 200, default = "-",)


    def __str__(self):
        return self.name

class Transactionone (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    number = models.CharField (max_length = 200, default = "2",)
    tf_type = models.CharField (max_length = 200, default = "-",)
    amount = models.CharField (max_length = 200, default = "-",)
    status = models.CharField (max_length = 200, default = "-",)
    date_time = models.CharField (max_length = 200, default = "-",)



    def __str__(self):
        return self.name

class Transactiontwo (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    number = models.CharField (max_length = 200, default = "3",)
    tf_type = models.CharField (max_length = 200, default = "-",)
    amount = models.CharField (max_length = 200, default = "-",)
    status = models.CharField (max_length = 200, default = "-",)
    date_time = models.CharField (max_length = 200, default = "-",)


    def __str__(self):
        return self.name


class Transactionthree (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    number = models.CharField (max_length = 200, default = "4",)
    tf_type = models.CharField (max_length = 200, default = "-",)
    amount = models.CharField (max_length = 200, default = "-",)
    status = models.CharField (max_length = 200, default = "-",)
    date_time = models.CharField (max_length = 200, default = "-",)


    def __str__(self):
        return self.name

class Wallet (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    btc = models.CharField (max_length = 200, default = "4",)
    eth = models.CharField (max_length = 200, default = "-",)
    usdt = models.CharField (max_length = 200, default = "-",)
    usdc = models.CharField (max_length = 200, default = "-",)


    def __str__(self):
        return self.name