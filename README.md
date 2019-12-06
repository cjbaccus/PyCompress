# PyCompress
Python script to cp a group of files in a TEMP dir, and then tar-gz each and remove the original large files.

## Usage

1. Edit the file PyTarGz.py and change the following variables:
     * *os.chdir(<path of files>)* this is the main directory where logs or whatever reside that need compression.
     * *file = glob.glob("<pattern>")* change the <pattern> section (hint: "*nameof file[!.gz]" would do all files with matching names but those ending in .gz)
     * *source = "<path>"* (this is the path of the source files up to the {})
     * *target = "<path>"* (this isthe target files into the newly created TEMP directory (for backups))
2. Then just execute with sudo python PyTarGz.py
3. Enjoy cleaned directory
4. (if all is well, you can now delete the TEMP directory)

## Bonus
The CreateDummyLog.py file is executed to literally create about 20 log files that are filled with bogus data...but about 1.7M and will compress to about 3.2k.  enjoy!

## future plans
probably going to make this into a class with several functions, that can then just be called in an interactive shell (easier)

maybe even pass variables like path in argv... we will see
