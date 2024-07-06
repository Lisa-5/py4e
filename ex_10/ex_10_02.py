fname = input('Enter file: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'

handle = open(fname)

times = dict()

for line in handle:
    line = line.rstrip()
    wds = line.split()

    if line.startswith('From '):
        time = wds[5].split(':')
        hour = time[0]
        times[time[0]] = times.get(time[0], 0) + 1

lst = list()
for k, v in times.items():
    lst.append((k, v))

lst.sort()
for k, v in lst:
    print(k, v)
