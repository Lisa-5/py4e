fname = input('Enter file: ')
if len(fname) < 1:
    fname = 'clown.txt'

fhand = open(fname)

many = dict()

for line in fhand:
    line = line.rstrip()
    wds = line.split()

    for w in wds:
        many[w] = many.get(w, 0) + 1

# find the word with the largest count
largest = None
wd = None

for key,value in many.items():
    if largest is None or value > largest:
        largest = value
        wd = key

print(wd, largest)