i=1
while(i<10):
    print(i)
    i=i+1
    if(i==5):
      
        break
    
print("++++++++++++++++++++++++++++++++++++")

j=1
while(j==1):
   name= input("Enter name: ")
   if(name=="quit"):
        break
print("++++++++++++++++++++++++++++++++++++")

k=1
while(k<=100):
    k=k+1
    if(k<=50):
        continue
    print(i)
print("++++++++++++++++++++++++++++++++++++")

password="vince"
for i in range(3):
    pwd=input("Enter password: ")
    j=3   #3 attempts more
    if(pwd==password):
        print("Welcome")
        break
    else:
        print("Wrong password. Attempts left: ",  j-i)