
import def_solve
import gc
import error_find
import right_dna
import per
import count_S
import recover_queue
import Transmit_str
import numpy as np
import co_single
import gailv
from gailv import gailv1
from def_solve import fun_solve
from error_find import error_find
from right_dna import right_code
from per import per
from count_S import count_S
from recover_queue import recover
from Transmit_str import Transmit_str
from co_single import co_single
# r_1 = input('请输入正确的序列:')      
# r_2 = input('请输入要纠正的序列:')
def result(r_1,r_2):
    group = [[]]
    final_result = []
    r_2 = list(r_2) #列表化
    l = len(r_2) # 待修复序列的长度
    error_list = error_find(r_2)[0] #错位标记
    # print(error_list)
    error_num = error_find(r_2)[1] #错位个数
    k = right_code(r_1)[0] #正确 dna 的长度
    x = fun_solve(k,l,error_num) #删除数和增添数 x[0],x[1]
    if(x[0] >= 0 and x[1] >= 0):
        if error_num == 0:
            r_2 = ''.join(r_2)
            final_result.append(list(co_single(r_1,r_2)))
        else:
            if (x[0] > 0):
                group = per(error_list,int(x[0]))
            x = (group)
            len_del = len(x) #排列组合数
            for i in range(0,len_del):
                r_3 = r_2[:]
                # print(r_3)
                error_list_2 = error_list[:]
                # print(group[i],error_list)
                # print(recover(r_3,0,group[i],error_list_2,l))
                final_result.extend(recover(r_3,group[i],error_list_2,l))
                # print(final_result)
                # print(group[i],error_list)
        # print(final_result)
    return final_result
def final_result(r_1,r_2):
    list_result = result(r_1,r_2)#记录长度
    # print(list)
    Array = (list_result)
    medium_len = len(Array)
    # print(medium_len)
    S = right_code(r_1)[1]
    # print(S)
    medium_str = []
    final_result_1 = []
    for i in range(medium_len):
        medium_str.append(''.join(list_result[i]))
    # print(medium_str)
    
    
    for i in range(medium_len):
        S1 = count_S(medium_str[i])
        # print(S1)
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

list2 = gailv1()[0]
str_list = gailv1()[1]


'''
a = input('序列1')
b = input('序列2')
list2=[]
str_list = []
list2.append(a)
str_list.append(b)
'''


def gailv(list2,str_list):
    count = 0
    s = 0 
    for i in range(10000):
        r_1 = list2[i]
        r_2 = str_list[i]
        k = final_result(r_1,r_2)[1]
        group_1 = final_result(r_1,r_2)[0]
        if r_1 in group_1:
            count = count + 1/k
            s = s + 1
            print(s)
    print('纠错率:',end='\t')
    print(count/10000)

'''
def gailv(list2,str_list):
    for i in range(10000):
        print(list2[i],end='\t')
        print(str_list[i],end='\n')
        str1 = list2[i]
        str2 = str_list[i]
        final_result(str1,str2)
'''


#print(final_result(r_1,r_2))

import time
time_start=time.time()
print(gailv(list2,str_list))


time_end=time.time()
print('totally cost',time_end-time_start)