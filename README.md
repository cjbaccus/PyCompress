# PyCompress
Python script to cp a group of files in a TEMP dir, and then tar-gz each and remove the original large files.

## Usage

1. Edit the file PyTarGz.py and change the following variables:
 a. os.chdir(<path of files>) this is the main directory where logs or whatever reside that need compression.
 b. file = glob.glob("<pattern>") change the <pattern> section (hint: "*nameof file[!.gz]" would do all files with matching names but those endingin .gz)
 c. source = "<path>" (this is the path of the source files up to the {})
 d. target = "<path>" (this isthe target files into the newly created TEMP directory (for backups))
2. then just execute with sudo python PyTarGz.py
3. Enjoy cleaned directory
4. (if all is well, you can now delete the TEMP directory)

## future plans
probably going to make this into a class with several functions, that can then just be called in an interactive shell (easier)

maybe even pass variables like path in argv... we will see
