# ipsum_file=open('files/ipsum.txt')

# # methord 1
# for line in ipsum_file:
#     # print(line)
#     print(line.rstrip())

# ipsum_file.seek(0)

# # methord 2
# lines=ipsum_file.readlines()
# print(lines)

# # methord 3
# ipsum_file.seek(5)  #start from 5th char
# file_text=ipsum_file.read(100)  # read 100 chars
# print(file_text)

# ipsum_file.close()


# another methord to open

def seq_filter(line):
    return '>' not in line

with open('files/dna.txt') as dna_file:
     # only open when idented
     lines=dna_file.readlines()
     print(list(filter(seq_filter,lines)))

# file is closed if not idented