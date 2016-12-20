#Given: Six positive integers, each of which does not exceed 20,000. The integers correspond to the 
#number of couples in a population possessing each genotype pairing for a given factor. In order, 
#the six given integers represent the number of couples having the following genotypes:

#    AA-AA
#    AA-Aa
#    AA-aa
#    Aa-Aa
#    Aa-aa
#    aa-aa

#Return: The expected number of offspring displaying the dominant phenotype in the next generation, 
#under the assumption that every couple has exactly two offspring.

AA_AA = 18902
AA_Aa = 19301
AA_aa = 16116
Aa_Aa = 19316
Aa_aa = 18634
aa_aa = 16670

genotypes = [AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa]
expectedDominant = [2, 2, 2, 1.5, 1, 0] #expected # of offspring with dominant phenotype for 2 offspring.
expected = []

def ExpectedDominantOffspring(genotypes):
	for i in range(len(genotypes)):
		expected.append(genotypes[i] * expectedDominant[i])
		total = float(sum(expected))
	return total

print ExpectedDominantOffspring(genotypes)