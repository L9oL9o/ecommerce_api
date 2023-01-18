from django.contrib.postgres.fields import HStoreField
from django.db.models import Model, CharField, ForeignKey, TextField, DecimalField, CASCADE

from shared.django import TimeBaseModel


class Category(Model):
    name = CharField(max_length=255)


class Product(TimeBaseModel):
    name = CharField(max_length=255)
    category = ForeignKey(Category, CASCADE)
    desc = TextField()
    price = DecimalField(max_digits=9, decimal_places=2)
    details = HStoreField()


class Order(TimeBaseModel):
    name = CharField(max_length=255)
