num = int(input("Enter any number: "))
if(num == 0 or num == 1):
    print(num,"Number is neither prime nor composite")
elif num>1 :
    for i in range(2,num):
        if(num%i == 0):
            print(num,"is not prime but composite number")
            break
    else:
        print(num,"number is prime but not composite number")

if (num%2 == 0):
    print(num,"is an even number")
else:
    print(num,"is an odd number")