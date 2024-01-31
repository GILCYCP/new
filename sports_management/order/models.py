from django.db import models

# Create your models here.
from register.models import Register


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    sportsitem_name = models.CharField(max_length=35)
    amount = models.IntegerField()
   #  user_id = models.IntegerField()
    user = models.ForeignKey(Register, to_field='user_id', on_delete=models.CASCADE)
    image = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'order'
