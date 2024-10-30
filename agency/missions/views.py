from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema

from missions.serializers import (
    MissionSerializer,
    MissionUpdateSerializer,
    TargetUpdateSerializer,
)
from missions.models import Mission, Target


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    @swagger_auto_schema(operation_summary="Create a new mission and targets")
    def create(self, request, *args, **kwargs):
        serializer = MissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Update mission status")
    def update(self, request, *args, **kwargs):
        mission_instance = self.get_object()
        serializer = MissionUpdateSerializer(mission_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Delete mission")
    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        try:
            mission.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetUpdateSerializer

    @swagger_auto_schema(operation_summary="Update target notes or status")
    def update(self, request, *args, **kwargs):
        target = self.get_object()
        if target.is_complete or target.mission.is_complete:
            return Response({"error": "Cannot update Notes as the target or mission is completed."},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)
