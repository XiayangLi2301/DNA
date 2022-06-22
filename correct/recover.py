import gc
result = []
def recover(dna_re,aim_re,group_re,error_re,k):
    r1 = dna_re
    if error_re != []:
        if error_re[0] in group_re:
            if error_re[0] != (k+1):
                if (error_re[0] + aim_re)% 2 == 0:
                    group_re_1 = group_re[:]
                    error_re_1 = error_re[:]
                    r2 = r1[:]
                    r1.insert(error_re[0]+aim_re-1,'C')
                    del group_re[0]
                    del error_re[0]
                    recover(r1,aim_re+1,group_re,error_re,k)
                    # del r1
                    # gc.collect()
                    r2.insert(error_re_1[0]+aim_re-1,'G')
                    del group_re_1[0]
                    del error_re_1[0]
                    recover(r2,aim_re+1,group_re_1,error_re_1,k)
                    # del r2
                    # gc.collect()
                else:
                    group_re_1 = group_re[:]
                    error_re_1 = error_re[:]
                    r2 = r1[:]
                    r1.insert(error_re[0]+aim_re-1,'A')
                    del group_re[0]
                    del error_re[0]
                    recover(r1,aim_re+1,group_re,error_re,k)
                    # del r1
                    # gc.collect()
                    r2.insert(error_re_1[0]+aim_re-1,'T')
                    del group_re_1[0]
                    del error_re_1[0]
                    recover(r2,aim_re+1,group_re_1,error_re_1,k)
                    # del r2
                    # gc.collect()
            else:
                group_re_1 = group_re[:]
                error_re_1 = error_re[:]
                r2 = r1[:]
                r1.insert(error_re[0]+aim_re-1,'C')
                del group_re[0]
                del error_re[0]
                recover(r1,aim_re+1,group_re,error_re,k)
                # del r1
                # gc.collect()
                r2.insert(error_re_1[0]+aim_re-1,'G')
                del group_re_1[0]
                del error_re_1[0]
                recover(r2,aim_re+1,group_re_1,error_re_1,k)
                # del r2
                # gc.collect()
        else:
            if error_re[0] != 1 and error_re[0] != k+1:
                error_re_1 = error_re[:]
                r2 = r1[:]
                group_re_1 = group_re[:]
                del r1[error_re[0]+aim_re-1]
                del error_re[0]
                recover(r1,aim_re-1,group_re,error_re,k)
                # del r1
                # gc.collect()
                del r2[error_re_1[0]+aim_re-2]
                del error_re_1[0]
                recover(r2,aim_re-1,group_re_1,error_re_1,k)
                # del r2
                # gc.collect()
            elif error_re[0] == 1:
                del r1[error_re[0]+aim_re-1]
                del error_re[0]
                recover(r1,aim_re-1,group_re,error_re,k)
                # del r1
                # gc.collect()
            else:
                del r1[error_re[0]+aim_re-2]
                del error_re[0]
                recover(r1,aim_re-1,group_re,error_re,k)
                # del r1
                # gc.collect()
    else:
        global result
        result.append(dna_re)
    return result



