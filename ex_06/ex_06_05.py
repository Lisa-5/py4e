str = 'X-DSPAM-Confidence: 0.8475 '

ipos = str.find(':')
# print(ipos)
substr = str[ipos + 1:].strip()
# print(repr(substr))
value = float(substr)
print(value)
