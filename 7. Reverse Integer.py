# -*- coding: utf-8 -*-
'''
Input: x = 123
Output: 321
'''

x = 1534236469


ans=0
num=abs(x)
while(num>0):
    remainder = num%10
    ans = ans*10+remainder
    num = num//10

if ans>2**31 or ans<-2**31:
    print(0)
else:
    if x<0:
        print(-ans)
    else:
        print(ans)
    












