from rest_framework import serializers
from missions.models import Target, Mission


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['name', 'country', 'notes']


class TargetUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['notes', 'is_complete']


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['cat', 'targets']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission


class MissionUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mission
        fields = ['is_complete']
