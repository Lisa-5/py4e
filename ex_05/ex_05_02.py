largest = None
smallest = None

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break

    try:
        num = int(num)
    except ValueError:
        print('Invalid input')
        continue

    if largest is None:
        largest = num
    elif num > largest:
        largest = num
    # print('largest', largest)

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    # print('smallest', smallest)

print('Maximum is', largest)
print('Minimum is', smallest)
