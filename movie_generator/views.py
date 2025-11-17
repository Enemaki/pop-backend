from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .search import get_movie_recommendation

class MovieRecommendationView(APIView):
    def post(self, request, format=None):
        preferences = request.query_params.get('preferences', '')
        # if not preferences:
        #     return Response({"error": "Preferences parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        recommendations = get_movie_recommendation(preferences)
        return Response({"recommendations": recommendations}, status=status.HTTP_200_OK)