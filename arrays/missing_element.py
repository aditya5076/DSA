# given finder([1,2,3,4,7,6],[3,2,1,4,7])
# find missing element


# zip method
# a=[1,2,3]
# print(a[-1]) #returns last element i.e 3
# b=[5,6,7]
# for n1,n2 in zip(a,b):
    # print(n1,n2)

# 1-->0nlogn
def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()

    for n1,n2 in zip(arr1,arr2): #will make tuple of 2 element from both arrays at every iter
        if n1!=n2:
            return n1
    return arr1[-1]

# print(finder([1,8,5,8,3],[1,5,8,3]))

# 2-->On
import collections
def finder2(arr1,arr2):
    count=collections.defaultdict(int) #defaultdict->does not throws err if theres no key assigned
    for item in arr2:
        # print(item)
        count[item]+=1
    # count={1: 1, 5: 1, 8: 1, 3: 1}
    # print(count)
    for item in arr1:
        if count[item]==0: #if num is not in count return num
            missing=[]
            missing.append(item)
            print(missing)
        else:
            count[item]-=1
            # print(count)

finder2([1,8,5,3,6,17],[1,5,8,3])

# 3-->clever trick using xor
def finder3(arr1,arr2):
    result=0
    for n in arr1+arr2:
        result^=n
        print(result)
    return result
# print(finder3([1,8,5,8,3],[1,8,8,3]))


