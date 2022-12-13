def palindromeIndex(s):
 # Write your code here
 l=len(s)
 def test(ch):
 for i in range(len(ch)):
 return ch[i]!=ch[-i-1]
	if test(s):
 if test(s):
 	return -1 
 elif l<=2: 
 	return -1 
 else :
 	ind=-1
 	for i in range(l):
 	if s[i]!=s[-i-1]:
 		ind=i
 		break
 
	return ind