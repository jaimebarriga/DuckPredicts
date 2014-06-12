from django.db import models
from consts import WC_COUNTRIES

# Create your models here.

class Team(models.Model):
	country = models.CharField(max_length=128, choices=WC_COUNTRIES)

class Match(models.Model):
	team1 = models.ForeignKey(Team)
	team2 = models.ForeignKey(Team)

class Results(models.Model):
	match = models.ForeignKey(Match)
	winner = models.ForeignKey(Team)
