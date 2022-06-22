import gc
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
        list1.append(l+1)
        count = count + 1 #为了方便,增加一末号位.

    return[list1,count]



