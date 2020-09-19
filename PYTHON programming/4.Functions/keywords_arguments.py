####solve the qudratic equation ax**2+bx+c=0
import math
def  qudratic(a,b,c):          ##you can set the default arguments
    pass
    ##x1=(-b+sqrt(b*b-4*a*c))/2*a
    ##x2=(-b-sqrt(b*b-4*a*c))/2*a
    determinant=math.sqrt(b*b-4*a*c)
    x1=(-b+determinant)/(2*a)
    x2 = (-b -determinant) / (2 * a)
    return x1,x2
root1,root2=qudratic(a=1,b=5,c=6)
print("x1:"+str(root1))
print("x1:"+str(root2))