# n=2
# output->['00','10','01','11']
# n-3
# output->['000','001','010','011','100','101','110','111']

def append_bit(x,l):
    # if l=['1','0'] and x=0
    # ['0'+'1'] and ['0'+'0']
    # output-->['01','00']
    return [x + element for element in l]

def generate_bit(n):
    if n == 0 : return []
    if n == 1 : return ['0','1']
    else:
        return append_bit('0',generate_bit(n-1))+append_bit('1',generate_bit(n-1))

print(generate_bit(3))


