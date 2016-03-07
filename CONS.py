f = open("rosalind_cons.txt", "r")
#print file.read()
file= f.read()

data = file.split(">")
del data[0]

strand = []

for i in range(len(data)):
	strand.append("".join(data[i].splitlines()[1:])) 

length = 0

for i in strand:
	if len(i) > length:
		length = len(i)

A = [0] * length
C = [0] * length
G = [0] * length
T = [0] * length

for i in strand:	
	for x in range(len(i)):
		if i[x] == "A":
			A[x] += 1
		elif i[x] == "C":
			C[x] += 1
		elif i[x] == "G":
			G[x] += 1
		elif i[x] == "T":
			T[x] += 1
			
consensus = []

for i in range(len(A)):
	if A[i] > C[i] and A[i] > G[i] and A[i] > T[i]:
		consensus.append("A")
	elif C[i] > A[i] and C[i] > G[i] and C[i] > T[i]:
		consensus.append("C")
	elif G[i] > A[i] and G[i] > C[i] and G[i] > T[i]:
		consensus.append("G")
	elif T[i] > A[i] and T[i] > C[i] and T[i] > G[i]:
		consensus.append("T")
	elif A[i] == C[i] and A[i] > G[i] and A[i] > T[i]:
		consensus.append("A")
	elif A[i] == G[i] and A[i] > C[i] and A[i] > T[i]:
		consensus.append("A")
	elif A[i] == T[i] and A[i] > C[i] and A[i] > G[i]:
		consensus.append("A")
	elif C[i] == G[i] and C[i] > A[i] and C[i] > T[i]:
		consensus.append("C")
	elif C[i] == T[i] and C[i] > A[i] and C[i] > G[i]:
		consensus.append("C")
	elif G[i] == T[i] and G[i] > A[i] and G[i] > C[i]:
		consensus.append("G")
	elif A[i] == C[i] and A[i] == G[i]:
		consensus.append("A")
	elif A[i] == C[i] and A[i] == T[i]:
		consensus.append("A")
	elif A[i] == G[i] and A[i] == T[i]:
		consensus.append("A")
	elif C[i] == G[i] and C[i] == T[i]:
		consensus.append("C")
	elif A[i] == G[i] and A[i] == C[i] and A[i] == T[i]:
		consensus.append("A")
	else:
		consensus.append("X")
		
print "".join(consensus)

print "A:",
for i in range(len(A)):
	print A[i],

print "\nC:",
for i in range(len(A)):
	print C[i],

print "\nG:",
for i in range(len(A)):
	print G[i],
	
print "\nT:",
for i in range(len(A)):
	print T[i],		
	
	
	

