import random

# for i in range(10):
#     x = random.random()
#     print(x)

# t = list(range(1, 11))
# for i in range(10):
#     print(random.choice(t))

# if 0 is 0.0:
#     print(True)
# else:
#     print(False)

# print(0 == 0.0)
total = 0
count = 0

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        int(number)
    except ValueError:
        print('Invalid input')
        continue
    total += int(number)
    count += 1

print(total, count, total / count)