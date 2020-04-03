class Planet:
    
    shape='round'
    
    def __init__(self,name,radius,gravity,system):  #constructor
        self.name=name
        self.radius=radius
        self.gravity=gravity
        self.system=system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def commons(cls): 
        return f'All planets are {cls.shape} because of gravity'

    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'Planets spins at {speed}'

planetX=Planet("X",2000,9.8,"X system")

print(f'name is {planetX.name}')
print(f'gravity is {planetX.gravity}')
print(f'system is {planetX.system}')
print(planetX.orbit())
print(planetX.shape)

print(Planet.commons())
print(planetX.commons())

print(Planet.spin())
print(planetX.spin())

print(Planet.spin('a very high speed'))





