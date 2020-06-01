from django.contrib.auth.models import User
from django.db import models
import uuid


class RealCharField(models.Field):
    def db_type(self, connection):
        return 'CHAR'


class Country(models.Model):
    name = models.CharField(max_length=50)
    country_code = RealCharField(max_length=3)

    def __str__(self):
        return f'name={self.name} - country_code={self.country_code}'


class City(models.Model):
    name = models.CharField(max_length=26)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    def __str__(self):
        return f'name={self.name} - country={self.country}'


class Zip(models.Model):
    zip = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return f'zip_code={self.zip} - city={self.city}'


class Property(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    address = models.CharField(max_length=100)
    zip = models.ForeignKey(Zip, on_delete=models.PROTECT)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'title={self.title} - price={self.price} - address={self.address} - zip={self.zip} - owner={self.owner}'


class PropertyImg(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    img = models.ImageField()
    order = models.IntegerField()

    def __str__(self):
        return f'property={self.property} - img={self.img} - order={self.order}'


class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'property={self.property} - customer={self.customer} - start_date={self.start_date} - ' \
               f'end_date={self.end_date}'


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'name={self.name}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    address = models.CharField(max_length=100)
    zip = models.ForeignKey(Zip, on_delete=models.PROTECT)

    def __str__(self):
        return f'user={self.user} - role={self.role} - address={self.address} - zip={self.zip}'
