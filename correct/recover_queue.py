def recover(dna_re,group_re,error_re,k):
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
                        del result[0]                         #元素出队
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

        

                    





                

            


