def diagonalDifference(arr):
    # Write your code here
    n=len(arr)
    d1=[]
    d2=[]
    for i in  range(n):
        d1.append(arr[i][i])
        d2.append(arr[i][-i-1])
    return abs(sum(d1)-sum(d2))