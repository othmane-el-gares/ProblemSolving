def miniMaxSum(arr):
    # Write your code here
    narr=sorted(arr)
    ms=sum(narr[:-1])
    mxs=sum(narr[1:])
    print(f"{ms} {mxs}")