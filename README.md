1. 客户端上传客户端号和分数(*注意：并不会上传排名,客户端无法上传排名*),同一个客户端可以多次上传分数，取最新的一次分数

   ```
   接口：http://127.0.0.1:8000/rank/get_or_update_rank/
   请求方式：POST
   数据格式:JSON
   {
    "uid":21,#客户端id
    "score":500 #分数
   }
   响应数据：暂定成功或错误状态码
   ```

   <a href='https://github.com/myin1994/rank/blob/master/rank/myrank/views.py'>视图链接</a>

2. 客户端查询排行榜

   ```
   接口：http://127.0.0.1:8000/rank/get_or_update_rank/
   请求方式：GET
   数据格式:PARAMS
   uid 客户端id
   start end 排序起止点
   响应数据：JSON
   对应排序及相关信息
   [
       {
           "1": {
               "uid__id": 49,
               "uid__username": "客户端49",
               "personal_high_score": 1046
           },
           "2": {
               "uid__id": 48,
               "uid__username": "客户端48",
               "personal_high_score": 1045
           },
           "3": {
               "uid__id": 47,
               "uid__username": "客户端47",
               "personal_high_score": 1044
           },
           "4": {
               "uid__id": 46,
               "uid__username": "客户端46",
               "personal_high_score": 1043
           },
           "5": {
               "uid__id": 45,
               "uid__username": "客户端45",
               "personal_high_score": 1042
           }
       },
       {
           "1": {
               "uid__id": 49,
               "uid__username": "客户端49",
               "personal_high_score": 1046
           }
       }
   ]
   ```

3. 附加题

   ```python
   from itertools import zip_longest
   
   version1 = "1.0"
   version2 = "1.0.0"
   
   def compareVersion(version1, version2):
       f = lambda x: map(int, x.split('.'))
       for v1, v2 in zip_longest(f(version1), f(version2), fillvalue=0):
           if v1 != v2:
               return 1 if v1 > v2 else -1
       return 0
   ret = compareVersion(version1,version2)
   print(ret)
   ```

   

