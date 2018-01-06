radius=int(input("Enter radius: "))
length=int(input("Enter length: "))

def area(radius):
        return 3.142*radius**2
area_cal=area(radius)

def volume(area, length):
        print(area*length)


volume(area(radius), length)





        
        
