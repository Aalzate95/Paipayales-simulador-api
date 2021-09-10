from django.db.models import Model, CASCADE, DO_NOTHING, SET_NULL
from django.db.models import ForeignKey, OneToOneField, ManyToManyField
from django.db.models import (
    CharField,
    IntegerField,
    FloatField,
    DateTimeField,
    TimeField,
    BooleanField,
    FileField,
    UUIDField,
    DateField
)
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse


class Pools(Model):
    name= CharField(max_length=5,blank=False)
    pool_type_choices = (("1","1"),("2","2"))
    pool_type = CharField(max_length=5,choices=pool_type_choices,default="1")
    size=FloatField(null=True,blank=False)

    def __str__(self):
        return f"{self.name,self.pool_type,self.size}"