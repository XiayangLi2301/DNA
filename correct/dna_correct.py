import gailv
from gailv import gailv1
def error_find(dna_code):
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
        list1.append(l)
        count = count + 1
    return[list1,count]


def count_S(dna):
    k = len(dna)
    s = 0
    dna = dna.replace('AC','00')
    dna = dna.replace('AG','01')
    dna = dna.replace('TC','10')
    dna = dna.replace('TG','11')
    for i in range(1,k):
        s = s + i *int(dna[i-1])
    return s%(2*k)

def Transmit_str(dna):
    dna = dna.replace('AC','00')
    dna = dna.replace('AG','01')
    dna = dna.replace('TC','10')
    dna = dna.replace('TG','11')
    return dna

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

def right_code(right_dna):
    k = len(right_dna)
    S = count_S(right_dna)
    return [k,S,right_dna]

def dna_correct(dna_code1,dna_code2):
    k = right_code(dna_code1)[0]
    S = right_code(dna_code1)[1]
    #print(S)
    l = len(dna_code2)
    error_num = int(error_find(dna_code2)[1])
    if error_num <= 1 and abs(k-l) <= 1:
        if l == k:
            if (error_num == 1):
                error_place = int(error_find(dna_code2)[0][0])
                if error_place%2 == 0:
                    dna_code2 = list(dna_code2)
                    dna_code3 = dna_code2[:]
                    dna_code2[error_place] = 'C'
                    dna_correct1 = dna_code2
                    dna_code3[error_place] = 'G'
                    dna_correct2 = dna_code3
                else:
                    dna_code2 = list(dna_code2)
                    dna_code3 = dna_code2[:]
                    dna_code2[error_place] = 'A'
                    dna_correct1 = dna_code2
                    dna_code3[error_place] = 'T'
                    dna_correct2 = dna_code3
            else:
                T = count_S(dna_code2)
                if abs(T-S) <= k:
                    dna_code2 = Transmit_str(dna_code2)
                    dna_code2 = list(dna_code2)
                    if(dna_code2[abs(T-S)-1] == '1'):
                        dna_code2[abs(T-S)-1] = '0'
                    else:
                        dna_code2[abs(T-S)-1] = '1'
                    
                    # print(dna_code2)
                    dna_code2 = ''.join(dna_code2)
                    dna_correct = Transmit_number(dna_code2)
                else:
                    dna_code2 = Transmit_str(dna_code2)
                    dna_code2 = list(dna_code2)
                    if(dna_code2[2*k-abs(T-S)-1] == '0'):
                        dna_code2[2*k-abs(T-S)-1] = '1'
                    dna_code2 = ''.join(dna_code2)
                    dna_correct = Transmit_number(dna_code2)
                return dna_correct

        if l == k - 1 :
            error_place = int(error_find(dna_code2)[0][0])
            if (error_place%2==0):
                dna_code2 = list(dna_code2)
                dna_code3 = dna_code2[:]
                dna_code2.insert(error_place-1,'C')
                dna_correct1 = dna_code2
                dna_code3.insert(error_place-1,'G')
                dna_correct2 = dna_code3
            if (error_place%2==1 and error_place != k-1):
                dna_code2 = list(dna_code2)
                dna_code3 = dna_code2[:]
                dna_code2.insert(error_place-1,'A')
                dna_correct1 = dna_code2
                dna_code3.insert(error_place-1,'T')
                dna_correct2 = dna_code3
            if(error_place == k-1):
                dna_code2 = list(dna_code2)
                dna_code3 = dna_code2[:]
                dna_code2.append('C')
                dna_correct1 = dna_code2
                dna_code3.append('G')
                dna_correct2 = dna_code3
                # print(dna_correct1)
        
        if l == k + 1 :
            error_place = int(error_find(dna_code2)[0][0])
            if error_place > 1:
                dna_code2 = list(dna_code2)
                dna_code3 = dna_code2[:]
                del dna_code2[error_place - 1]
                del dna_code3[error_place - 2]
                dna_correct1 = dna_code2
                dna_correct2 = dna_code3
            else :
                dna_code2 = list(dna_code2)
                del dna_code2[error_place - 1]
                dna_correct = dna_code2
                dna_correct = ''.join(dna_correct)
                return dna_correct

        dna_correct1 = ''.join(dna_correct1)
        dna_correct2 = ''.join(dna_correct2)
        S1 = count_S(dna_correct1)
        S2 = count_S(dna_correct2)
        if S1 == S:
            return dna_correct1
        else :
            return dna_correct2

list2 = gailv1()[0]
str_list = gailv1()[1]
def gailv(list2,str_list):
    count = 0
    for i in range(1000):
        r_1 = list2[i]
        r_2 = str_list[i]
        group_1 = dna_correct(r_1,r_2)
        if group_1 != None:
            if r_1 in group_1:
                count = count + 1
    print(count)
'''
r_1 = input('请输入正确的序列:')      
r_2 = input('请输入要纠正的序列:')
print('正确序列为:'+r_1)
if dna_correct(r_1,r_2) != None:
    print('纠正后的序列为:'+dna_correct(r_1,r_2)) 
    '''
print(gailv(list2,str_list))


