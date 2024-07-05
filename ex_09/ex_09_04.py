name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

emails = dict()

for line in handle:
    line = line.rstrip()
    wds = line.split()
    
    if line.startswith('From '):
            emails[wds[1]] = emails.get(wds[1], 0) + 1

count = None
email = None

for key,value in emails.items():
     if count is None or value > count:
          count = value
          email = key

print(email, count)