# The fuel control mechanisms have three operations: 1) Add one fuel pellet2) Remove one fuel pellet3) Divide the entire group of fuel 
# pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only 
# allow this to happen if there is an even number of pellets)Write a function called solution(n) which takes a positive integer as a 
# string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can 
# only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.
# if the least significant bit is zero, then divide by 2
# if n is 3, or the 2 least significant bits are 01, then subtract
# In all other cases: add.
import math
def solution(n):
    n=int(n)
    count=0
    while n!=1:
        if n%2==0:
            n/=2
        elif n==3 or n%4==1:
            n-=1
        else:
            n+=1
        count+=1
    return count

print(solution('15'))