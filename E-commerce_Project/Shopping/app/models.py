from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

from django.contrib.auth.models import User

# class User(models.Model):
#     username=models.CharField(max_length=100)
#     password=models.CharField(max_length=100)
#     first_name=models.CharField(max_length=70)

STATE_CHOICE=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Ladakh','Ladakh'),
    ('Lakshadweep','Lakshadweep'),
    ('Puducherry', 'Puducherry'),
)


class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=70)
    locality=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    zipcode=models.IntegerField()
    state=models.CharField(max_length=30,choices=STATE_CHOICE)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW', 'Bottom Wear'),


)

class Product(models.Model):
    title = models.CharField(max_length=70)
    selling_price = models.FloatField(max_length=100)
    discounted_price = models.FloatField(max_length=70)
    description = models.TextField()
    brand = models.CharField(max_length=70)
    product_image = models.ImageField(upload_to='productimg')
    category = models.CharField(max_length=2,choices=CATEGORY_CHOICES)


    def __str__(self):
        return str(self.id)


STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way', 'On the Way'),
    ('Cancel','Cancel'),
    ('Delivered','Delivered'),

)

class Orderedplace(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')


class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return str(self.id)