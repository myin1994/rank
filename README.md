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
               "uid": 4,
               "client_name": "客户端4",
               "score": 33300
           },
           "2": {
               "uid": 27,
               "client_name": "客户端27",
               "score": 6474
           },
           "3": {
               "uid": 26,
               "client_name": "客户端26",
               "score": 6454
           },
           "4": {
               "uid": 25,
               "client_name": "客户端25",
               "score": 3454
           },
           "5": {
               "uid": 24,
               "client_name": "客户端24",
               "score": 3444
           },
           "6": {
               "uid": 23,
               "client_name": "客户端23",
               "score": 3424
           },
           "7": {
               "uid": 1,
               "client_name": "客户端1",
               "score": 500
           },
           "8": {
               "uid": 2,
               "client_name": "客户端2",
               "score": 400
           },
           "9": {
               "uid": 3,
               "client_name": "客户端3",
               "score": 100
           }
       },
       {
           "8": {
               "uid": 2,
               "client_name": "客户端2",
               "score": 400
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

   

