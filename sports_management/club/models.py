from django.db import models

# Create your models here.
class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=80)
    password = models.CharField(max_length=45)
    status = models.CharField(max_length=45, blank=True, null=True)
    fees = models.CharField(max_length=45)
    img = models.CharField(max_length=45, blank=True, null=True)
    more_information = models.CharField(db_column='more information', max_length=45, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    facilities = models.CharField(max_length=45, blank=True, null=True)


    class Meta:
         managed = False
         db_table = 'club'
