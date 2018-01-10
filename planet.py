class Planet:
    shape="round"
    
    def __init__(self,name, radius, gravity, system):
        self.name=name
        self.radius=radius
        self.gravity=gravity
        self.system=system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'
    @classmethod
    def commons(cls):
        return f"All planets are {cls.shape} because of gravity"

hoth=Planet("Hoth", 500000,5.5, "Hoth system")
print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'Gravity is: {hoth.gravity}')
print(f'System is: {hoth.system}')

print("======================================")

naboo=Planet("Naboo", 300000,3.5, "Naboo system")
print(f'Name is: {naboo.name}')
print(f'Radius is: {naboo.radius}')
print(f'Gravity is: {naboo.gravity}')
print(f'System is: {naboo.system}')
    
print(Planet.shape)
print(hoth.shape)
print(Planet.commons())
print(hoth.commons())



