# 재귀적용법을 활용한 피보나치 수열

def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)
# 비재귀적 용법
def fib(num):
    a,b = 1,1
    if num ==1 or num ==2:
        return 1

    for i in range(1,num):
        a,b = b,a+b
    
    return a

# i = 1 : 1,2
# i = 2 : 2,3
# i = 3 : 3,5


# 1 : 1
# 2 : fibo(1) + fibo(0) : 1 + 0 : 1
# 3 : fibo(2) + fibo(1) : 1 + 1 : 2
# 4 : fibo(3) + fibo(2) : 2 + 1 : 3



num = int(input())
print(fibo(num))
print(fib(num))






