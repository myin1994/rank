from django.shortcuts import render, HttpResponse
from django.views import View
from .models import UserInfo, TopScore
from django.db import transaction
from django.http import JsonResponse
import json


# Create your views here.
class RankSolver(View):

    def get_rank(self, uid, start, end):
        all_data = TopScore.objects.filter(
            personal_high_score__gte=0).values("uid__id", "uid__username", "personal_high_score").order_by(
            "-personal_high_score")
        rank_data = {}
        user_rank_data = {}
        for index, value in enumerate(all_data, start=1):
            if index >= start and index <= end:
                rank_data[index] = value
            if value.get("uid__id") == uid:
                user_rank_data[index] = value
        return [rank_data,user_rank_data]

    def get(self, request):
        uid = int(request.GET.get("uid"))
        start = int(request.GET.get("start"))
        end = int(request.GET.get("end"))
        all_rank_data = self.get_rank(uid, start, end)
        return JsonResponse(all_rank_data,safe=False)

    @transaction.atomic
    def post(self, request):
        jason_data = json.loads(request.body)
        uid = jason_data.get("uid")
        score = int(jason_data.get("score"))
        print(uid, score)

        try:
            with transaction.atomic():
                UserInfo.objects.get(id=uid)
                score_log = TopScore.objects.get(uid_id=uid)
                personal_high_score = score_log.personal_high_score
                if personal_high_score < score:
                    score_log.personal_high_score = score
                    score_log.save()
        except UserInfo.DoesNotExist:
            return HttpResponse("user_id error")
        except TopScore.DoesNotExist:
            TopScore.objects.create(uid_id=uid, personal_high_score=score)
        except Exception as e:
            print(e)
            return HttpResponse("ignored error")

        return HttpResponse("score has been update")