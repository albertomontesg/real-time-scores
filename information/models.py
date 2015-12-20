from django.db.models import Model, CharField
from django.conf import settings

class Team(Model):
    GENDERS = (
        ('M', u'Masculí'),
        ('F', u'Femení')
    )

    name = CharField(max_length=100, blank=False)
    gender = CharField(max_length=10, choices=GENDERS, default='M')
    url_id = CharField(max_length=100, blank=True)

    def get_url(self, day):
        ' The day is "jornada"'
        assert isinstance(day, int) or isinstance(day, str), 'Day must be and integer or a string'
        return settings.FCB_COMPETITIONS_URL + self.url_id + '/' + str(day)

    def full_name(self):
        return self.name + ' ' + self.gender

    def has_url(self):
        return self.url_id != ''
