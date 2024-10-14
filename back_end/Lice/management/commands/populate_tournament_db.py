from django.core.management.base import BaseCommand
from Lice.models import EnemyTeam, Tournament, Match, Round, RoundPerformance, Fighter


class Command(BaseCommand):
    args = '<foo bar ...>' ### copié collé
    help = 'our help string comes here' ### ### copié collé

    def _populate_db(self):
        EnemyTeam.objects.all().delete()

        team_to_create = [
            "Les bannerets d'Auvergne",
            "La garde du Roussillon",
            "Diex Aïe",
            "Les ardents",
            "Pardus Bellator",
            "White company"
                          ]

        for team_name in team_to_create:
            enemyteam = EnemyTeam()
            enemyteam.name = team_name
            enemyteam.save()


        Tournament.objects.all().delete()
        
        enemyteams = EnemyTeam.objects.all()
        fighters = Fighter.objects.all()

        tournaments_to_create = [
            {
                'name': 'Parthenay',
                'date': '2022-05-17',
                'localization': 'Parthenay',
                'ranking': 5,
                'number_of_match': 4,
                'matchs': [
                    {'enemyteam': enemyteams.get(name = 'White company'), 'match_rank': 1, 'number_of_round': 2, 'victory': True, 'rounds': [
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Takeshi', 'Sylvie', 'Tod', 'Quellcrist', 'Rad']),
                            'round_rank': 1,
                            'issue': 'V'},
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Takeshi', 'Nakita', 'Tod']),
                            'round_rank': 2,
                            'issue': 'DR'}
                    ]},
                    {'enemyteam': enemyteams.get(name = 'Diex Aïe'), 'match_rank': 2, 'number_of_round': 2, 'victory': True, 'rounds': [
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Tod', 'Quellcrist', 'Rad']),
                            'round_rank': 1,
                            'issue': 'V'},
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Quellcrist', 'Nakita', 'Tod', 'Takeshi', 'Sylvie']),
                            'round_rank': 2,
                            'issue': 'V'}
                    ]},
                    {'enemyteam': enemyteams.get(name = 'Pardus Bellator'), 'match_rank': 3, 'number_of_round': 3, 'victory': False, 'rounds': [
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Tod', 'Quellcrist', 'Rad']),
                            'round_rank': 1,
                            'issue': 'DR'},
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Quellcrist', 'Nakita', 'Tod', 'Takeshi', 'Sylvie']),
                            'round_rank': 2,
                            'issue': 'DE'},
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Tod', 'Quellcrist', 'Rad']),
                            'round_rank': 3,
                            'issue': 'DE'}
                    ]},
                    {'enemyteam': enemyteams.get(name = 'Les ardents'), 'match_rank': 4, 'number_of_round': 2, 'victory': False, 'rounds': [
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Quellcrist', 'Nakita', 'Tod', 'Takeshi', 'Sylvie']),
                            'round_rank': 1,
                            'issue': 'DR'},
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Tod', 'Quellcrist', 'Rad']),
                            'round_rank': 2,
                            'issue': 'DR'}
                    ]}
                ]
            },
            {
                'name': 'La Cassine',
                'date': '2022-07-05',
                'localization': 'La Cassine',
                'ranking': 3,
                'number_of_match': 2,
                'matchs': [
                    {'enemyteam': enemyteams.get(name = 'La garde du Roussillon'), 'match_rank': 1, 'number_of_round': 4, 'victory': False, 'rounds': [
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Quellcrist', 'Nakita', 'Tod', 'Takeshi', 'Sylvie']),
                            'round_rank': 1,
                            'issue': 'V'},
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Rad', 'Nakita', 'Tod', 'Takeshi', 'Sylvie']),
                            'round_rank': 2,
                            'issue': 'DR'},
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Quellcrist', 'Rad', 'Tod', 'Takeshi', 'Sylvie']),
                            'round_rank': 3,
                            'issue': 'DE'},
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Quellcrist', 'Nakita', 'Tod', 'Rad', 'Takeshi']),
                            'round_rank': 4,
                            'issue': 'DE'}
                    ]},
                    {'enemyteam': enemyteams.get(name = "Les bannerets d'Auvergne"), 'match_rank': 2, 'number_of_round': 3, 'victory': True, 'rounds': [
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Tod', 'Quellcrist', 'Rad']),
                            'round_rank': 1,
                            'issue': 'V'},
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Tod', 'Quellcrist', 'Rad']),
                            'round_rank': 2,
                            'issue': 'DE'},
                        {
                            'fighters_involved': fighters.filter(first_name__in = ['Tod', 'Quellcrist', 'Rad']),
                            'round_rank': 3,
                            'issue': 'V'}
                    ]},
                ]
            },
        ]

        for new_tournament in tournaments_to_create:
            tournament = Tournament()
            tournament.name = new_tournament['name']
            tournament.date = new_tournament['date']
            tournament.localization = new_tournament['localization']
            tournament.ranking = new_tournament['ranking']
            tournament.number_of_match = new_tournament['number_of_match']
            tournament.save()
            print('tournament', tournament)
            for new_match in new_tournament['matchs']:
                match = Match()
                match.tournament = tournament
                match.enemyteam = new_match['enemyteam']
                match.match_rank = new_match['match_rank']
                match.number_of_round = new_match['number_of_round']
                match.victory = new_match['victory']
                match.save()
                print('match', match)
                for new_round in new_match['rounds']:
                    round = Round()
                    round.match = match
                    round.round_rank = new_round['round_rank']
                    round.issue = new_round['issue']
                    round.save()
                    round.fighters_involved.set(new_round['fighters_involved'])
                    round.save()
                    print('round', round)
            

    def handle(self, *args, **options): ### copié collé
        self._populate_db() ### copié collé




