from django.db import models

# Create your models here.
class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    mob_no = models.CharField(max_length=10)
    password = models.CharField(max_length=45)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop'
