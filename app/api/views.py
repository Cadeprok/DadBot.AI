from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getChatBotResponse(request):
    person = {1: '1'}

    return Response(person)

@api_view(['GET'])
def home(request):
    return Response({1:'2'})