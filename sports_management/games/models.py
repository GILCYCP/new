from django.db import models

# Create your models here.
class Games(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=35)
    game_points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'games'
