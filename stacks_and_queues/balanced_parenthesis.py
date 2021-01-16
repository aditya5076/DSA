# import Stack from stack_implementation
def balanced_parenthesis(string):
    # edge case for odd numbers of string
    if len(string)%2!=0:
        return False
        
    opening=set('({[')

    matching=set([('(',')'),('{','}'),('[',']')])

    stack=[]
    for paren in string:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack)==0:
                return False
            last_open_paren=stack.pop()
            if (last_open_paren,paren) not in matching:
                return False
    return len(stack)==0
        

print(balanced_parenthesis('[[()]]'))





# alternate approach
    # i=0
    # stack=[]
    # while i<len(string):
    #     if string[i] == '{' or string[i] == '[' or string[i] == '(':
    #         stack.append(i)
    #     else:
    #         stack.pop()
    #     i+=1