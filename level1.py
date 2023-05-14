# Write a function called solution(data, n) that takes in a list of less than 100 integers and a number n, 
# and returns that same list but with all of the numbers that occur more than n times removed entirely. 
# The returned list should retain the same ordering as the original list - 
# you don't want to mix up those carefully-planned shift rotations! 
# For instance, if data was [5, 10, 15, 10, 7] and n was 1, solution(data, n)
#  would return the list [5, 15, 7] because 10 occurs twice, and thus was removed from the list entirely.

def solution(data,n):
    #data is a list of less than 100
    #return list with all the numbers that occur more than n times removed
    frequencies = dict()
    #count how many times each number shows up
    for i in data:
        if i in frequencies.keys():
            frequencies[i]+=1
        else:
            frequencies[i]=1
    deleteNums = []
    for key in frequencies:
        if frequencies[key]>n:
            while key in data:
                data.remove(key)
    return data

print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))

