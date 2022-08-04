num = int(input("Enter the number: "))
def getSum(num):
    sum = 0
    for digit in range(1, num+1): 
      sum = sum + int(digit)  
    return sum
print(getSum(num))
