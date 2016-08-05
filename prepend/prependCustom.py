import fileinput
import sys

print
pre = raw_input("Enter the pre:")
print

print
post = raw_input("Enter the post:")
print

for line in fileinput.input(['./prepend.txt'], inplace = True):
	l = line.strip()  + "%s\n" %(post)
	sys.stdout.write('%s%s' %(pre,l))
