from django.db import models


class Election(models.Model):
    candidate_name = models.CharField(max_length=10)
    constituency = models.CharField(max_length=20)
    total_voters = models.IntegerField()
    secured_votes = models.IntegerField()
    choice = [('elected', 'ELECTED'), ('defeated', 'DEFEATED')]
    status = models.CharField(max_length=10, choices=choice)




