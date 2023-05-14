# Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that state has gone to the 
# next state and return an array of ints for each terminal state giving the exact probabilities of each terminal state, represented as 
# the numerator for each state, then the denominator for all of them at the end and in simplest form. The matrix is at most 10 by 10. 
# It is guaranteed that no matter which state the ore is in, there is a path from that state to a terminal state. 
# That is, the processing will always eventually end in a stable state. The ore starts in state 0. 
# The denominator will fit within a signed 32-bit integer during the calculation, as long as the fraction is simplified regularly.

# make transition matrix
# do some markov chain stuff

# transition matrix to the power of 100 times
