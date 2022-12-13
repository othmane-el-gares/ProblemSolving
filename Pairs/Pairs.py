# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. INTEGER k
# 2. INTEGER_ARRAY arr
#
def pairs(k, arr):
 # Write your code here
 l=[]
 for x in arr:
 for e in arr:
 if abs(x-e)==k:
 l.append(1)


 return int(len(l)/2)