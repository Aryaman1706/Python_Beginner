# ninja_belts={"crystal":"red","ryu":"black"}
# print(ninja_belts)

# print(ninja_belts['ryu'])

# print('yoshi' in ninja_belts)

# print('ryu' in ninja_belts)

# print(ninja_belts.keys())

# print(ninja_belts.values())

# print(list(ninja_belts.keys()))

# print(list(ninja_belts.values()))

# vals=list(ninja_belts.values())

# print(vals.count('black'))

# print(vals.count('blue'))

# ninja_belts['yoshi']='red'

# print(ninja_belts)


# person=dict(name="shaun", age=27, height="6ft")

# print(person)


def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'i am {key} and i am a {val} belt')

ninja_belts={}

while True:
    ninja_name=input('enter a ninja name: ')
    ninja_belt=input('enter a belt colour: ')

    ninja_belts[ninja_name]=ninja_belt

    another=input('add another? (y/n) ')
    if another=='y':
        continue
    else:
        break
ninja_intro(ninja_belts)






