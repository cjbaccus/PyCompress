#!/usr/bin/env python

from shutil import copyfile

filename = "core-log-2019"

FH = open(filename, "w")

this = "1212"*1000
that = "1010*"*1000


for n in range(1,100):
	FH.write(this + that)
	FH.write(that + this + ".\n")

FH.close()

for y in range(2,20):
	source = "core-log-2019"
	target = "core-log-2019{}".format(y)
	
	copyfile(source, target)

