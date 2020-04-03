# name="ary"
# age=20
# nums=[1,2,3]
# print(type(name))
# print(type(nums))
# print(type(age))

# print(name.upper())

# class Planet:
#     def __init__(self):  #constructor
#         self.name="hoth"
#         self.radius=20000
#         self.gravity=5.5
#         self.system="hoth system"

#     def orbit(self):
#         return f'{self.name} is orbiting in the {self.system}'

# hoth= Planet()
# print(f'name is: {hoth.name}')
# print(f'radius is: {hoth.radius}')
# print(hoth.orbit())


class Planet:
    def __init__(self,name,radius,gravity,system):  #constructor
        self.name=name
        self.radius=radius
        self.gravity=gravity
        self.system=system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

planetX=Planet("X",2000,9.8,"X system")

print(f'name is {planetX.name}')
print(f'gravity is {planetX.gravity}')
print(f'system is {planetX.system}')
print(planetX.orbit())