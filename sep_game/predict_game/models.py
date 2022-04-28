from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(help_text="The field stores the score of each member.", default=0)
    victory = models.IntegerField(help_text="The field stores the number of times the score was hit.", default=0)

    def get_absolute_url(self):
        return reverse('member-detail-view', args=[str(self.id)])

    
    def __str__(self):
        return self.name
    

class Match(models.Model):
    home_team_name = models.CharField(max_length=100)
    away_team_name = models.CharField(max_length=100)
    home_team_goals = models.IntegerField()
    away_team_goals = models.IntegerField()
    date = models.DateField(null=True)
    arena = models.CharField(max_length=100, null=True)

    def get_absolute_url(self):
        return reverse('match-detail-view', args=[str(self.id)])

    
    def __str__(self):
        return f'{self.home_team_name} X {self.away_team_name}'


class Hunch(models.Model):
    member_id = models.ForeignKey('Member', null=True, on_delete=models.SET_NULL)
    match_id = models.ForeignKey('Match', null=True, on_delete=models.SET_NULL)
    home_team_hunch = models.IntegerField(null=True)
    away_team_hunch = models.IntegerField(null=True)
    point = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('hunch-detail-view', args=[str(self.id)])
    

    def __str__(self):
        return f'{self.home_team_hunch} X {self.away_team_hunch}'