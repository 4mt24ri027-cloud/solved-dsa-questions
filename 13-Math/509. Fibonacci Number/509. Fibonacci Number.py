1class Solution:
2    def fib(self, n: int) -> int:
3        fibo = [0]*(n+1)
4        if n == 0 :
5            return 0 
6        if n == 1:
7            return 1  
8        fibo[0],fibo[1] = 0 , 1
9
10        i = 2
11        while i <= n:
12            fibo[i] = fibo[i-1]+ fibo[i-2]
13            i += 1
14
15        return fibo[n]