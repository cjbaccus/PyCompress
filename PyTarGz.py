import os
import glob
import tarfile
from time import sleep
from shutil import copyfile

# ensure you are in correct directory
os.chdir("/home/cbaccus/Code/python/PyCompress/")


files = glob.glob("*core*[!.gz]")

#check files 
print(files)

# create TEMP directory
os.mkdir("TEMP")

#Safety check...you can kill the script if it looks like this is wrong
sleep(10)

for n in files:
	source = "/home/cbaccus/Code/python/PyCompress/{}".format(n)
	target = "/home/cbaccus/Code/python/PyCompress/TEMP/{}".format(n) + "-bk"
	copyfile(source, target)
	new_name = n + ".gz"
	tfile = tarfile.open(new_name, "w:gz")
	tfile.add(n)
	tfile.close()
	os.remove(n)

gzfiles = glob.glob("*core*.gz")

print(gzfiles)
print("All  files successfully gzipped")
 


