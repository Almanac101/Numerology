from pyexpat import model
from django.db import models


# Create your models here.
class site_visitor(models.Model):
    first_name=models.CharField(max_length=50)
    email_address=models.CharField(max_length=50)

    def _str_(self):
        return self.site_visitor


class AlphaGuide(models.Model):
    Letter_Position = models.CharField(max_length=30)
    Attribute = models.TextField(max_length=700)

    def _str_(self):
        return self.Attributes
        

class Alphatables(AlphaGuide):
    pass
