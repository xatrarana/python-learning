## to generate the list of squre::

##square=[1,4,9,16,25,36]
##square=[#expression,#for_loop #condition]
square=[i*i for i in range(1,11)]
print(square)





squar=[i*i for i in range(1,11) if i%2==0] ##if the condition is true then it will print  in the list.
print(squar)

squares=[i*i for i in range(1,11) if i%2!=0]
print(squares)

