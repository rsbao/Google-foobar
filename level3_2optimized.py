# Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the 
# next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as 
# the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. 
# It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. 
# That is, the processing will always eventually end in a stable state. The ore starts in state 0. 
# The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly.

# make transition matrix
# do some markov chain stuff

# transition matrix to the power of 100 times
from fractions import Fraction
import timeit
import math
def solution(m):
    # first get rid of unreachable states (to save time) e.g. 8.9ms->7.9ms on 1k iters of test case 2
    # then fix transition matrix
    # run 100 times
    # convert decimal to fraction
    reachable = [] # tells whether state is reachable (1) or unreachable (0)
    s0 = [[]] # represents first state e.g. [1,0,0,0,0,0]
    is_terminal=[] # whether state is terminal or not (0 or 1)
    for i in range(len(m)):
        if(sum(m[i])==0):
            is_terminal.append(1)
        else:
            is_terminal.append(0)
    for col in range(len(m)):
        col_sum = 0
        for row in range(len(m)):
            col_sum+=m[row][col]
        if(col_sum==0): # mark state as unreachable
            reachable.append(0)
        else:
            reachable.append(1)
            
    # add 0s to make s0 size of input
    for i in range(len(m)):
        s0[0].append(0)
    s0[0][0]=1
    # remove unreachable states from s0
    for i in range(1, len(reachable)):
        if reachable[i]==0:
            s0[0].pop()
    orig_len = len(reachable)
    # delete unreachable states from m
    for state in range(orig_len-1,0,-1): # go in reverse order to not mess up indices by deleting entries
        if(reachable[state]==0):
            m.pop(state)
            for row in range(len(m)):
                m[row].pop(state)

    # make terminal states loop to themselves
    for i in range(len(m)):
        if(sum(m[i])==0):
            m[i][i]=1
            
    # normalize matrix to make transition matrix
    for row in range(len(m)):
        row_sum = sum(m[row])
        for col in range(len(m[0])):
            if(sum(m[row])!=0):
                m[row][col]=float(m[row][col])/float(row_sum)
                
    # iterate until convergence
    error=10**(-17)
    e=1
    n=1
    while e>error:
        s1 = mm(s0, m)
        e=0
        for i in range(len(s0[0])):
            e+=(s1[0][i]-s0[0][i])**2
        s0=s1
        n+=1
        
    # turn decimal into fractions
    tuples = []
    s_idx=0
    for s in range(len(is_terminal)):
        if is_terminal[s]==1: # if state is a terminal state, check if it is unreachable. if so, add a (0,1) tuple, else add from the s0 list 
            if reachable[s]==0 and s!=0:
                tuples.append((0,1))
            else:
                tuples.append((Fraction(s0[0][s_idx]).limit_denominator().numerator,Fraction(s0[0][s_idx]).limit_denominator().denominator))
                s_idx+=1
        else:
            s_idx+=1
            
    # find lcm of denoms
    denoms = []
    for tuple in range(len(tuples)):
        denoms.append(tuples[tuple][1])
        
    cur = denoms[0]
    lcm=denoms[0]
    for i in range(1,len(denoms)):
        lcm = find_lcm(lcm,denoms[i])
        
    res = []
    for t in range(len(tuples)):
        res.append(int(tuples[t][0]*(lcm/tuples[t][1])))
    res.append(int(lcm))

    return res

def find_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
def mm(A,B):
    # iterating by row of A
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(B[0])):
            result[i].append(0)
    for i in range(len(A)):
    
        # iterating by column by B
        for j in range(len(B[0])):
    
            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


avgtime=0
for i in range(1000):
    start = timeit.default_timer()
    solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    stop = timeit.default_timer()
    avgtime+=(stop-start)
print(avgtime/100)
