name = input("Enter file:")
count = 0
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith("From:"):
        count += 1
        line = line.rstrip()
        words = line.split()
        email = words[1]
        if email not in counts:
            counts[email] = 1
        else:
            counts[email] = counts[email] + 1
bigemail = None
bigcount = None
for email, count in counts.items():
    if bigcount is None or count > bigcount:
        bigemail = email
        bigcount = count
print(bigemail, bigcount)

