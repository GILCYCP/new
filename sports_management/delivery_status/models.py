from django.db import models
from register.models import Register

# Create your models here.
class DeliveryStatus(models.Model):
    deliverystatus_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    delivery_date = models.DateField()
    status = models.CharField(max_length=50)
    time = models.TimeField()
    order_id = models.IntegerField(blank=True, null=True)
    # user_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(Register, to_field='user_id', on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'delivery_status'
