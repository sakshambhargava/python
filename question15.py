numOne = input("Enter the 1st number: ")
numTwo = input("Enter the 2nd number: ")
numThree = input("Enter the 3rd number: ")

if (numOne >= numTwo) and (numOne >= numThree):
   largest = numOne
elif (numTwo >= numOne) and (numTwo >= numThree):
   largest = numTwo
else:
   largest = numThree
   
print("The greatest number from 3 numbers is: ",largest)