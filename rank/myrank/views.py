from django.shortcuts import render, HttpResponse
from django.views import View
from .models import UserInfo, TopScore
from django.db import transaction
from django.http import JsonResponse
import redis
from .utils import POOL
import json


# Create your views here.
class RankSolver(View):

    def get_rank(self, uid, start, end):
        coon = redis.Redis(connection_pool=POOL)
        rank_data = coon.zrevrange("topscore", start, end, withscores=True, score_cast_func=int)
        user_rank_data = {
            coon.zrevrank("topscore", uid) + 1: {
                "uid": uid,
                "client_name": UserInfo.objects.get(id=uid).username,
                "score": int(coon.zscore("topscore", uid))
            }
        }
        all_rank_data = {}
        for index, value in enumerate(rank_data):
            client_name = UserInfo.objects.get(id=value[0]).username
            all_rank_data[index + start + 1] = {
                "uid": int(value[0]),
                "client_name": client_name,
                "score": int(value[1])
            }

        return [all_rank_data, user_rank_data]

    def get(self, request):
        uid = int(request.GET.get("uid"))
        start = int(request.GET.get("start")) - 1
        end = int(request.GET.get("end")) - 1
        all_rank_data = self.get_rank(uid, start, end)
        return JsonResponse(all_rank_data, safe=False)

    @transaction.atomic
    def post(self, request):
        jason_data = json.loads(request.body)
        uid = jason_data.get("uid")
        score = int(jason_data.get("score"))
        print(uid, score)
        coon = redis.Redis(connection_pool=POOL)

        try:
            with transaction.atomic():
                UserInfo.objects.get(id=uid)
                score_log = TopScore.objects.get(uid_id=uid)
                personal_high_score = score_log.personal_high_score
                if personal_high_score < score:
                    score_log.personal_high_score = score
                    score_log.save()
                    coon.zadd("topscore", uid, score)
        except UserInfo.DoesNotExist:
            return HttpResponse("user_id error")
        except TopScore.DoesNotExist:
            TopScore.objects.create(uid_id=uid, personal_high_score=score)
            coon.zadd("topscore", uid, score)
        except Exception as e:
            print(e)
            return HttpResponse("ignored error")

        return HttpResponse("score has been update")
