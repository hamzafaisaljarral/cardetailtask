from django.db.models import Q
from rest_framework import viewsets, generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SubModelSerializer, CarSerializer
from .models import Car, SubModel


class MMSViewSet(viewsets.ModelViewSet):
    queryset = SubModel.objects.all().order_by('name')
    serializer_class = SubModelSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ADDCarView(APIView):

    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer = CarSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():
            # If user data is valid, create a new car item record in the database
            car_item_object = create_serializer.save()

            # Serialize the new car item from a Python object to JSON format
            read_serializer = CarSerializer(car_item_object)

            # Return a HTTP response with the newly created car item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)


class CarSearchView(generics.ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def get_queryset(self):
        """
        return car on base of user filter for mileage and price.
        """
        if self.request.GET.get('price') and self.request.GET.get('mileage'):
            return super().get_queryset().filter(
                Q(price=self.request.GET.get('price')) & Q(mileage=self.request.GET.get('mileage'))
            ).order_by('updated_at')
        else:
            raise ValidationError(detail='Invalid Params')
