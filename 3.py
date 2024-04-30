list1=["hello","take"]
list2=["dear","sir"]
my_list=[]
for i in range(len(list1)):
    for j in range(len(list2)):
        my_list.append(list1[i]+" "+list2[j])
print(my_list)