from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema

from cats.models import SpyCat
from cats.serializers import SpyCatSerializer, SpyCatUpdateSerializer


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

    @swagger_auto_schema(operation_summary="Create a new SpyCat")
    def create(self, request, *args, **kwargs):
        serializer = SpyCatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        spycat_instance = self.get_object()
        serializer = SpyCatUpdateSerializer(spycat_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Delete SpyCat")
    def destroy(self, request, *args, **kwargs):
        spycat = self.get_object()
        try:
            spycat.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
