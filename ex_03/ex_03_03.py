score = input("Enter score: ")
try:
    f_score = float(score)
except ValueError:
    print("Bad score")
    quit()

if f_score >= .9:
    print('A')
elif f_score >= .8:
    print('B')
elif f_score >= .7:
    print('C')
elif f_score >= .6:
    print('D')
elif f_score < .6:
    print('F')
