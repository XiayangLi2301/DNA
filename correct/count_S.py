def count_S(dna):
    k =  len(dna)
    s = 0
    dna = dna.replace('AC','00')
    dna = dna.replace('AG','01')
    dna = dna.replace('TC','10')
    dna = dna.replace('TG','11')
    for i in range(1,k+1):
        s = s + i *int(dna[i-1])
        
    return s%(2*k)
