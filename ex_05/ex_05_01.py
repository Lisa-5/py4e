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