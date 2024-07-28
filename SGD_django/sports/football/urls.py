# sports/football/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlayerInfoViewSet, RecordViewSet, TeamStatsViewSet, TeamViewSet, PlayerViewSet, TournamentInfoViewSet, MatchTeamStatsViewSet, MatchStatsViewSet, MatchViewSet

router = DefaultRouter()
router.register(r'player_info', PlayerInfoViewSet)
router.register(r'records', RecordViewSet)
router.register(r'team_stats', TeamStatsViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'tournaments', TournamentInfoViewSet)
router.register(r'match_team_stats', MatchTeamStatsViewSet)
router.register(r'match_stats', MatchStatsViewSet)
router.register(r'matches', MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
