from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from api.serializers import BonusSerializer
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)
from core.models import *

from datetime import datetime

import os

@swagger_auto_schema(method='post',request_body=BonusSerializer)
@api_view(["POST"])
def bonus(request):
    serializer = BonusSerializer(data = request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)
    
    bonus_key = os.getenv("bonus_key")

    if bonus_key != serializer.data["bonus_key"]:
        return Response(status = HTTP_400_BAD_REQUEST)
    
    try:
        diler = Diler.objects.get(seller_code=serializer.data["s_code"])
    except Diler.DoesNotExist:
        return Response(status=HTTP_400_BAD_REQUEST)
    
    

    date_create = datetime.strptime(serializer.data["date_create"], '%Y-%m-%d').date()


    shapes = Bonus.objects.filter(select='s')
    for shape in serializer.data['shape']:
        try:
            s = shapes.get(shape__name=shape["name"])
        except Bonus.DoesNotExist:
            continue

        if s.fr <= date_create and s.to >= date_create:
            diler.bonus = diler.bonus + (s.count * int(shape["m2"]))



    glazings = Bonus.objects.filter(select='g')
    for glazing in serializer.data['glazing']:
        try:
            s = glazings.get(glazing__articul=glazing["name"])
        except Bonus.DoesNotExist:
            continue


        if s.fr <= date_create and s.to >= date_create:
            diler.bonus = diler.bonus + (s.count * int(glazing["m2"]))



    implements = Bonus.objects.filter(select='i')
    for implement in serializer.data['implement']:
        try:
            s = implements.get(implement__name=implement["name"])
        except Bonus.DoesNotExist:
            continue

        if s.fr <= date_create and s.to >= date_create:
            diler.bonus = diler.bonus + (s.count * int(implement["amount"]))


    diler.save()


    return Response({
        'success': True,
    }, status=HTTP_200_OK)



def register(request):
    pass