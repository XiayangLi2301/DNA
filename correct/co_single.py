import count_S
from count_S import count_S
import Transmit_number
from Transmit_number import Transmit_number
import Transmit_str
from Transmit_str import Transmit_str
import right_dna
from right_dna import right_code
def co_single(dna_code1,dna_code2):
    k = right_code(dna_code1)[0]
    S = right_code(dna_code1)[1]
    l = len(dna_code2)
    T = count_S(dna_code2)
    dna_correct = ''
    if abs(T-S) <= k and abs(T-S) > 0:
        dna_code2 = Transmit_str(dna_code2)
        dna_code2 = list(dna_code2)
        if dna_code2[abs(T-S)-1] == '1':
            dna_code2[abs(T-S)-1] = '0'
            dna_code2 = ''.join(dna_code2)
            dna_correct = Transmit_number(dna_code2)
        elif dna_code2[abs(T-S)-1] == '0':
            dna_code2[abs(T-S)-1] = '1'
            dna_code2 = ''.join(dna_code2)
            dna_correct = Transmit_number(dna_code2)
    elif abs(T-S) > k:
        dna_code2 = Transmit_str(dna_code2)
        dna_code2 = list(dna_code2)
        if dna_code2[2*k-abs(T-S)-1] == '0':
            dna_code2[2*k-abs(T-S)-1] = '1'
            dna_code2 = ''.join(dna_code2)
            dna_correct = Transmit_number(dna_code2)
        else:
            dna_code2[2*k-abs(T-S)-1] = '0'
            dna_code2 = ''.join(dna_code2)
            dna_correct = Transmit_number(dna_code2)
    else:
        dna_correct = dna_code2
    return dna_correct
