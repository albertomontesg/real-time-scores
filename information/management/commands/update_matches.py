import requests

from django.core.management.base import BaseCommand

from information.models import Team, Match
from information.util.parser import find_match_url

class Command(BaseCommand):
    help = 'Check all the matches for each team'

    def handle(self, *args, **options):
        teams = Team.objects.all()
        for team in teams:
            if not team.has_url():
                continue
            for i in range(team.num_matches):
                j = i + 1
                r = requests.get(team.get_url(j))
                content = r.content
