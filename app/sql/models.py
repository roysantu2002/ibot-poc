"""
ldn databse moels
"""

from django.db import models

# Create your models here.

"""
SQL server model
"""

class SQLServer(models.Model):
     id = models.BigAutoField(
                auto_created = True,
                unique=True,
                primary_key = True,
                serialize = False,
                verbose_name ='id')
     server_id = models.CharField(max_length=150,  blank=True,  unique=True)
     is_active = models.BooleanField()

     # class Meta:
     #    constraints = [
     #        models.CheckConstraint(
     #            check=models.Q(server_id__length__gte=10),
     #            name="%(app_label)s_%(class)s_server_id_length",
     #        )
     #    ]

     def __str__(self) -> str:
          return self.server_id
