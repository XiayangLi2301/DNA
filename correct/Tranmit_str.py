def Transmit_str(dna):
    dna = dna.replace('AC','00')
    dna = dna.replace('AG','01')
    dna = dna.replace('TC','10')
    dna = dna.replace('TG','11')
    return dna