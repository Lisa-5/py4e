# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"

# fh = open(fname)
# email_lst = list()

# for line in fh:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     email_lst.append(words[1])
#     print(words[1])

# print(f'There were {len(email_lst)} lines in the file with From as the first word')

fruit = 'Banana'
fruit[0] = 'b'
print(fruit)