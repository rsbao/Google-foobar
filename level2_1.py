# Given a non-empty list of positive integers l and a target positive integer t, write a function solution(l, t) which verifies if 
# there is at least one consecutive sequence of positive integers within the list l (i.e. a contiguous sub-list) that can be summed 
# up to the given target positive integer t (the key) and returns the lexicographically smallest list containing the smallest start 
# and end indexes where this sequence can be found, or returns the array [-1, -1] in the case that there is no such sequence 
# (to throw off Lambda's spies, not all number broadcasts will contain a coded message).For example, given the broadcast list l 
# as [4, 3, 5, 7, 8] and the key t as 12, the function solution(l, t) would return the list [0, 2] because the list l contains the 
# sub-list [4, 3, 5] starting at index 0 and ending at index 2, for which 4 + 3 + 5 = 12, even though there is a shorter sequence 
# that happens later in the list (5 + 7). On the other hand, given the list l as [1, 2, 3, 4] and the key t as 15, the function 
# solution(l, t) would return [-1, -1] because there is no sub-list of list l that can be summed up to the given target value t = 15.
# To help you identify the coded broadcasts, Bunny HQ has agreed to the following standards: - Each list l will contain at least 1 element 
# but never more than 100.- Each element of l will be between 1 and 100.- t will be a positive integer, not exceeding 250.- 
# The first element of the list l has index 0. - For the list returned by solution(l, t), the start index must be equal or smaller than 
# the end index. 

def solution(l, t):
    beg=0
    end=0
    runningsum=0
    # add to list until over t
    # if over t, remove beginning of list
    while beg<len(l):
        if(t==runningsum):
            end-=1
            return [beg,end]
        if runningsum<t:
            if(end==len(l)):
                return [-1,-1]
            runningsum+=l[end]
            end+=1
            print("add",runningsum)
        else:
            runningsum-=l[beg]
            beg+=1
            print("minus",runningsum)
            
    print("end")
    return [-1,-1]
            
print(solution([4, 3, 10, 2, 8], 12))