from django.db import models


class Company(models.Model):
    """
    Company details for businesses signing up to the platform
    """

    name = models.CharField(max_length=100)
    companies_house_number = models.IntegerField()
    description = models.TextField()
    role = models.CharField(
        max_length=100
    )  # Role of the company on the platform i.e. supplier, consumer, etc.
    supply_license = models.IntegerField(max_length=100)  # Ofgem supply license number
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
