from django.db import models
#from customer.models import customer

STATES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam' , 'Assam'),
    ('Bihar' , 'Bihar'),
    ('Chhattisgarh' , 'Chhattisgarh'),
    ('Goa' , 'Goa'),
    ('Gujarat' , 'Gujarat'),
    ('Haryana' , 'Haryana'),
    ('Himanchal Pradesh' , 'Himanchal Pradesh'),
    ('Jammu & Kashmir' , 'Jammu & Kashmir'),
    ('Jharkhand' , 'Jharkhand'),
    ('Karnataka' , 'Karnataka'),
    ('Kerala' , 'Kerala'),
    ('Madhya Pradesh' , 'Madhya Pradesh'),
    ('Maharashtra' , 'Maharashtra'),
    ('Manipur' , 'Manipur'),
    ('Meghalaya' , 'Meghalaya'),
    ('Mizoram' , 'Mizoram'),
    ('Nagaland' , 'Nagaland'),
    ('Odisha' , 'Odisha'),
    ('Punjab' , 'Punjab'),
    ('Rajasthan' , 'Rajathan'),
    ('Sikkim' , 'Sikkim'),
    ('Tamil Nadu' , 'Tamil Nadu'),
    ('Telangana' , 'Telangana'),
    ('Tripura' , 'Tripura'),
    ('Uttarakhand' , 'Uttarakhand'),
    ('Uttar Pradesh' , 'Uttar Pradesh'),
    ('West Bengal' , 'West Bengal')
    )

class Pharmacy(models.Model):
    pharmacy_id = models.CharField(max_length=20,primary_key=True)
    pharmacy_name = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    owner_fname = models.CharField(max_length=50)
    owner_lname = models.CharField(max_length=50)
    vat_no = models.ImageField()
    drug_license = models.ImageField()
    address_street = models.TextField()
    address_city = models.CharField(max_length=20)
    address_state = models.CharField(max_length=20,choices=STATES)
    address_pincode = models.IntegerField()


    def __str__(self):
        return self.pharmacy_id

class contact_pharmacy(models.Model):
    pharmacy = models.ForeignKey(Pharmacy,on_delete=models.CASCADE)
    contact_no = models.BigIntegerField()
    default=models.BooleanField(default=False)

