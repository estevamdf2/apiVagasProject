from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

class VagaList(APIView):
    def post(self, request):
        try:
            serializer = VagaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    
    ''' Responsável por exibir todos os registros salvos.'''
    def get(self, request):
        try:
            lista_vagas = Vaga.objects.all()
            serializer = VagaSerializer(lista_vagas, many=True)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

''' Classe responsável para usar verbos com parametros
    get (findById) put e delete '''
class VagaDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'Mensagem': "O ID deve ser maior que zero."},status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            serializer = VagaSerializer(vaga)
            return Response(serializer.data)
        except Vaga.DoesNotExist:
            return JsonResponse({'Mensagem': "A vaga não existe."},status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'Mensagem': "Ocorreu um erro no servidor."},status=status.HTTP_500_INTERNAL_SERVER_ERROR)