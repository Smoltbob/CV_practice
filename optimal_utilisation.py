import heapq

def optimal_utilisation(a,b,target):
    heap = []
    res =[]
    for id1, val1 in a:
        for id2, val2 in b:
            if val1 + val2 <= target:
                heapq.heappush(heap, (-(val1 + val2), id1, id2))

    while heap[0][0] == -target:
        elem = heapq.heappop(heap)
        res.append([elem[1], elem[2]])

    if not res:
        elem = heapq.heappop(heap)
        res.append([elem[1], elem[2]])

    return res

a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

print(optimal_utilisation(a,b,target))

a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10
print(optimal_utilisation(a,b,target))
