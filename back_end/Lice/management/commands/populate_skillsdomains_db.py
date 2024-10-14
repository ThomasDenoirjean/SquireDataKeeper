from django.core.management.base import BaseCommand
from Lice.models import Technique, SkillDomain


class Command(BaseCommand):
    args = '<foo bar ...>' ### copié collé
    help = 'our help string comes here' ### ### copié collé

    def _populate_db(self):
        Technique.objects.all().delete()
        SkillDomain.objects.all().delete()

        data_to_create = {
            'Wrestling': {'techniques': ['Capuche', 'Camion', 'Sangsue'], 'color': '#EEE3AF'},
            'Striking': {'techniques': ['Genoux', 'Frappe 1 main', 'Frappe 2 mains'], 'color': '#253342'},
            'Projection': {'techniques': ['Osoto Gari', 'Balayette', 'Mawashigari'], 'color': '#4FB06D'},
            'Running': {'techniques': ['Angle Mort', 'Prise de terrain', 'Communication'], 'color': '#D49137'},
        }

        for key in data_to_create.keys():
            skilldomain = SkillDomain()
            skilldomain.name = key
            skilldomain.color = data_to_create.get(key).get('color')
            skilldomain.save()
            for technique_name in data_to_create.get(key).get('techniques'):
                technique = Technique()
                technique.name = technique_name
                technique.domain = skilldomain
                technique.save()

    def handle(self, *args, **options): ### copié collé
        self._populate_db() ### copié collé




