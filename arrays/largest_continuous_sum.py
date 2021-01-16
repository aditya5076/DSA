# [1,2,-1,3,4,10,10,-10,-1] answer-> 29

def larg_cont_sum_array(arr1):
    max_sum=current_sum=arr1[0]
    for num in arr1[1:]: #iterate from 2nd element
        current_sum=max(current_sum+num,num)
        max_sum=max(current_sum,max_sum)
    return max_sum

print(larg_cont_sum_array([1,2,-1,3,4,10,10,-10,-1]))

