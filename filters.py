grades=['A','B','F','C','F','A']
filtered_grates=[]

def remove_Fs(grade):
    return grade != 'F'
# using for loop

# for grade in grades:
#     if grade!='F':
#         filtered_grates.append(grade)
# print(filtered_grates)

# comprehension

# print([grade for grade in grades if grade!='F'])

# using filter methord    

print(list(filter(remove_Fs,grades)))