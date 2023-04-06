from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
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
@permission_classes((IsAdminUser,))
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
    

    date_create = datetime.strptime(serializer.data["date_create"], '%y-%m-%d')

    shapes = Bonus.objects.filter(select='s')
    for shape in serializer.data['shape']:
        s = shapes.get(shape__name=shape["name"])


        if s.fr <= date_create and s.to >= date_create:
            diler.bonus = diler.bonus + (s.count * (int(shape["m2"]) // 1))



    glazings = Bonus.objects.filter(select='g')
    for glazing in serializer.data['glazing']:
        s = glazings.get(glazing__name=glazing["name"])


        if s.fr <= date_create and s.to >= date_create:
            diler.bonus = diler.bonus + (s.count * (int(glazing["m2"]) // 1))



    implements = Bonus.objects.filter(select='i')
    for implement in serializer.data['implement']:
        s = implements.get(implement__name=implement["name"])
        if s.fr <= date_create and s.to >= date_create:
            diler.bonus = diler.bonus + (s.count * (int(glazing["amount"]) // 1))


    return Response({
        'success': True,
    }, status=HTTP_200_OK)