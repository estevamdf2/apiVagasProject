from django.shortcuts import render

# Create your views here.
class VagaList(APIView):
    def get(self, request):
           try:
            lista_vagas = Vaga.objects.all()
            paginator = PaginacaoVagas()
            result_page = paginator.paginate_queryset(lista_vagas, request)
            serializer = VagaSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
         Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)