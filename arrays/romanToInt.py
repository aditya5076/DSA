"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Input: s = "IV"
Output: 4
"""

def romanToInt(s):
    _dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    prev=0
    sum=0
    for i in s[::-1]: #reverse s-->if [IV] ---> [VI]
        current_value=_dict[i]
        if prev > current_value:
            sum-=current_value
        else:
            sum+=current_value
        prev=current_value
    return sum
print(romanToInt('VI'))






