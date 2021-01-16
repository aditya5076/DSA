# clint eastwood=old west action

# 1->easy  way
# def anagram(str1,str2):
#     # if(str1.length!=str2.length):
#     #     return False
#     str1=str1.replace(' ','').lower()
#     str2=str2.replace(' ','').lower()
#     return sorted(str1)==sorted(str2)


# 2->manual way
def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    count={}
    for letter in s1: #add letter with count =1
        if letter in count:
            count[letter]+=1
        else:
            count[letter]=1
    # for s2
    for letter in s2: #add letter with count =1
        if letter in count:
            count[letter]-=1
        else:
            count[letter]=1

    for key in count: 
        if count[key]!=0:
            return False
    return True



if __name__ == "__main__":
    check=anagram('god','dog')
    # print(check)

    

