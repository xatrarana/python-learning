def update(x):                                          #####defining the function
    x=10
    print("inside the function: "+str(x))

x=5
print("outside function:"+str(x))
update(x)                                                #####calling  the function
print("after the function, the value of x:"+str(x))