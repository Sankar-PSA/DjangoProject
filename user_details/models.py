from django.db import models
from django.utils.timezone import now


# Create your models here.

class Registermodel(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=200)
    userid = models.CharField(max_length=200)
    password = models.IntegerField()
    mblenum = models.BigIntegerField()
    email = models.EmailField(max_length=300, null=True)


class AddressTable(models.Model):
    line1 = models.CharField(max_length=300)
    line2 = models.CharField(max_length=300)
    pin = models.IntegerField()
    state = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=False,blank=False)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True,blank=True)
    updated_date = models.DateTimeField(null=True,blank=True)


class Contact_details(models.Model):
    mob = models.BigIntegerField()
    email = models.EmailField(max_length=300, null=True)
    account = models.BigIntegerField()
    beneficiary_name = models.CharField(max_length=300)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=False, blank=False)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

class VendorTable(models.Model):
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=300)
    gst = models.CharField(max_length=300)
    pan = models.CharField(max_length=300)
    branch = models.CharField(max_length=300)
    address = models.ForeignKey(AddressTable, on_delete=models.SET_NULL, null=True)
    contact = models.ForeignKey(Contact_details, on_delete=models.SET_NULL, null=True)
    status = models.SmallIntegerField(default=1)
    created_by = models.IntegerField(null=False, blank=False)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)



