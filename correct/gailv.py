import numpy as np
list2 = []
list1 = []
#for i in range(0,10):
  #  for j in range(0,10):
   #     list1.append(np.random.choice([1,2,3,0],p=p)
    #    list1
 #   list.append(list1)
 #   list1 = []

#print(list)

list2 = []
list1 = []
for j in range(0,10000):
    for j in range(0,150):
        k = np.random.choice(['AC','AG','TC','TG'])
        list1.append(k)
    list1=''.join(list1)
    list2.append(list1)
    list1 = []

# num_list = []
# for i in range(0,10000):
#     k = np.random.randint(0,60)
#     num_list.append(k)

# str_list = []
# for i in range(0,10000):
#     #print(list2[i])
#     str_list1 = list(list2[i])

#     alpha = np.random.choice(['A','T','C','G'])
#     str_list1[num_list[i]] = alpha
#     str_list1 = ''.join(str_list1)
#     str_list.append(str_list1)


# str_list = []
# for i in range(0,10000):
#     #print(list2[i])
#     str_list1 = list(list2[i])
#     del str_list1[num_list[i][0]]
#     alpha = np.random.choice(['A','T','C','G'])
#     str_list1.insert(num_list[i][1],alpha)
#     str_list1 = ''.join(str_list1)
#     str_list.append(str_list1)


num_list = []
num_list1 = []
p = [0.001,0.001,0.0005,0.0005,0.997]
for j in range(0,10000):
    for j in range(0,300):
        k = np.random.choice([1,2,3,4,0],p=p)
        num_list1.append(k)
    num_list.append(num_list1)
    num_list1 = []
str_list = []
for i in range(0,10000):
    l = 0
    #print(list2[i])
    str_list1 = list(list2[i])
    for j in range(0,300):
        if num_list[i][j] == 1:
            del str_list1[j+l]
            l = l - 1
        elif num_list[i][j] == 2:
            alpha = np.random.choice(['A','T','C','G'])
            str_list1[j+l] = alpha
        elif num_list[i][j] == 3:
            alpha = np.random.choice(['A','T','C','G'])
            str_list1.insert(j+l,alpha)
            l = l + 1
        elif num_list[i][j] == 4:
            alpha = np.random.choice(['A','T','C','G'])
            str_list1.insert(j+l+1,alpha)
            l = l + 1
    str_list1 = ''.join(str_list1)
    str_list.append(str_list1)

def gailv1():
    return list2,str_list

# count = 0
# for i in range(10):
    # if list2[i] in final_result(list2[i],str_list[i]):
        # Array = list(final_result(list2[i],str_list[i]))
        # All_number = len(Array)
        # count = count+1/All_number
        # print(count)
        # c = count/10


#print(list)
#print(num_list)
#print(list2)
#print(str_list)
#print(c)