hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
float_hours = float(hours)
float_rate = float(rate)
pay = float_hours * float_rate

if float_hours > 40:
    # print("overtime")
    reg_pay = 40 * float_rate
    ot_pay = (float_hours - 40) * ((float_rate) * 1.5)
    pay = reg_pay + ot_pay
else:
    # print('regular')
    pay = float_hours * float_rate

print("Pay:", pay)