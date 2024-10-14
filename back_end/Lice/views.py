from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Fighter, LicePosition, SkillDomain, Technique, TechniqueLevel, Tournament, Match, Round, EnemyTeam, RoundPerformance
from .serializers import RoundPerformanceSerializer, FighterSerializer, LicePositionSerializer, SkillDomainSerializer, TechniqueSerializer, TechniqueLevelSerializer, TournamentSerializer, MatchSerializer, RoundSerializer, EnemyTeamSerializer


class LicePositionAPI(APIView):
    def get(self, request):
        licepositions = LicePosition.objects.all()
        serialized = LicePositionSerializer(licepositions, many=True)
        return Response(serialized.data)
    

class SkilldomainAPI(APIView):
    def get(self, request, pk=None):
        if pk:
            domain = SkillDomain.objects.get(pk=pk)
            serialized = SkillDomainSerializer(domain)
        else:    
            domains = SkillDomain.objects.all()
            serialized = SkillDomainSerializer(domains, many=True)
        return Response(serialized.data)
    
    def post(self, request):
        serializer = SkillDomainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        domain = SkillDomain.objects.get(pk=pk)
        if not domain:
            return Response(
                {"res": "Object with skill domain id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'color': request.data.get('color')
        }
        serializer = SkillDomainSerializer(instance = domain, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        try:
            domain = SkillDomain.objects.get(pk=pk)
            domain.delete()
            return Response({"message": "Domaine supprimé avec succès."}, status=status.HTTP_204_NO_CONTENT)
        except SkillDomain.DoesNotExist:
            return Response({"message": "Le domaine spécifié n'existe pas."}, status=status.HTTP_404_NOT_FOUND)


class TechniqueAPI(APIView):
    def get(self, request):
        technique_id = request.GET.get('id')

        try:
            technique = Technique.objects.get(pk=technique_id)
            serialized_data = TechniqueSerializer(technique).data
            return Response({'name': serialized_data['name']})
        except Technique.DoesNotExist:
            return Response({'error': 'La technique spécifiée n\'existe pas'}, status=404)

    def post(self, request):
        print('request.data', request.data)
        serializer = TechniqueSerializer(data=request.data)
        print('serializer', serializer)
        print('serializer.is_valid()', serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            technique = Technique.objects.get(pk=pk)
            technique.delete()
            return Response({"message": "Technique supprimée avec succès."}, status=status.HTTP_204_NO_CONTENT)
        except Technique.DoesNotExist:
            return Response({"message": "La technique spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND) 
    

class FighterAPI(APIView):
    def get(self, request, pk=None):
        if pk:
            fighter = Fighter.objects.get(pk=pk)
            serialized = FighterSerializer(fighter)
        else:    
            fighters = Fighter.objects.all()
            serialized = FighterSerializer(fighters, many=True)
        return Response(serialized.data)
    
    def post(self, request):
        serializer = FighterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('serializer.errors', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        try:
            fighter = Fighter.objects.get(pk=pk)
            fighter.delete()
            return Response({"message": "Combattant supprimé avec succès."}, status=status.HTTP_204_NO_CONTENT)
        except Technique.DoesNotExist:
            return Response({"message": "Le combattant spécifié n'existe pas."}, status=status.HTTP_404_NOT_FOUND) 
    

class TechniqueLevelAPI(APIView):
    def post(self, request):
        technique_level_id = request.data.get('id')
        new_level = request.data.get('new_level')
        technique_level = TechniqueLevel.objects.get(pk=technique_level_id)
        try:
            technique_level.level = new_level
            technique_level.save()
            serializer = TechniqueLevelSerializer(technique_level)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SkillDomain.DoesNotExist:
            return Response({"message": "La technique spécifiée n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
    

@receiver(post_save, sender=Technique)
@receiver(post_save, sender=Fighter)
def create_initial_technique_levels(sender, instance, created, **kwargs):
    """
    Fonction de réception pour créer des TechniqueLevel lors de la création d'une nouvelle technique
    ou d'un nouveau combattant, avec un niveau initial de 0 pour chaque combinaison.
    """
    if created:
        if isinstance(instance, Technique):
            fighters = Fighter.objects.all()
            for fighter in fighters:
                TechniqueLevel.objects.create(
                    fighter=fighter,
                    technique=instance,
                    level=0
                )
        elif isinstance(instance, Fighter):
            techniques = Technique.objects.all()
            for technique in techniques:
                TechniqueLevel.objects.create(
                    fighter=instance,
                    technique=technique,
                    level=0
                )

################################
####### Section tournois #######
################################

class TournamentAPI(APIView):
    def get(self, request, pk=None):
        if pk:
            tournament = Tournament.objects.get(pk=pk)
            serialized = TournamentSerializer(tournament)
        else:    
            tournaments = Tournament.objects.all()
            serialized = TournamentSerializer(tournaments, many=True)
        return Response(serialized.data)
    
    def post(self, request):
        print('request.data', request.data)

        new_tournament_id = 0

        try:
            tournament = Tournament()
            tournament.name = request.data['name']
            tournament.date = request.data['date']
            tournament.localization = request.data['localization']
            tournament.ranking = request.data['ranking']
            tournament.number_of_match = request.data['number_of_match']
            tournament.save()
            new_tournament_id = tournament.id
            print('tournament', tournament)
            print('new_tournament_id', new_tournament_id)
            for new_match in request.data['matchs']:
                match = Match()
                match.tournament = tournament
                match.enemyteam = EnemyTeam.objects.get(name = new_match['enemyteam'])
                match.match_rank = new_match['match_rank']
                match.number_of_round = new_match['number_of_rounds']
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
            return Response(new_tournament_id, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        try:
            tournament = Tournament.objects.get(pk=pk)
            tournament.delete()
            return Response({"message": "Tournoi supprimé avec succès."}, status=status.HTTP_204_NO_CONTENT)
        except SkillDomain.DoesNotExist:
            return Response({"message": "Le tournoi spécifié n'existe pas."}, status=status.HTTP_404_NOT_FOUND)


class MatchAPI(APIView):
    def get(self, request):
        match_id = request.GET.get('id')

        try:
            match = Match.objects.get(pk=match_id)
            serialized = MatchSerializer(match)
            return Response(serialized.data)
        except Match.DoesNotExist:
            return Response({'error': 'Le match spécifié n\'existe pas'}, status=404)


class RoundAPI(APIView):
    def get(self, request):
        round_id = request.GET.get('id')

        try:
            round = Round.objects.get(pk=round_id)
            serialized = RoundSerializer(round)
            return Response(serialized.data)
        except Round.DoesNotExist:
            return Response({'error': 'Le round spécifié n\'existe pas'}, status=404)


class EnnemyTeamAPI(APIView):
    def get(self, request):
        ennemy_teams = EnemyTeam.objects.all()
        serialized = EnemyTeamSerializer(ennemy_teams, many=True)
        return Response(serialized.data)


class RoundPerformanceAPI(APIView):
    def get(self, request):
        round_ID = request.GET.get('id')

        print('round_ID', round_ID)

        round_performance = RoundPerformance.objects.filter(roundID=round_ID)
        print('round_performance', round_performance)
        serialized = RoundPerformanceSerializer(round_performance, many = True)
        print('round performance founded !!', serialized.data)
        return Response(serialized.data)

    def post(self, request):
        print('request.data', request.data)

        serializer = RoundPerformanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('serializer.errors', serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            round_performance = RoundPerformance.objects.get(pk=pk)
            round_performance.delete()
            return Response({"message": "Round performance supprimé avec succès."}, status=status.HTTP_204_NO_CONTENT)
        except SkillDomain.DoesNotExist:
            return Response({"message": "Round performance spécifié n'existe pas."}, status=status.HTTP_404_NOT_FOUND)
