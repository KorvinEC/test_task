from rest_framework import generics
from .serializers import DealerSerializer, CarSerializer
from .models import Dealer, Car

from django_filters.rest_framework import DjangoFilterBackend


class DealerList(generics.ListCreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class DealerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dealer']


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

