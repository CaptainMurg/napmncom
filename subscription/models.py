from django.db import models

class Distribution(models.Model):
    name = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(unique=True, max_length=3)

    def __str__(self):
        return self.name

class Rate(models.Model):
    distribution = models.ForeignKey(Distribution)
    currency = models.ForeignKey(Currency)
    months = models.IntegerField()
    price = models.IntegerField()

class ExchangeRate(models.Model):
    currency = models.ForeignKey(Currency)
    percent = models.FloatField()
