def permutat(string):
    output=[]

    # base case
    if len(string)<=1:
        output.append(string)

    else:
        # for every letter in string
        for index,letter in enumerate(string):

            # for every permutation resulting 'a' and 'bc'
            for perm in permutat(string[:index] + string[index+1:]):
            # permutat('a'+'bc')
                print('perm is ',perm)
                print('current_letter is =>',letter)
                print('current_index is =>',index)

                # add to output
                output+=[letter+perm]
        return output

result=permutat('abc')
print(result)