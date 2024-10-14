
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import LicePosition, Technique, SkillDomain, Fighter, TechniqueLevel, EnemyTeam, Tournament, Match, Round, RoundPerformance

from django.conf import settings
from urllib.parse import urljoin

class LicePositionSerializer(ModelSerializer):

    class Meta:
        model = LicePosition
        fields =  ['id', 'position']


class TechniqueSerializer(ModelSerializer):
 
    class Meta:
        model = Technique
        fields = ['id', 'name', 'domain']


class SkillDomainSerializer(ModelSerializer):

    class Meta:
        model = SkillDomain
        fields = ['id', 'color', 'name', 'techniques']


class TechniqueLevelSerializer(ModelSerializer):
    technique = TechniqueSerializer()

    class Meta:
        model = TechniqueLevel
        fields = ['id', 'technique', 'level']


class FighterSerializer(ModelSerializer):
    techniques_levels = TechniqueLevelSerializer(many=True, required=False)
    role = serializers.PrimaryKeyRelatedField(queryset=LicePosition.objects.all(), many=True, required=False)
    picture = serializers.ImageField(required=False)

    class Meta:
        model = Fighter
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'nickname', 
            'picture', 
            'member_since', 
            'first_tournament', 
            'tournament_participation',
            'role',
            'techniques_levels'
            ]


class EnemyTeamSerializer(ModelSerializer):
    class Meta:
        model = EnemyTeam
        fields = ['id', 'name']


class TournamentSerializer(ModelSerializer):
    class Meta:
        model = Tournament
        fields = ['id', 'name', 'date', 'localization', 'ranking', 'number_of_match', 'matchs']
    

class MatchSerializer(ModelSerializer):
    enemyteam = EnemyTeamSerializer()

    class Meta:
        model = Match
        fields = ['id', 'tournament', 'enemyteam', 'match_rank', 'number_of_round', 'victory', 'rounds']


class RoundSerializer(ModelSerializer):
    match = MatchSerializer()
    fighters_involved = FighterSerializer(many=True)

    class Meta:
        model = Round
        fields = ['id', 'match', 'fighters_involved', 'round_rank', 'issue']

       
class RoundPerformanceSerializer(ModelSerializer):
    class Meta:
        model = RoundPerformance
        fields = [
            'id', 
            'fighterID', 
            'lice_position_position', 
            'roundID', 
            'first_on_the_ground', 
            'resistance_level', 
            'takedown_solo', 
            'takedown_team', 
            'double_chute'
        ]
        
    def to_internal_value(self, data):
        resistance_mapping = {v: k for k, v in RoundPerformance.RESISTANCE_CHOICES}

        resistance_level = data.get('resistance_level')
        if resistance_level in resistance_mapping:
            data['resistance_level'] = resistance_mapping[resistance_level]
        else:
            raise serializers.ValidationError({
                'resistance_level': f'Invalid choice for resistance level: {resistance_level}'
            })

        return super().to_internal_value(data)