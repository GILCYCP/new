from django.db import models

# Create your models here.
class Facilities(models.Model):
    facilities_id = models.IntegerField(primary_key=True)
    equipments = models.CharField(max_length=30)
    special_features = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'facilities'
