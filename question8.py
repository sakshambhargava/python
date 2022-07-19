num = input("Enter the number: ")
def getSum(num):
    sum = 0
    for digit in str(num): 
      sum = sum + int(digit)      
    return sum
print(getSum(num))
