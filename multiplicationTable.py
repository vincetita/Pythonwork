#parsing string input value to int
number=int(input("Enter number: "))

for i in range(1, (number+1)):
    print("==========", "\n")
    for j in range(1,11):
        print(i, "x", j, "=", i*j)
            
       
