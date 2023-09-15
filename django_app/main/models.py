#from django.db import models
from django.contrib.auth.models import User
'''
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    company_name = models.CharField(max_length=100)
    full_addres = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Person: {self.company_name}"
'''