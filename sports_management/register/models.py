from django.db import models

# Create your models here.
class Register(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=35)
    email = models.CharField(max_length=30)
    contact_number = models.IntegerField()
    password = models.CharField(max_length=15)


    class Meta:
        managed = False
        db_table = 'register'
