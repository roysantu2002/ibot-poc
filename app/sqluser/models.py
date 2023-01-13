from django.conf import settings
from django.db import models
from sql.models import SQLServer

# Create your models here.

"""
SQL user model
"""

class SQLUser(models.Model):
     id = models.BigAutoField(
                auto_created = True,
                unique=True,
                primary_key = True,
                serialize = False,
                verbose_name ='id')
     user_id = models.CharField(max_length=150,  blank=True)
     #server_id = models.CharField(max_length=150,  blank=True)
     server = models.ForeignKey(SQLServer, blank=True, null=True, on_delete=models.CASCADE)
     flag = models.BooleanField()

     def __str__(self) -> str:
          return self.user_id
