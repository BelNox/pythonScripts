import sys
import fileinput

listNumbers = []

while True:
    listNumbers.append(raw_input("Please enter the number:  "))
    iDoNext = raw_input("Do you want to add another numer? (n):  ")
    if iDoNext == "n":
        break

iNumTotal = 0
for idx in listNumbers:
    iNumTotal += int(idx)

print "%.2f" % (iNumTotal/float(len(listNumbers)))
