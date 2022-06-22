def Transmit_number(dna):
    k = len(dna)
    dna = list(dna)
    for i in range(k):
        if dna[i] == '0' and dna[i+1] == '0':
            dna[i] = 'A'
            dna[i+1] = 'C'
            i = i + 2
        elif dna[i] == '0' and dna[i+1] == '1':
            dna[i] = 'A'
            dna[i+1] = 'G'
            i = i + 2 
        elif dna[i] == '1' and dna[i+1] == '0':
            dna[i] = 'T'
            dna[i+1] = 'C'
            i = i + 2 
        elif dna[i] == '1' and dna[i+1] == '1':
            dna[i] = 'T'
            dna[i+1] = 'G'
            i = i + 2 
    dna = ''.join(dna)
    return dna

    