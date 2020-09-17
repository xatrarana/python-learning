###make a new list which contains the elements present in the list1 & 2

list1=[1,2,3,4,5]
list2=[4,5,6,7,8,]
list3=[i for i in list1 if i in list2]
print(list3)
