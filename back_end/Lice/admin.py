from django.contrib import admin
from .models import SkillDomain, Technique, Fighter, TechniqueLevel, EnemyTeam, Tournament, Match, Round, RoundPerformance 

# Register your models here.
admin.site.register([SkillDomain, Technique, Fighter, EnemyTeam, Tournament, Match, Round, RoundPerformance])

class TechniqueLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'fighter', 'technique', 'level')

admin.site.register(TechniqueLevel, TechniqueLevelAdmin)