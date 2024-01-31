from django.db import models
from register.models import Register
from club.models import Club
# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user = models.ForeignKey(Register, to_field='user_id', on_delete=models.CASCADE)
    booking_status = models.CharField(max_length=45)
    date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    # club_id = models.IntegerField(blank=True, null=True)
    club = models.ForeignKey(Club, to_field='club_id', on_delete=models.CASCADE)
    from_time = models.CharField(max_length=45, blank=True, null=True)
    to_time = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking'

