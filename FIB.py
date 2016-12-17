n = 33 #number of months
k = 4 #number of offspring pairs for every mature rabbit pair

e = [0] * n #create a list of length n, months. Value of e[n] is number of rabbit pairs living in that month.

e[0] = 1 #set e[0] and e[1] = 1 for the starting pair of rabbits
e[1] = 1

for i in range(n-2): #3rd month is equal to 2nd month + 1st month * 3. 
	e[i+2] = ( e[i+1] + k*e[i] )

print e[n-1]
