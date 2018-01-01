numb=int(input("Enter number: "))
expt=int(input("Enter exponent: "))

result=1
for i in range(1,(expt+1)):
    result=result*numb
print("The result is ",result)

input("Press enter to exit")

