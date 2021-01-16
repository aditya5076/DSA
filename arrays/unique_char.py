# 'aabbcc'=>false
# 'abcde'=>true

# using set ds
# def unique_char(s):
#     return len(set(s))==len(s)



# manual approach
def unique_char(s):
    chars=set()
    for letter in s:
        if letter in chars:
           return False
        else:
            chars.add(letter)
    return True

# print(unique_char('abcd'))


"""
n=5
 staircase
     #
    ##
   ###
  ####
 #####

   #
"""

def staircase(n):
    # for row in range(1,n+1):
    #     print(" "*(n-row)+"#"*(row))

    # # for opposite
    # for row in range(1,n+1):
    #     print("#"*(row)+" "*(n-row))


    """ #
       ###
      #####
    """
    row=1
    count=0
    while(row<=n):
        print(" "*(n-row)+"#"*(row+count)+" "*(n-row))
        row+=1
        count+=2
        if(count>=row): count-=1

staircase(10)




""" enumerate use:

profile=['aditya','22','male']

for index,item in enumerate(profile):
    print(index+1,'=>',item)


"""

