from django.db import models

# Create your models here.
class Advertisement(models.Model):
    ads_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=500)
    product_image = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'advertisement'
