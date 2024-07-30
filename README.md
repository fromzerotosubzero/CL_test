# File System Analyzer

## About
A command-line tool that analyzes and reports on the file system structure and usage on a Linux system.
The tool uses only Python built-in modules such as os, argparse and stat. Python version is 3.9.5. 

### Usage
```
file_analyser.py [-h] -p PATH [-k KILOBYTES] [-m MEGABYTES] [-g GIGABYTES]

Generate report on file system structure and usage on a Linux system

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  provide path to directory, type [.] for current directory
  -k KILOBYTES, --kilobytes KILOBYTES
                        specify size threshold in Kilobytes (must be integer)
  -m MEGABYTES, --megabytes MEGABYTES
                        specify size threshold in Megabytes (must be integer)
  -g GIGABYTES, --gigabytes GIGABYTES
                        specify size threshold in Gigabytes (must be integer)
```
E.g.:
```
python file_analyser.py -p /mnt/c/Users/user/Pictures -k 500
```

### Report examples
When provided path is faulty:
```
❯ python3 file_analyser.py -p /mnt/c/Users/user/Desktop/cloudlinux_te
Path /mnt/c/Users/user/Pictur is not valid or doesn't exist. Please try again.
```
When there are no files above threshold:
```
❯ python file_analyser.py -p  C:\\Users\user\Desktop\cloudlinux_test\ -k 500

File system structure and usage report:

File type: development
Quantity: 2
Size: 7.91 KB

File type: text
Quantity: 1
Size: 7.91 KB

File type: database
Quantity: 1
Size: 95.91 KB

AHTUNG! It's a world writable file: C:\\Users\user\Desktop\cloudlinux_test\file_analyser.py
AHTUNG! It's a world writable file: C:\\Users\user\Desktop\cloudlinux_test\.vs\VSWorkspaceState.json
AHTUNG! It's a world writable file: C:\\Users\user\Desktop\cloudlinux_test\requirements.txt
AHTUNG! It's a world writable file: C:\\Users\user\Desktop\cloudlinux_test\.vs\slnx.sqlite
```
When there are files above threshold: 
```
❯ python file_analyser.py -p  C:\\Users\user\Desktop\cloudlinux_test\ -k 5

File system structure and usage report:

File type: development
Quantity: 2
Size: 7.91 KB

File type: text
Quantity: 1
Size: 7.91 KB

File type: database
Quantity: 1
Size: 95.91 KB

AHTUNG! It's a world writable file: C:\\Users\user\Desktop\cloudlinux_test\file_analyser.py
AHTUNG! It's a world writable file: C:\\Users\user\Desktop\cloudlinux_test\.vs\VSWorkspaceState.json
AHTUNG! It's a world writable file: C:\\Users\user\Desktop\cloudlinux_test\requirements.txt
AHTUNG! It's a world writable file: C:\\Users\user\Desktop\cloudlinux_test\.vs\slnx.sqlite

File C:\\Users\user\Desktop\cloudlinux_test\file_analyser.py size exceeds threshold value 5.00 KB being 7.83 KB

File C:\\Users\user\Desktop\cloudlinux_test\.vs\slnx.sqlite size exceeds threshold value 5.00 KB being 88.00 KB
```


