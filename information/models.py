from django.db import models
from django.conf import settings

class Team(models.Model):
    GENDERS = (
        ('M', u'Masculí'),
        ('F', u'Femení')
    )

    name = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=10, choices=GENDERS, default='M')
    url_id = models.CharField(max_length=100, blank=True)
    num_matches = models.IntegerField(default=0)

    def get_url(self, day):
        ' The day is "jornada"'
        assert isinstance(day, int) or isinstance(day, str), 'Day must be and integer or a string'
        return settings.FCB_COMPETITIONS_URL + self.url_id + '/' + str(day)

    def full_name(self):
        return self.name + ' ' + self.gender

    def has_url(self):
        return self.url_id != ''

class Match(models.Model):
    team = models.ForeignKey('Team')
    game_num = models.IntegerField(default=0)
    opponent = models.CharField(max_length=50, blank=False)
    datetime = models.DateTimeField()
    local = models.BooleanField(default=True)
    local_score = models.IntegerField()
    visitant_score = models.IntegerField()
    url_id = models.CharField(max_length=50, blank=False)

    def get_url(self):
        return settings.FCB_MATCHES_URL + self.url_id

    def get_score(self):
        return str(local_score) + '-' + str(visitant_score)
