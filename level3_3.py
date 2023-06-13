# To trick the system, you'll need to write a program to return the same security checksum that the bunny trainers would have after they would have checked all the workers through. 
# Fortunately, Commander Lambda's desire for efficiency won't allow for hours-long lines, so the trainers at the checkpoint have found ways to quicken the pass-through rate. 
# Instead of checking each and every worker coming through, the bunny trainers instead go over everyone in line while noting their worker IDs, then allow the line to fill back up. 
# Once they've done that they go over the line again, this time leaving off the last worker. They continue doing this, leaving off one more worker from the line each time 
# but recording the worker IDs of those they do check, until they skip the entire line, at which point they XOR the IDs of all the workers they noted into a checksum and 
# then take off for lunch. Fortunately, the workers' orderly nature causes them to always line up in numerical order without any gaps.
# For example, if the first worker in line has ID 0 and the security checkpoint line holds three workers, the process would look like this:
# 0 1 2 /
# 3 4 / 5
# 6 / 7 8 
# where the trainers' XOR (^) checksum is 0^1^2^3^4^6 == 2.
# Likewise, if the first worker has ID 17 and the checkpoint holds four workers, the process would look like:
# 17 18 19 20 /
# 21 22 23 / 24
# 25 26 / 27 28
# 29 / 30 31 32
# which produces the checksum 17^18^19^20^21^22^23^25^26^29 == 14.
# All worker IDs (including the first worker) are between 0 and 2000000000 inclusive, and the checkpoint line will always be at 
# least 1 worker long. With this information, write a function solution(start, length) that will cover for the missing security checkpoint by outputting the same checksum the trainers
# would normally submit before lunch. You have just enough time to find out the ID of the first worker to be checked (start) and the length of the line (length) before the automatic
# review occurs, so your program must generate the proper checksum with just those two values.

def solution(start, length):
    res = 0
    start_parity = start % 2 # 0 if start is even, 1 if odd
    for n in range(length, 0, -1): # count down from length to 1
        # based on start parity and length of row, we can simplify the xor expression for the row by combining even/odd pairs, and pairs of even/odd pairs
        if (start_parity==0):
            if (n % 2 == 0):
                # if length is even, we will have an integer number of of even/odd pairs
                # if(length%4==0):
                    #do nothing, will have pairs of pairs
                if (n % 4 != 0):
                    #will have odd number of even/odd pairs, just xor with 1
                    res ^= 1
            if (n % 2 == 1):
                # everything xors to 0 except last number in row
                res ^= (start + length - 1 + (length - 1)*(length - n))
                if((n - 1) % 4 != 0): # check if the rest of the even/odd pairs will cancel
                    res ^= 1
        else:
            if(n % 2 == 0):
                # if length of row is even, xor the first and last elements
                res ^= (start + length - 1 + (length - 1)*(length - n)) #last element in row
                res ^= (start + length*(length - n)) #first element in row
                if((n - 2) > 0 and (n - 2) % 4 != 0): # check if the rest of the even/odd pairs will cancel
                    res ^= 1
            else:
                # if length of row is odd, xor the first element
                res ^= (start + length*(length - n)) #first element in row
                if((n - 1) > 0 and (n - 1) % 4 != 0): # check if the rest of the even/odd pairs will cancel
                    res ^= 1 
        if (length % 2 == 1):
            start_parity = not start_parity # flip parity for every row if length is odd
    
        
    print(res)

# NAIVE solution
# def solution2(start, length):
#     res = start
#     for n in range(length):
#         for m in range(length-n):
#             if(n!=0 or m!=0):
#                 res=res^(start+n*length+m)
#     print(res)

                
solution(0,3)
solution2(17,4)
