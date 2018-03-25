from django.db import models



class customer(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    cart_id = models.IntegerField(default=0)


class address_list(models.Model):
    username = models.ForeignKey(customer, on_delete=models.CASCADE)
    address_street = models.TextField()
    address_city = models.CharField(max_length=20)
    address_state = models.CharField(max_length=20)
    address_pincode = models.IntegerField()
    default = models.BooleanField(default=False)


class contact_customer(models.Model):
    username = models.ForeignKey(customer, on_delete=models.CASCADE)
    contact_no = models.BigIntegerField()


