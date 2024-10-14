from django.db import models


class LicePosition(models.Model):
    position = models.fields.IntegerField()

    def __str__(self):
        return str(self.position)


class SkillDomain(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default='#925040')

    def __str__(self):
        return self.name


class Technique(models.Model):
    name = models.CharField(max_length=100)
    domain = models.ForeignKey(SkillDomain, on_delete=models.CASCADE, related_name='techniques')

    def __str__(self):
        return self.name


class Fighter(models.Model):
    first_name = models.fields.CharField(max_length=100)
    last_name = models.fields.CharField(max_length=100)
    nickname = models.fields.CharField(max_length=100, blank=True)
    picture = models.ImageField(upload_to='fighterspictures/', blank=True, max_length=100)
    member_since = models.fields.DateField()
    first_tournament = models.fields.DateField(blank=True, null=True)
    tournament_participation = models.fields.IntegerField(default=0)
    role = models.ManyToManyField(LicePosition, blank=True)

    def __str__(self):
        if self.nickname:
            return f'{self.first_name} "{self.nickname}" {self.last_name}'
        else:
            return f'{self.first_name} {self.last_name}'


class TechniqueLevel(models.Model):
    fighter = models.ForeignKey(Fighter, on_delete=models.CASCADE, related_name='techniques_levels')
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.fighter} "{self.technique}" {self.level}'


class EnemyTeam(models.Model):
    name = models.fields.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Tournament(models.Model):
    name = models.fields.CharField(max_length=100)
    date = models.fields.DateField()
    localization = models.fields.CharField(max_length=100, blank=True, null=True)
    ranking = models.fields.IntegerField()
    number_of_match = models.fields.IntegerField()

    def __str__(self):
        return f"Tournoi de {self.name} - { self.date }"
    

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matchs')
    enemyteam = models.ForeignKey(EnemyTeam, on_delete=models.CASCADE)
    match_rank = models.fields.IntegerField()
    number_of_round = models.fields.IntegerField()
    victory = models.fields.BooleanField()

    def __str__(self):
        return f"Match de {self.number_of_round} rounds contre {self.enemyteam} au {self.tournament}"


class Round(models.Model):
    ROUND_ISSUE_CHOICES = [('V', 'victory'), ('DE', 'defeat'), ('DR', 'draw')]

    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='rounds')
    fighters_involved = models.ManyToManyField(Fighter)
    round_rank = models.fields.IntegerField()
    issue = models.fields.CharField(max_length=8, choices = ROUND_ISSUE_CHOICES)

    def __str__(self):
        return f"Round {self.round_rank} du {self.match}"


class RoundPerformance(models.Model):
    RESISTANCE_CHOICES = [('B', 'bad'), ('M', 'medium'), ('G', 'good'), ('LS', 'last standing')]

    fighterID = models.fields.IntegerField()
    lice_position_position = models.fields.IntegerField()
    roundID = models.fields.IntegerField()
    first_on_the_ground = models.fields.BooleanField(default=False)
    resistance_level = models.fields.CharField(max_length = 15, choices = RESISTANCE_CHOICES)
    takedown_solo = models.fields.IntegerField(default=0)
    takedown_team = models.fields.IntegerField(default=0)
    double_chute = models.fields.BooleanField(default=False)
