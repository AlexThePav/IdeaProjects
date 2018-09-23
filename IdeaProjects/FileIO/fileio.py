jabber = open('/home/pav/Desktop/sample.txt', 'r')

for line in jabber:
    print(line.strip("\n"))

jabber.close()