from django.db import models


class Company(models.Model):
    """
    Energy efficiency measures that could be applied to a property.
    E.g. Loft insulation,
    insulation material deployed in lofts to reduce energy lost through the roof, often 50mm-300mm thick,
    £1000-£2000 for a 3 bed semi-detached house.
    """

    name = models.CharField(max_length=100)
    companies_house_number = models.IntegerField()
    description = models.TextField()
    postcode = models.CharField(max_length=10)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    address3 = models.CharField(max_length=100)
    address4 = models.CharField(max_length=100)
    address5 = models.CharField(max_length=100)
    address6 = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
