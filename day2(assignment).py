"""Write a program that takes 2 inputs from the user in variable a and b. Based on these inputs find the output of following expressions:
1. Floor Division
2. a power b
3. Find out whether two variables have equal value or not - if yes then print True if they are not equal then print False"""

#CODE : 
a=int(input("Enter Number 1 : "))
b=int(input("Enter Number 2 : "))

print("\nFloor Division : ",a//b)
print("A power b : ",a**b)
print("Two numbers are equal : ",end="")
print(True if (a==b) else False)

"""
Sample Input and Output :
Enter Number 1 : 20
Enter Number 2 : 2

Floor Division :  10
A power b :  400
Two numbers are equal : False"""
