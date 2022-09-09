from tool import right_code, count_S, error_find, fun_solve, recover, per
from co_single import co_single
from silico import lc_sil,err_sil,err_sil_1,err_sil_2

def result(r_1,r_2,m):


    """
    
    ---------------------------------------------------------------
    Return all the feasible corrected results without calculating S
    ---------------------------------------------------------------

    param: r_1: A right DNA sequence.
           r_2: A DNA sequence equipped with errors
           m: The bound of misplacement index
    
    type: r_1: list
          r_2: list
          m: int

    Test Cases: 
    Input: dna = 'AGTCTCTG'
    Output: 9

    
    """


    group = [[]]
    final_result = []
    r_2 = list(r_2) 
    l = len(r_2) 
    error_list = error_find(r_2)[0] 
    error_num = error_find(r_2)[1] 
    if error_num > m:
        return []
    k = right_code(r_1)[0] 
    x = fun_solve(k,l,error_num) 
    if(x[0] >= 0 and x[1] >= 0):
        if error_num == 0:
            r_2 = ''.join(r_2)
            final_result.append(list(co_single(r_1,r_2)))
        else:
            if (x[0] > 0):
                group = per(error_list,int(x[0]))
            x = (group)
            len_del = len(x) 
            for i in range(0,len_del):
                r_3 = r_2[:]
                error_list_2 = error_list[:]
                final_result.extend(recover(r_3,group[i],error_list_2,l))
    return final_result


def final_result(r_1,r_2,m):


    """
    
    ---------------------------------------------------------------
    Return the final corrected results without calculating S
    ---------------------------------------------------------------

    param: r_1: The right DNA sequence
           r_2: The DNA sequence equipped with errors
           m: The bound of misplacement index
    
    type: r_1: list
          r_2: list
          m: int

    Test Cases: 
    Input: dna = 'AGTCTCTG'
    Output: 9

    
    """
    list_result = result(r_1,r_2,m)
    Array = (list_result)
    medium_len = len(Array)
    S = right_code(r_1)[1]
    medium_str = []
    final_result_1 = []
    for i in range(medium_len):
        medium_str.append(''.join(list_result[i]))
    
    
    for i in range(medium_len):
        S1 = count_S(medium_str[i])
        if S1 == S:
            final_result_1.append(medium_str[i])
    if final_result_1 == []:
        for i in range(medium_len):
            if(co_single(r_1,medium_str[i]) != ''):
                final_result_1.append(co_single(r_1,medium_str[i]))
    final_result = []
    [final_result.append(i) for i in final_result_1 if not i in final_result]
    k = len(final_result)
    return final_result,k

def correct_rate(list2 , str_list, nums, misplace = 5):

    """
    
    --------------------------------------------
    Calculate the correction rate of DNA-LC code
    --------------------------------------------

    Param: list2: The right DNA sequences
           str_list: The DNA sequences equipped with errors
           nums: the number of simulations
           misplace: the bound of misplacement index

    type: list2: list
          str_list: list
          nums: int
          misplace: int
    
    
    """
    m = misplace
    count = 0
    s = 0 
    for i in range(nums):
        r_1 = list2[i]
        r_2 = str_list[i]
        k = final_result(r_1,r_2,m=5)[1]
        group_1 = final_result(r_1,r_2,m=5)[0]
        if r_1 in group_1:
            count = count + 1/k
            s = s + 1
    print('Correction rate:',end='\t')
    print(count/nums)

if __name__ == '__main__':

    print('------------------------------------')
    print('please choose the type of error:(1/2/3)')
    print('1-> all three errors')
    print('2-> deletions')
    print('3-> inconsecutive deletions')

    ty = int(input())
    if ty == 1:
        print('please input the length of message squence:')
        lens = int(input())
        print('Please enter the number of simulations:')
        nums = int(input())
        print('Please input the rate of substitution:')
        a = float(input())
        print('Please input the rate of insertions:')
        b = float(input())
        print('please input the rate of deletion:')
        c = float(input())
        err_rate = [a,b,c]
        right_dna = lc_sil(lens, nums)   #Generate the right DNA sequences
        error_dna = err_sil(err_rate, right_dna)    # make errors
    if ty == 2:
        print('please input the length of message squence:')
        lens = int(input())
        print('Please enter the number of simulations:')
        nums = int(input())
        print('Please input the number of deletions:')
        a = int(input())
        right_dna = lc_sil(lens, nums)   #Generate the right DNA sequences
        error_dna = err_sil_1(right_dna, a) 
    if ty == 3:
        print('please input the length of message squence:')
        lens = int(input())
        print('Please enter the number of simulations:')
        nums = int(input())
        print('Please input the number of inconsecutive deletions:')
        a = int(input())
        right_dna = lc_sil(lens, nums)   #Generate the right DNA sequences
        error_dna = err_sil_2(right_dna, a) 
    import time
    time_start=time.time()
    print(correct_rate(right_dna, error_dna, nums))   # calculate the correction rate
    time_end=time.time()
    print('totally cost',time_end-time_start)

