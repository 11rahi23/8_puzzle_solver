import heapq

h = []
heapq.heappush(h, (5, 6))
heapq.heappush(h, (7, 2))
heapq.heappush(h, (1, 8))
heapq.heappush(h, (3, 4))
heapq.heappush(h, (3, 5))
print(h)
h=heapq.heapsort(h)
p=heapq.heappop(h)
print(p)
print(h)