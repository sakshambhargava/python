numOne = int(input("Enter the 1st number: "))
numTwo = int(input("Enter the 2nd number: "))

x = lambda a, b: a + b
print("The sum of",numOne,"and",numTwo,"is:",x(numOne, numTwo))