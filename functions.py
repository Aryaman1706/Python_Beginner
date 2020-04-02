# def greet(name, time):
#     # code block
#     print(f'Good {time} {name}')

# name=input('enter your name: ')
# time=input('enter the time of day: ')
# greet(name,time)

# def greet(name='aryaman', time='morning'):
#     # code block
#     print(f'Good {time} {name}')

# name=input('enter your name: ')
# time=input('enter the time of day: ')
# greet(name)

def area(radius):
    return(3.142*radius*radius)

def vol(area,length):
    print(area*length)

radius=int(input('enter a radius: '))
length=int(input('enter the length: '))

# area_calc=area(radius)
# vol(area_calc,length)

vol(area(radius),length)