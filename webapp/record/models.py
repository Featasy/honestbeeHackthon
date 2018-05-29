from django.db import models

class Record(models.Model):

    id = models.AutoField(primary_key=True)

    date = models.DateTimeField(auto_now=True)

    honest_url = models.CharField(max_length=100)

    honest_item = models.CharField(max_length=100)

    honest_price =  models.FloatField()

    carre_item = models.CharField(max_length=100)

    carre_price =  models.FloatField()
