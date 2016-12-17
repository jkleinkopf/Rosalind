n = 33
k = 4

e = [0] * n
e[0] = 1
e[1] = 1

for i in range(n-2):
	e[i+2] = ( e[i+1] + k*e[i] )
	
print e
print e[n-1]