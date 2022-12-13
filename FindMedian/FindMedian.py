
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):
 # Write your code here
 sarr=sorted(arr)
 md=sarr[len(sarr)//2]
 return md
