# You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining the maximum amount
#  of power output per array, and to do THAT, you'll first need to figure out what the maximum output of each array actually is. 
# Write a function solution(xs) that takes a list of integers representing the power output levels of each panel in an array, 
# and returns the maximum product of some non-empty subset of those numbers. So for example, if an array contained panels with power 
# output levels of [2, -3, 1, 0, -5], then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, 
# giving the product 2*(-3)*(-5) = 30.  So solution([2,-3,1,0,-5]) will be "30".

def solution(xs):
    # use all non-0 numbers
    # get rid of the smallest negative to make it an even number of negatives
    prod = 1
    smallest_neg=-1001
    for i in xs:
        if i!=0:
            prod*=i
            if i<0 and smallest_neg<i:
                smallest_neg=i
    if prod<0 and len(xs)!=1: # edge case: 1 negative number
        prod/=smallest_neg
    if prod==1 and 1 not in xs: # edge case: all 0s
        return str(0)
    
    return str(prod)

print(solution([2, 0, 2, 2, 0]))
