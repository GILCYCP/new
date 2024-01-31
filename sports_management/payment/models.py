from django.db import models
from register.models import Register
# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    account_number = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=20)
    amount = models.IntegerField()
    # user_id = models.IntegerField()
    user=models.ForeignKey(Register,to_field='user_id',on_delete=models.CASCADE)
    status = models.CharField(max_length=45)
    ifsc_code = models.CharField(max_length=45)
    type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'
