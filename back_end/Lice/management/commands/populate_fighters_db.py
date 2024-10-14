from django.core.management.base import BaseCommand
from Lice.models import LicePosition, Fighter


class Command(BaseCommand):
    args = '<foo bar ...>' ### copié collé
    help = 'our help string comes here' ### ### copié collé

    def _populate_db(self):
        LicePosition.objects.all().delete()

        for position in range(5):
            liceposition = LicePosition()
            liceposition.position = position + 1
            liceposition.save()

        Fighter.objects.all().delete()

        roles = LicePosition.objects.all()

        # trouver un moyen de filtrer les querrysets pour enregistrer leur id dans le many to many field
        # sinon ça ne fonctionnait que pour les personnes qui avaient tous les roles
        fighters_to_create = {
            'Takeshi Kovacs': {
                'firstname': 'Takeshi',
                'nickname': 'La chance',
                'lastname': 'Kovacs',
                'member_since': '2015-02-03',
                'first_tournament': '2015-02-10',
                'tournament_participation': 10,
                'role': roles
            },
            'Nadiah Makita': {
                'firstname': 'Nadiah',
                'lastname': 'Makita',
                'member_since': '2020-10-19',
                'role': roles.filter(position__in = [1, 5])
            },
            'Sylvie Oshima': {
                'firstname': 'Sylvie',
                'nickname': 'Cyber',
                'lastname': 'Oshima',
                'member_since': '2015-02-03',
                'role': roles.filter(position = 3)
            },
            'Tod Murakami': {
                'firstname': 'Tod',
                'lastname': 'Murakami',
                'member_since': '2017-08-10',
                'first_tournament': '2018-02-10',
                'tournament_participation': 1,
                'role': roles.filter(position__in = [2, 4])
            },
            'Quellcrist Falconer': {
                'firstname': 'Quellcrist',
                'nickname': 'Decolo',
                'lastname': 'Falconer',
                'member_since': '2019-02-03',
                'first_tournament': '2019-02-10',
                'tournament_participation': 5,
                'role': roles
            },
            'Rad Sevesgul': {
                'firstname': 'Rad',
                'nickname': 'BadBoy',
                'lastname': 'Sevesgul',
                'member_since': '2022-02-03',
                'role': roles.filter(position = 3)
            }, 
        }

        for new_fighter in fighters_to_create.keys():
            print('new_fighter', new_fighter)
            fighter = Fighter()
            fighter.first_name = fighters_to_create[new_fighter]['firstname']
            fighter.last_name = fighters_to_create[new_fighter]['lastname']
            print("'nickname' in fighters_to_create[new_fighter].keys()", 'nickname' in fighters_to_create[new_fighter].keys())
            if 'nickname' in fighters_to_create[new_fighter].keys():
                fighter.nickname = fighters_to_create[new_fighter]['nickname']
            fighter.member_since = fighters_to_create[new_fighter]['member_since']
            print("'first_tournament' in fighters_to_create[new_fighter].keys()", 'first_tournament' in fighters_to_create[new_fighter].keys())
            if 'first_tournament' in fighters_to_create[new_fighter].keys():
                fighter.first_tournament = fighters_to_create[new_fighter]['first_tournament']
                fighter.tournament_participation = fighters_to_create[new_fighter]['tournament_participation']
            print('s apprete à sauver')
            fighter.save()
            fighter.role.set(fighters_to_create[new_fighter]['role']) 
            fighter.save()

    def handle(self, *args, **options): ### copié collé
        self._populate_db() ### copié collé
