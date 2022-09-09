"""

This module is the encoding for DNA-LC

"""


import math
import numpy as np

def encode_lc(origin):

    """

    ----------------------------------------------------------------------
    Take a string of binary sequences and return a string of DNA sequences
    ----------------------------------------------------------------------

    :param: origin: a string of binary sequences which you input
    :type: origin: list

    :Test cases:
    Input: origin = [1,1,0,0,1,0,0]
    Output: dna = 'TGTGTCACTCAC'
    Input: origin = [1,1,0,0,1,0,0,1]
    Output: The sequence length you provided does not meet our encoding requirements


    
    """
    len_org = len(origin)
    len_enc = len_org
    while(len_org > len_enc - math.ceil(np.log2(len_enc))-1):
        len_enc = len_enc + 1
    if(len_enc % 2 != 0):
        print('The sequence length you provided does not meet our encoding requirements')
    ind = []
    for i in range(len_enc-1):
        if np.log2(i+1) - int(np.log2(i+1)) != 0:
            ind.append(i+1)
    pla_1 = np.dot(ind,origin)
    rem = 2*len_enc - pla_1 % (2*len_enc)
    if rem > 2**(math.ceil(np.log2(len_enc))) - 1:
        rem = rem - len_enc
        bina = bin(rem)
        par = []
        for i in range(2,len(bina)):
            par.append(int(bina[i]))
        loc = 0
        for i in range(len_enc - 1):
            if np.log2(i + 1) - int(np.log2(i + 1)) == 0:
                loc += 1
                if loc <= len(par):
                    origin.insert(i, par[-loc])
                else:
                    origin.insert(i, 0)
        origin.insert(len_enc, 1)
    else:
        bina = bin(rem)
        par = []
        for i in range(2,len(bina)):
            par.append(int(bina[i]))
        loc = 0
        for i in range(len_enc - 1):
            if np.log2(i + 1) - int(np.log2(i + 1)) == 0:
                loc += 1
                if loc <= len(par):
                    origin.insert(i, par[-loc])
                else:
                    origin.insert(i, 0)
        origin.insert(len_enc, 0)
    dna = [str(i) for i in origin]
    k = len(dna)
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