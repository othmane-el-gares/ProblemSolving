#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#
def truckTour(petrolpumps):
 # Write your code here
 pos=fuel=0
 for i in range(len(petrolpumps)):
 fuel+=petrolpumps[i][0]-petrolpumps[i][1]
 if fuel<0:
 pos=i+1
 fuel=0
 return pos
