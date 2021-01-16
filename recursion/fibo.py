def fibo(n):
    # base case
    if n==1 or n==0:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(5))