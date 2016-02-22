"""The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""

file = raw_input("Enter FASTA file name > ") #choose fasta/txt file

f = open(str(file), "r")
data = f.read().split(">") #New list called data. Each item is the name and sequence. Removes ">".

del data[0] #Delete the first item in data, which is a blank.


gc, strand, gc_cont = [], [], [] #num of GC in each sample, sample sequence, and gc/strand length
index, highest_gc = 0, 0 


for i in range(len(data)): #loop through indices in data
	strand.append("".join(data[i].splitlines()[1:])) 
		#splits each list item in data by line into a new list. Joins all but first item. 
		#strand is a list of sequences.
		
	gc.append(strand[i].count("G")+strand[i].count("C"))
		#counts the number of "G" and "C" in each sequence. Appends that number to gc list.
		
	gc_cont.append(100 * float(gc[i]) / len(strand[i]))
		#calculates gc content (as a %) by dividing gc at index i by length of strand at index i.
	
	if gc_cont[i] > highest_gc: 
			#makes index and highest_gc the index of the greatest value gc_cont.
		index = i
		highest_gc = gc_cont[i]
		
		
print str(data[index].splitlines()[0]) + "\n" + str(gc_cont[index]) + "%"
	#prints the name of the highest gc_cont sample.
	#prints new line.
	#prints biggest gc_cont value and % symbol.
	
f.close()
	


