# hey there   how are you
# ans-->you are how there hey

def my_reversed(s):
    return " ".join(s[::-1])

def rev_word(s):
    words=[]
    length=len(s)
    spaces=[' ']
    i=0
    while i<length:
        if s[i] not in spaces:
            word_start=i #will start storing letters till it find the space
            print(word_start)
            while i<length and s[i] not in spaces:
                i+=1
            words.append(s[word_start:i])
            print(words)
            
        i+=1
    return my_reversed(words)


# one liner
def easy_rev_word(s):
    return " ".join(reversed(s.split()))

print(rev_word('hey   hi'))