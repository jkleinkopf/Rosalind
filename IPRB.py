#Intro to Mendelian inheritance:
#(Yy x Yy = 1/4YY, 1/2 Yy, 1/4yy. Cross of two individuals. 2 Alleles, Y and y of same trait/factor)
#Y is dominant, y is recessive: YY or Yy individuals will show dominant traits. yy will show recessive traits.
#genotype is Yy or yy or YY. Phenotype is physical appearance of genotype.

#Using probability
#Given: Three positive integers k, m, and n, representing a population containing k+m+n 
#organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n 
#are homozygous recessive.

#Return: The probability that two randomly selected mating organisms will produce an 
#individual possessing a dominant allele (and thus displaying the dominant phenotype). 
#Assume that any two organisms can mate.

#k = individuals, homozygous_dominant_YY
#m = individuals, heterozygous_Yy
#n = individuals, homozygous_recessive_yy

def mendel(k, m, n):
	k = float(k)
	m = float(m)
	n = float(n)
	
	t_pop = k + m + n
	
	#if select dominant phenotype first
	kx_ = k / t_pop #k crossed with anything is dominant
	
	#if select heterozygous phenotype first
	mxk = (m / t_pop) * (k / (t_pop - 1)) 
	mxm = (m / t_pop) * ((m - 1) / (t_pop - 1)) * (0.75) #m x m is only dominant 3/4 of the time
	mxn = (m / t_pop) * (n / (t_pop - 1)) * (0.5) #m x n is only dominant 1/2 of the time
	het_x_dom = mxk + mxm + mxn
	
	#if select recessive phenotype first
	nxk = (n / t_pop) * (k / (t_pop - 1))
	nxm = (n / t_pop) * (m / (t_pop - 1)) * (0.5) #n x m is only dominant 1/2 of the time
	rec_x_dom = nxk + nxm

	dominant_phenotype = kx_ + het_x_dom + rec_x_dom
	print dominant_phenotype
	
mendel(28, 21, 21)
