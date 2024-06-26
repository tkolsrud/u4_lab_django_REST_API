from rest_framework import serializers
from .models import Conference, Team, Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='team-detail',
        read_only=True
    )

    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source='team'
    )

    player_url = serializers.ModelSerializer.serializer_url_field(
        view_name='player-detail'
    )

    class Meta:
        model = Player
        fields = '__all__' 

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    conference = serializers.HyperlinkedRelatedField(
        view_name='conference-detail',
        read_only='true'
    )

    conference_id = serializers.PrimaryKeyRelatedField(
        queryset=Conference.objects.all(),
        source='conference'
    )

    players = serializers.HyperlinkedRelatedField(
        view_name='player-detail',
        many=True,
        read_only=True
    )
    team_url = serializers.ModelSerializer.serializer_url_field(
        view_name='team-detail'
    )

    class Meta:
        model = Team
        fields = '__all__'

class ConferenceSerializer(serializers.HyperlinkedModelSerializer):
    teams = serializers.HyperlinkedRelatedField(
        view_name='team-detail',
        many=True,
        read_only=True
    )

    conference_url = serializers.ModelSerializer.serializer_url_field(
        view_name='conference-detail'
    )

    class Meta:
        model = Conference
        fields = '__all__'