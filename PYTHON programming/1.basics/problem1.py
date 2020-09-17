##find the sum of integers from 1 to n without using the loop:;/with loop::


#with out loop
n=int(input("Enter the value of n"))
print(sum(list(range(1,n+1))))

#with loop::

print("with loop")
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)