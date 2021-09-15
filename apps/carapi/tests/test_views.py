import json

from rest_framework import status
from django.test import TestCase, Client
from rest_framework.test import APITransactionTestCase

from ..models import Car, SubModel
from ..serializers import SubModelSerializer, CarSerializer

# initialize the APIClient app
client = Client()


class GetAllMMSTest(TestCase):
    """ Test module for MMS API """

    def test_get_all_mms(self):
        # get API response
        response = client.get('/all/')
        # get data from db
        submodels = SubModel.objects.all()
        serializer = SubModelSerializer(submodels, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllCarTest(TestCase):
    """ Test module for MMS API """

    def test_get_all_mms(self):
        # get API response
        response = client.get('/car/')
        # get data from db
        car = Car.objects.all()
        serializer = CarSerializer(car, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AddCarTest(TestCase):
    """ Test module for add car API """

    def setUp(self):
        self.valid_payload = {
            "id": "54e7616d98e8d95e2dfdcbae19f09d41e",
            "active": "t",
            "year": "2009",
            "mileage": "178000",
            "price": "28000",
            "body_type": "Coupe",
            "transmission": "Automatic",
            "fuel_type": "Petrol",
            "exterior_color": "Grey",

        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_create_valid_car(self):
        response = client.post('/addcar/',
                               data=json.dumps(self.valid_payload),
                               content_type='application/json'
                               )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_car(self):
        response = client.post('addcar/',
                               data=json.dumps(self.invalid_payload),
                               content_type='application/json'
                               )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CarSearchTest(APITransactionTestCase):
    def test_null(self):
        parms = {"price": "100", "mileage": "10001"}
        response = self.client.post("searchcar/", parms=parms)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def wrong_parms(self):
        parms = {"pe": "100", "m": "10001"}
        response = self.client.post("searchcar/", parms=parms)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def get_car_test(self):
        parms = {"price": "200", "mileage": "10100"}
        response = self.client.post("searchcar/", parms=parms)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
