import re

hand = open('regex_sum_2040202.txt')
total = list()

for line in hand:
    line = line.rstrip()
    targets = re.findall('[0-9]+', line)
    if len(targets) > 0:
        for i in targets:
            i = int(i)
            total.append(i)

print(sum(total))

