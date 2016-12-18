#Mortal fibonacci rabbits
#how many rabbit pairs are there after n months, if each rabbit pair only lives m months.
#each rabbit pair gives birth to 1 pair of rabbits every month.

n=95
m=19

def RabbitCalculator(n, m):
	#create a list where each item is the number of rabbit pairs of a certain age in months.
	#ie if rabbitAges[3] == 2, 2 pairs of rabbits are 4 months old. 
	rabbitAges = [0] * m
	rabbitAges[0] = 1 #start with 1 pair of rabbits at 1 mo. old.

	for i in range(n-1):
		#because only mature rabbits (older than 1 month) can produce babies, 
		#add up all the pairs older than 1 month and add them together, and set 1st position of 
		#rabbitAges to that value. The rest of the rabbits are 1 month older, and oldest rabbits will
		#die after reaching rabbitAges[m-1]. 
		rabbitAges = [sum(rabbitAges[1:])] + rabbitAges[:-1]
		if i == (n-2):
			print "Total # of rabbits at %d months is " % (i+2), sum(rabbitAges)

RabbitCalculator(n, m)


