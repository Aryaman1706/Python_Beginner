# from classes import Planet

# planetX=Planet("X",2000,9.8,"X system")
# print(f'name is {planetX.name}')
# print(f'gravity is {planetX.gravity}')
# print(f'system is {planetX.system}')


from space.planet import Planet
from space.calc import planet_mass,planet_vol


planetX=Planet("X",2000,9.8,"X system")

planetX_mass=planet_mass(planetX.gravity,planetX.radius)
planetX_vol=planet_vol(planetX.radius)

print(f'name is {planetX.name}')
print(f'mass is {planetX_mass}')
print(f'vol is {planetX_vol}')



