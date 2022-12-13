def lonelyinteger(a):
    # Write your code here
    if len (a)==1:
        return a[0]
    for x in a :
        s=[e for e in a if e==x]
        if len(s)==1:
            return x