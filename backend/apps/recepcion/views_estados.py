from rest_framework.views import APIView
from rest_framework.response import Response
from apps.utils.choices import EstadoRecepcionChoices

class EstadoRecepcionChoicesView(APIView):
    def get(self, request):
        return Response([
            {"value": choice.value, "label": choice.label}
            for choice in EstadoRecepcionChoices
        ])
