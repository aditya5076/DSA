"""1) string='hello world' ans='dlrow olleh'
   2) string='abc' ans='cba'
 """

def reverse(string):
    # base case
    if len(string)<=1:
        return string

    # approach for recursion
    return reverse(string[1:]) + string[0]
    """               'bc'             +   'a'
    now, for reverse('bc')
        return reverse('c') + 'b'
        o/p-->'c'+'b'+'a' === cba
    """

print(reverse('hello world'))