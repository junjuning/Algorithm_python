from collections import deque

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    
    cities = [city.lower() for city in cities]
    cache = deque()

    for city in cities:
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
    return answer