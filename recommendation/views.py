from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from recommendation.services import LawyerRecommendationService


# Create your views here.
class RecommendationView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        if user.id:
            lawyer = LawyerRecommendationService.get_laywer(2)

        return HttpResponse(content="")


class LawyerDetailsView(View):
    def get(self, request, *args, **kwargs):
        lawyer_id = request.GET["lawyer_id"]
        try:
            lawyer = LawyerRecommendationService.get_lawyer(lawyer_id)
            return HttpResponse()
        except Exception as e:
            return HttpResponse()
