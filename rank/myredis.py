from redis import Redis
redis = Redis(host="127.0.0.1",port=6379,db=1)
# redis.zadd("zet","a3",8,"a2",9)
# print(redis.zcount("zet",1,5))
aa=redis.zrange("zet",1,2,desc=False,withscores=True,score_cast_func=int)
print(aa)