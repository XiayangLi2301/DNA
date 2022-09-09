"""

This module provide some functions used for error-correction in DNA-LC code

"""


from scipy import linalg
import numpy as np
from itertools import combinations


def count_S(dna):

    """
    
    ------------------------------------------------------------------
    Count the syndrome of a DNA sequence
    ------------------------------------------------------------------

    param: dna: A DNA sequence

    type: dna: str

    Test Cases: 
    Input: dna = 'AGTCTCTG'
    Output: 9

    
    """

    k =  len(dna)
    s = 0
    dna = dna.replace('AC','00')
    dna = dna.replace('AG','01')
    dna = dna.replace('TC','10')
    dna = dna.replace('TG','11')
    for i in range(1,k+1):
        s = s + i *int(dna[i-1])

    return s%(2*k)


def Transmit_number(dna):

    """
    
    -----------------------------------------------
    Transform a binary sequence into a DNA sequence
    -----------------------------------------------

    param: dna: A binary sequence

    type: dna: str

    Test Cases: 
    Input: dna = '1000'
    Output: 'TCAC'

    
    """
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

def Transmit_str(dna):

    """
    
    -----------------------------------------------
    Transform a DNA sequence into a binary sequence
    -----------------------------------------------

    param: dna: A binary sequence

    type: dna: str


    """
    dna = dna.replace('AC','00')
    dna = dna.replace('AG','01')
    dna = dna.replace('TC','10')
    dna = dna.replace('TG','11')
    return dna

def right_code(right_dna):

    """
    
    ----------------------------------------------------------------
    Return the length and the syndrome of an error-free DNA sequence
    ----------------------------------------------------------------

    param: right_dna: A DNA sequence

    type: right_dna: str

 
    """
    k = len(right_dna)
    S = count_S(right_dna)
    return [k,S]

def recover(dna_re,group_re,error_re,k):
    """
    
    --------------------------------------------------------
    Correct multiple errors without computing the syndrome S
    --------------------------------------------------------

    param: dna_re: A DNA sequence to be corrected
           group_re: the insertion locations
           error_re: the misplacement locations
           k: the length of DNA sequence

    type: dna_re: str
          group_re: list
          error_re: list
          k: int
 
    """
    
    aim_re = 0
    count = 1
    count_2 = 0
    result = []
    result.append(dna_re)
    while error_re != []:
        if error_re[0] in group_re:
            if error_re[0] != (k+1):
                if (error_re[0] + aim_re)%2 == 0:
                    while count != 0:
                        r1 = result[0]
                        del result[0]                        
                        count = count - 1
                        r2 = r1[:]
                        r1.insert(error_re[0] + aim_re - 1,'C')
                        result.append(r1)
                        r2.insert(error_re[0] + aim_re - 1,'G')
                        result.append(r2)
                        count_2 = count_2 + 2
                else:
                    while count != 0:
                        r1 = result[0]
                        del result[0]
                        count = count - 1
                        r2 = r1[:]
                        r1.insert(error_re[0] + aim_re - 1,'A')
                        result.append(r1)
                        r2.insert(error_re[0] + aim_re - 1,'T')
                        result.append(r2)
                        count_2 = count_2 + 2
            else:
                while count != 0:
                    r1 = result[0]
                    del result[0]                         #元素出队
                    count = count - 1
                    r2 = r1[:]
                    r1.insert(error_re[0] + aim_re - 1,'C')
                    result.append(r1)
                    r2.insert(error_re[0] + aim_re - 1,'G')
                    result.append(r2)
                    count_2 = count_2 + 2
            count = count_2
            count_2 = 0
            aim_re = aim_re + 1
            del error_re[0]
            del group_re[0]
        else:
            if error_re[0] != k + 1:
                while count != 0:
                    r1 = result[0]
                    del result[0]
                    count = count - 1
                    if(error_re[0]+aim_re-2>=0):
                        r2 = r1[:]
                        del r1[error_re[0]+aim_re-1]
                        result.append(r1)
                        del r2[error_re[0]+aim_re-2]
                        result.append(r2)
                        count_2 = count_2 + 2
                    else:
                        del r1[error_re[0]+aim_re-1]
                        result.append(r1)
                        count_2 = count_2 + 1
            else:
                while count != 0:
                    r1 = result[0]
                    del result[0]
                    count = count - 1
                    del r1[error_re[0]+aim_re-2]
                    result.append(r1)
                    count_2 = count_2 + 1
            count = count_2
            count_2 = 0
            aim_re = aim_re - 1
            del error_re[0]
    return(result)

def fun_solve(n,l,m):

    """
    
    --------------------------------------------------------------------
    Calculate the values of our paper s and t.(insertions and deletions)
    --------------------------------------------------------------------

    param: n: the length of the error-free DNA sequence
           l: the length of the received sequence 
           m: the misplacement index m

    type: n: int
          l: int
          m: int
 
    """   


    A = np.array([[1,-1],[1,1]])
    b = np.array([n-l,m])
    x = linalg.solve(A,b)
    return(x)

def error_find(dna_code):
    """
    
    --------------------------------------------------------------
    Return the location of misplacement and the misplacement index
    --------------------------------------------------------------

    param: dna_code: A DNA sequence

    type: right_dna: str

 
    """   
    l = len(dna_code)
    count = 0
    list1=[]
    for i in range(1,l+1):
        if (i-count) % 2 == 0:
            if (dna_code[i-1] == 'A' or dna_code[i-1] == 'T'):
                list1.append(i)
                count = count + 1
        if (i-count) % 2 == 1:
            if (dna_code[i-1] == 'C' or dna_code[i-1] == 'G'):
                list1.append(i)
                count = count + 1
    if (dna_code[l-1] == 'A' or dna_code[l-1] == 'T'):
        list1.append(l+1)
        count = count + 1 

    return[list1,count]


def per(temp_list,n):
    """
    
    --------------------------------------------------
    Return the combination of error correction schemes
    --------------------------------------------------

    param: temp_list: The error positions of DNA sequence
           n: the number of insertions
    type: temp_list: list
          n: int

 
    """

    temp_list2 = []
    temp_list1 = []
    for c in combinations(temp_list,n):
        temp_list2.append(c)
    for i in temp_list2:
        temp_list1.append(list(i))
    return temp_list1