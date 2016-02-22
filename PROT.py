#use the RNA codon table to translate an RNA sequence into a protein sequence.
#this code only translates RNA from the first AUG

codon_table = {
'UUU': 'F',    'CUU': 'L','AUU': 'I', 'GUU': 'V',
'UUC': 'F',    'CUC': 'L','AUC': 'I', 'GUC': 'V',
'UUA': 'L',    'CUA': 'L','AUA': 'I', 'GUA': 'V',
'UUG': 'L',    'CUG': 'L','AUG': 'M', 'GUG': 'V',
'UCU': 'S',    'CCU': 'P','ACU': 'T', 'GCU': 'A',
'UCC': 'S',    'CCC': 'P','ACC': 'T', 'GCC': 'A',
'UCA': 'S',    'CCA': 'P','ACA': 'T', 'GCA': 'A',
'UCG': 'S',    'CCG': 'P','ACG': 'T', 'GCG': 'A',
'UAU': 'Y',    'CAU': 'H','AAU': 'N', 'GAU': 'D',
'UAC': 'Y',    'CAC': 'H','AAC': 'N', 'GAC': 'D',
'UAA': 'Stop', 'CAA': 'Q','AAA': 'K', 'GAA': 'E',
'UAG': 'Stop', 'CAG': 'Q','AAG': 'K', 'GAG': 'E',
'UGU': 'C',    'CGU': 'R','AGU': 'S', 'GGU': 'G',
'UGC': 'C',    'CGC': 'R','AGC': 'S', 'GGC': 'G',
'UGA': 'Stop', 'CGA': 'R','AGA': 'R', 'GGA': 'G',
'UGG': 'W',    'CGG': 'R','AGG': 'R', 'GGG': 'G'
}

sequence = open("rosalind_prot.txt", "r") #open RNA sequence file
s = sequence.read()

start = s.find("AUG")


def translate(s):
	n = 3 #codons are 3 nts long
	lst = [s[i:i+n] for i in range(start,len(s),n)] #creates a list starting at "AUG". Each item is a codon.
	#print lst #test to see list is made up correctly.
	
	prot_seq = []
	for i in lst:
		if i == 'UAA' or i == 'UAG' or i == 'UGA': #stop codons
			break
		else:
			prot_seq.append(codon_table[i])
			
	print "RNA Sequence:"
	print s
	
	print "Protein Sequence:"
	print "".join(prot_seq)

translate(s)
	
	