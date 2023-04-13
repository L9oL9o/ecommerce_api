from django.contrib.postgres.fields import HStoreField
from django.db.models import Model, CharField, ForeignKey, TextField, DecimalField, CASCADE

from shared.django import TimeBaseModel


class Category(Model):
    name = CharField(max_length=255)

    class Meta:
        db_table = 'Category'


class Product(TimeBaseModel):
    name = CharField(max_length=255)
    price = DecimalField(max_digits=9, decimal_places=2)
    category = ForeignKey(Category, CASCADE)
    desc = TextField()
    details = HStoreField()

    class Meta:
        db_table = 'Product'


class Order(TimeBaseModel):
    name = CharField(max_length=255)

    class Meta:
        db_table = 'Order'


class Discount (Model):
    name = CharField(max_length=255)
    product = ForeignKey(Product, CASCADE)

    class Meta:
        db_table = 'Discount'

