from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from api.serializers import BonusSerializer
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
)
from core.models import *

@swagger_auto_schema(method='post',request_body=BonusSerializer)
@api_view(["POST"])
@permission_classes((AllowAny,))
def bonus(request):
    serializer = BonusSerializer(data = request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)


    

    return Response({
        'success': True,
    }, status=HTTP_200_OK)