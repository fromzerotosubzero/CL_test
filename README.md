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
python file_analyser.py -p /home/user/Pictures -k 500
```

### Report examples
When provided path is faulty:
```
❯ python3 file_analyser.py -p home/user/Desktop/cloudlinux_te
Path home/user/Desktop/cloudlinux_te is not valid or doesn't exist. Please try again.
```
When there are no files above threshold:
```
❯ python file_analyser.py -p /home/user/CL_test -k 500

File system structure and usage report:

File type: development
Quantity: 2
Size: 10.52 KB

File type: system
Quantity: 1
Size: 11.73 KB

AHTUNG! It's a world writable file: /home/user/CL_test/README.md

```
When there are files above threshold: 
```
❯ python file_analyser.py -p /home/user/CL_test -k 5

File system structure and usage report:

File type: development
Quantity: 2
Size: 10.52 KB

File type: system
Quantity: 1
Size: 11.73 KB

AHTUNG! It's a world writable file: /home/user/CL_test/README.md

File /home/user/CL_test/file_analyser.py size exceeds threshold value 5.00 KB being 7.71 KB
```

