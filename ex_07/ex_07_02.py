fname = input('Enter the file name: ')
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
count = 0
total_value = 0

for lx in fh:
    if lx.startswith('X-DSPAM-Confidence:'):
        ipos = lx.find(':')
        substr = lx[ipos + 1:].rstrip()
        value = float(substr)
        total_value += value
        count += 1

print(f'Average spam confidence: {total_value / count}')
