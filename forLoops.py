avengers=['ironman','hulk','thor','cap']

# for avenger in avengers:
#     # code block
#     print(avenger)

# for avenger in avengers[1:3]: # slicing 1(index) inclusive 3(index) exclusive
#     print(avenger)

# for avenger in avengers:
#     if avenger=='hulk':
#         print(f'{avenger} - strongest')
#     else:
#         print(avenger)


for avenger in avengers:
    if avenger=='hulk':
        print(f'{avenger} - strongest')
        break
    else:
        print(avenger)

