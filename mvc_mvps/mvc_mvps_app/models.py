from django.db import models

# Create your models here.
class Conference(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name
    
class Player(models.Model):
    class Position(models.TextChoices):
        POINTGUARD = 'PG', _("Pointguard")
        SHOOTING_GUARD = 'SG', _('Guard')
        FORWARD = 'F', _('Forward')
        CENTER = 'C', _('Center')

    name = models.CharField(max_length=100)
    age = models.IntegerField(default=19)
    position = models.CharField(choices=Position, default=Position.SHOOTING_GUARD) 
    injured = models.models.BooleanField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players') 