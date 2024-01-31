from django.db import models

# Create your models here.
from register.models import Register


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=35)
    amount = models.IntegerField()
    image = models.CharField(max_length=45)
    # user_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(Register, to_field='user_id', on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'item'
