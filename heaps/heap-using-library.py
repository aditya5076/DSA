from heapq import heappop,heappush,heapify

my_heap=[]
nums=[12,3,-2,6,4,8,9]

for number in nums:
    heappush(my_heap,number)

while my_heap:
    print(heappop(my_heap))

# ALTERNATE WAY
# heapify(nums)

# print(nums)
