#Last recently used를 사용함
#캐시크기 , 도시이름배열 - cache hit : 1, cache miss : 5
#큐에 넣고... 제일 왼쪽이 제일 오래전에 사용한 도시가 되도록 할 수 있나?
#사용되고 큐에 있으면- 큐에서 지우고 다시 append하고 cache hit : 1
#사용되고 큐에 없으면 ~ append하고 cache miss : 5
from collections import deque
def solution(cacheSize, cities):
    cache = {}
    exec_time = 0
    if cacheSize == 0 :
        return 5*len(cities)
    for i, city in enumerate(cities) : 
        city = city.lower()
        if city in cache : 
            cache[city] = i
            exec_time += 1
            continue
        if len(cache) < cacheSize and city not in cache :
            cache[city] = i
            exec_time += 5
            continue
        if cache and city not in cache : 
            min_v = ["", float('inf')]
            for k, v in cache.items() :
                if min_v[1] >= v : 
                    min_v[0] = k
                    min_v[1] = v
            cache.pop(min_v[0])
            cache[city] = i
            exec_time += 5
    return exec_time