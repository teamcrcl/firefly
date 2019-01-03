from rest_framework import views, status
from rest_framework.response import Response

from countries.models import Country
from countries.serializers import CountrySerializer


class FetchCountries(views.APIView):

    def get(self, request, **kwargs):
        countries = Country.objects.all()
        return Response({"Success": CountrySerializer(countries, many=True).data}, status=status.HTTP_200_OK)


