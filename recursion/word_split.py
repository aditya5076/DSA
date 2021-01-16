""" factorial """

def fact(n):
    if n==0: #base case
        return 1
    else:
        return n*fact(n-1)


""" n=4321
    answer = 4+3+2+1
"""

def sum_func(n):

    # base case
    if len(str(n)) == 1:
        return n
    
    else:
        return n%10+sum_func(n//10)


# print(sum_func(4321))


""" WORD SPLIT PROBLEM
    given->('iamjohnpapa',['i','am','papa'])
    o/p->(['i','am'])
"""

def word_split(phrase,list_of_words,output=None):

# to initailize with list to add the matching words
    if output is None:
        output=[]

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):],list_of_words,output)
    
    return output

print(word_split('iamjhonpapa',['i','am','papa']))