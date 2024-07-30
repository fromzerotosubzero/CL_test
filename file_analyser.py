import os
import argparse
import stat
import errno

from os.path import getsize, join


'''
File catigorization dictionaries based on https://github.com/jddinneen/file-extension-categoriser
'''
text = ['textFiles', 'doc', 'docx', 'docm', 'odt', 'txt', 'rtf', 'pages', 'pfb', 'mobi', 'chm', 'tex', 'bib', 'dvi', 'abw', 'text', 'epub', 'nfo', 'log', 'log1', 'log2', 'wks', 'wps', 'wpd', 'emlx', 'utf8', 'ichat', 'asc', 'ott', 'fra', 'opf']
image = ['imageFiles', 'img','jpg', 'jpeg', 'png', 'png0', 'ai', 'cr2', 'ico', 'icon', 'jfif', 'tiff', 'tif', 'gif', 'bmp', 'odg', 'djvu', 'odg', 'ai', 'fla', 'pic', 'ps', 'psb', 'svg', 'dds', 'hdr', 'ithmb', 'rds', 'heic', 'aae', 'apalbum', 
         'apfolder', 'xmp', 'dng', 'px', 'catalog', 'ita', 'photoscachefile', 'visual', 'shape', 'appicon', 'icns']
system = ['systemFiles', 'bif','shs', 'ds_store', 'gadget', 'so', 'idx', 'ipmeta', 'sys', 'dll', 'dylib', 'etl', 'regtrans-ms', 'key', 'lock', 'man', 'inf', 'x86', 'dev', 'config', 'cfg', 'cpl', 'cur', 'dmp', 'drv', 'mot', 'ko', 'supported', 
          'pxe', 'cgz', '0', 'file', 'install', 'desktop', 'ttc', 'ttf', 'fnt', 'fon', 'otf', 'download', 'acsm', 'ini', 'opt', 'dat', 'sav', 'save', 'aux', 'raw', 'temp', 'tmp', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'cache', 'ipsw', 
          'stt', 'part', 'appcache', 'sbstore', 'gpd', 'sqm', 'emf', 'jrs', 'pri', 'vcrd', 'mui', 'localstorage', 'localstorage-journal', 'data', 'crash', 'webhistory', 'settingcontent-ms', 'itc', 'atx', 'apversion', 'apmaster', 'apdetected', 
          'pos', 'glk', 'blob', 'cat', 'sns', 'adv', 'asd', 'lrprev', 'csl', 'rdl', 'sthlp', 'tm2', 'mcdb', 'fragment', 'nif', 'blockdata', 'continuousdata', 'upk', 'znb', 'xnb', 'idrc', 'model', 'primitives', 'ovl', 'sid', 'stringtable', 
          'foliage', 'civ4savedgame', 'cgs', 'thewitchersave', 'pssg', 'pac', 'unity3d', 'ifi', 'vmt', 'vtf' ,'pfm', 'deu', 'map', 'simss']
executable = ['executableFiles', 'exe', 'bat', 'dmg', 'msi', 'bin', 'pak', 'app', 'com', 'application']
development = ['devFiles', 'py', 'h', 'm', 'jar', 'cs', 'c', 'c#', 'cpp', 'c++', 'class', 'java', 'php', 'phps', 'php5', 'htm', 'html', 'css', 'xml', '3mf', 'o', 'obj', 'json', 'jsonp', 'blg', 'bbl', 'j', 'jav', 'bash', 'bsh', 'sh', 'rb', 
               'vb', 'vbscript', 'vbs', 'vhd', 'vmwarevm', 'js', 'jsp', 'xhtml','md5', 'nib', 'strings', 'frm', 'myd', 'myi', 'props', 'vcxproj', 'vs', 'lst', 'sol', 'vbox', 'vbox-prev', 'pch', 'pdb', 'lib', 'nas', 'assets', 'sql', 'sqlite-wal', 
               'rss', 'swift', 'xsl', 'manifest', 'up_meta', 'down_meta', 'woff', 'dist', 'sublime-snippet', 'd', 'ashx', 'tpm', 'dsw', 'hpp', 'tga', 'kf', 'rq', 'rdf', 'ttl', 'pyc', 'pyo', 's', 'lua', 'vim', 'p', 'dashtoc', 
               'md', 'mo', 'make', 'cmake', 'makefile', 'options', 'def', 'cc', 'f90', 'dcp', 'cxx', 'seto', 'f', 'simt']
spreadsheet = ['spreadsheetFiles', 'csv', 'odf', 'ods', 'xlr', 'xls', 'xlsx', 'numbers', 'xlk']
archive = ['archiveFiles', 'zip', 'gz', 'rar', 'cab', 'iso', 'tar', 'lzma', 'bz2', 'pkg', 'xz', '7z', 'vdi', 'ova', 'rpm', 'z', 'tgz', 'deb', 'vcd', 'ost', 'vmdk', '001', '002', '003', '004', '005', '006', '007', '008', '009', 'arj', 'package', 'ims']
audio = ['audioFiles', 'mp3', 'm3u', 'm4a', 'wav', 'ogg', 'flac', 'midi', 'oct', 'aac', 'aiff', 'aif', 'wma', 'pcm', 'cda', 'mid', 'mpa', 'ens', 'adg', 'dmpatch', 'sngw', 'seq', 'wem', 'mtp', 'l6t', 'lng', 'adx', 'link']
database = ['databaseFiles', 'accdb', 'accde', 'mdb', 'mde', 'odb', 'db', 'gdbtable', 'gdbtablx', 'gdbindexes', 'sqlite', 'enz', 'enl', 'sdf', 'hdb', 'cdb', 'gdb', 'cif', 'xyz', 'mat', 'bgl', 'r', 'exp', 'asy', 'info', 'meta', 'adf', 'appinfo', 'xg0', 'yg0']
presentation = ['presentationFiles', 'ppt', 'pptx', 'pps', 'ppsx', 'odp', 'key']
video = ['videoFiles', 'mpg', 'mpeg', 'avi', 'mp4', 'flv', 'h264', 'mov', 'mk4', 'swf', 'wmv', 'mkv', 'plist', 'm4v', 'trec', '3g2', '3gp', 'rm', 'vob']
categories = {'text': text, 'image': image, 'development': development, 'spreadsheet': spreadsheet, 'system': system, 'executable': executable, 'archive': archive, 'audio': audio, 'database': database, 'presentation': presentation, 'video': video}


# sorting files by category based on their extensions
def file_groups(path):
    allgroups =  {}
    for root, dirs, files in os.walk(path):
        for name in files:
            full_path = join(root, name)
            extension = os.path.splitext(full_path)[1][1:]
            for key, value in categories.items():
                if extension in value:
                    allgroups.setdefault(key,[]).append(full_path)
                    break
    return allgroups


# auxilary function to print human-readable size format
def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f'{size:.2f} {unit}'


# checking file permissions and highlighting most peculiar ones
def permissions(groups):
    for k, v in groups.items():
        for full_path in v:
            mode = os.stat(full_path).st_mode
            if mode & stat.S_IWOTH:
                print('AHTUNG! It\'s a world writable file:', full_path) 
            elif mode & stat.S_ISUID:
                print('Special permission for user access level:', full_path)
            elif mode & stat.S_ISGID:
                print('Special permission for group access level:', full_path)
            elif mode & stat.S_ISVTX:
                print('Here\'s a sticky bit:', full_path)


# calculating quantity and size of files in each category 
def group_size(groups):
    size = 0
    count = 0
    for k, v in groups.items():
        size += sum(getsize(full_path) for full_path in v)
        form_size = format_size(size)
        count = len(v)   
        print(f'File type: {k}\nQuantity: {count}\nSize: {form_size}\n')


def main():
    # adding arguments
    parser = argparse.ArgumentParser(description='Generate report on file system structure and usage on a Linux system')
    parser.add_argument('-p', '--path', required=True, help='provide path to directory, type [.] for current directory')
    parser.add_argument('-k', '--kilobytes', type=int, required=False, help='specify size threshold in Kilobytes (must be integer)')
    parser.add_argument('-m', '--megabytes', type=int, required=False, help='specify size threshold in Megabytes (must be integer)')
    parser.add_argument('-g', '--gigabytes', type=int, required=False, help='specify size threshold in Gigabytes (must be integer)')
    args = parser.parse_args()

    # size threshold parameters
    kb = int(args.kilobytes or 0)
    mb = int(args.megabytes or 0)
    gb = int(args.gigabytes or 0)
    min_size = 0
    if kb > 0:
        min_size = kb * 1024
    if mb > 0:
        min_size = mb * 1024 * 1024
    if gb > 0:
        min_size = gb * 1024 * 1024 * 1024

    # path paramether error handling snippet
    path = args.path
    if not os.path.exists(path):
        print(f'Path {path} is not valid or doesn\'t exist. Please try again.')
    try:
        # starting analisys
        print('\nFile system structure and usage report:\n')

        groups = file_groups(path)
        group_size(groups)
        permissions(groups)
        
        # checking if file size exceeds threshold parameter
        if not min_size:
            pass
        else:
            for k, v in groups.items():
                for full_path in v:
                    file_size = getsize(full_path)
                    if file_size > min_size:
                        print(f'\nFile {full_path} size exceeds threshold value {format_size(min_size)} being {format_size(file_size)}')

    except OSError:
        print(f'Can\'t access directory {path}. Please check permisions.')

      
if __name__ == '__main__':
    main()