""" EASY  """


# def removeDuplicates(nums):
#     # PYTHON TRICK
#     # length=len(set(nums))
#     # return list(set(list(nums))),int(length)

""" TWO POINTER APPROACH """
#     if not nums:
#         return 0
#     i=0
#     j=1
#     for j in range(len(nums)):
#         if nums[i] != nums[j]:
#             i+=1
#             print("i-->",nums[i])
#             print("j-->",nums[j])
#             nums[i]=nums[j]
#         else:
#             continue
#     return i+1

# if __name__ == "__main__":
#     nums=[0,0,1,1,1,2,2,3,3,4]
#     print(removeDuplicates(nums))

""" MEDIUM
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3]
Explanation: Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It doesn't matter what you leave beyond the returned length.

"""
def removeDuplicates(nums):
    initial=0
    for cur_num in nums:
        if initial < 2 or cur_num > nums[initial - 2]:
            nums[initial] = cur_num
            print(nums)
            initial+=1
    return initial

if __name__ == "__main__":
    nums=[1,1,1,2,2,3]
    print("result:",removeDuplicates(nums))