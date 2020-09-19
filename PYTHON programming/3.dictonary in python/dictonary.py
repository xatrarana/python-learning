details={"name":"chhatra","age":20,"contact":9844792560}
print(details)


##to get the age

print(details["age"])
print(details["contact"])

###print the key that is not in the dictonary
#it gives the key valuse errror


details["bloodgroup"]="A positive" ### to add the value in the in the dictonary
print(details)



#### to change the value in the dictonary

details["name"]="blackgemini"
print(details)

## method by ,get method

print(details.get("bloodgroup"))  ###same as  fetching the value using squre braces..


##alternative
 ##way tho create the dictonary
##squares={1:1,2:4,3:9,4:16}
squares=dict([(1,1),(2,4),(3,9),(4,16)])  ##  dict(list(tuple paris))
print(squares)
