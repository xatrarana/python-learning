#########To find the palindrome of the string
org_h=input("Enter the palindrome word")
reverstring=org_h[::-1]
if org_h==reverstring:
    print("the given word is palindrome")

else:
    print("not a palindrome")
