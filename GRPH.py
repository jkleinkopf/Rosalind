
#For a collection of strings and a positive integer k, the overlap graph for the strings is a directed 
#graph Ok in which each string is represented by a node, and string s is connected to string t with a 
#directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s!=t; we demand s!=t
#to prevent directed loops in the overlap graph (although directed cycles may be present).
#Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
#Return: The adjacency list corresponding to O3. You may return edges in any order.f = open('', 'r')

file = raw_input("ENTER FASTA FILE NAME: ")
fna = open(str(file), "r")

names = []
sequences = []

data = fna.read().split(">")
del(data[0])

for i in range(len(data)):
	names.append(data[i].splitlines()[0])
	sequences.append("".join(data[i].splitlines()[1:]))

for i in range(len(sequences)):
	for i2 in range(len(sequences)):
		if i == i2:
			continue
		elif sequences[i][-3:] == sequences[i2][:3]:
			print names[i] + " " + names[i2]

fna.close()