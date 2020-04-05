with open('files/write.txt','w') as write_file:
    write_file.write('lorem ipsum')
    write_file.write('\nlorem ipsum')

with open('files/write.txt','w') as write_file:
    write_file.write('\nlorem ipsum')  # overwrite from begining

with open('files/write.txt','a') as write_file:
    write_file.write('\nlorem ipsum')

quotes=[
    '\ni am iron man',
    '\ni am iron man',
    '\ni am iron man'
]

with open('files/write.txt','a') as write_file:
    write_file.writelines(quotes)

