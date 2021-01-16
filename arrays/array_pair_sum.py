# pair_sum([1,3,2,2],4)
# return --> [1,3] and [2,2]

# arr=[1,3,2,2]
# time O(n^2) | O(1)
# def pair_sum(arr,target):
#     for i in range(0,len(arr)):
#         for j in range(1,len(arr)+1):
#             if arr[i]+arr[j] == target:
#                 return [arr[i],arr[j]]
#     return []


# 2-->time O^n BY SETS
def pair_sum(arr,target):
    # base case
    if len(arr)<2:
        return 
    
    # sets for tracking === TRICK
    seen = set()
    output = set()

    for num in arr:
        partial=target-num

        if partial not in seen:
            seen.add(partial)
        else:
            output.add((min(partial,num),max(partial,num)))
    
    print('\n'.join(map(str,list(output)))

pair_sum([1,3,2,2],4)

            



