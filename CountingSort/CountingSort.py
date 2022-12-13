def countingSort(arr):
    # Write your code here
    m=max(arr)+1
    res=[0 for i in range(m)]
    for i in range(m):
        res[i]=arr.count(i)
    return res