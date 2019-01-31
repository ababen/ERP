from django.db import models
from django.contrib.auth.models import User

class Object(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class ObjectProperties(models.Model):
    properties_data_fk = models.ForeignKey(ObjectPropertiesData, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description =  models.CharField(max_length=250)
    property_type_code = models.CharField(max_length=250)


class ObjectPropertyTypes(models.Model):
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    connected_table_name = models.CharField(max_length=250)
    connected_table_key = models.CharField(max_length=250)
    connected_table_value = models.CharField(max_length=250)


class ObjectPropertiesData(models.Model):
    properties_fk = models.ForeignKey(ObjectProperties, on_delete=models.CASCADE)
    intake_fk = models.ForeignObject(Object, on_delete=models.CASCADE)
    data_int = models.SmallIntegerField()
    data_bitint = models.BigIntegerField()
    data_float = models.FloatField()
    data_datetime = models.DateTimeField()
    data_string = models.CharField(max_length=250)
    created = models.ForeignKey(User, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)