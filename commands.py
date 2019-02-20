import pathlib

def close():
    raise SystemExit

def navigate(path=None):
    global file, DEFAULT_PATH
    #prcess user input
    if path==None:
        temp=DEFAULT_PATH
        print('|new search started')
    else:
        temp=file.joinpath(path)
    temp=temp.resolve()
    #report to user
    if not temp.exists():
        print('!cannot find '+str(temp)+' path')
        print('|reverting to previous location \''+str(file)+'\'...')
    elif temp.is_file():
        print('|'+repr(temp.name)+' file found')
        file=temp
        print('|proceeding to count words...')
        count()
    else:
        print('|\''+str(temp)+'\' path found')
        file=temp
    return

def list_files():
    global file
    for item in file.iterdir():
        print(item.name)
    return

def count():
    global file, DEFAULT_PATH, SUPPORTED_FILES
    if not file.suffix in SUPPORTED_FILES:
        print('!\''+file.suffix+'\' file type not supported')
    else:
        SUPPORTED_FILES[file.suffix][0]()
    file=file.joinpath('..').resolve()
    print('|returning to upper file location \''+str(file)+'\' ...')
    return

def txt_count():
    global file
    text=file.read_text()
    words=text.split()
    print('|\''+file.name+'\' contains '+str(len(words))+' words')
    return

def list_commands():
    global COMMANDS
    for command in COMMANDS:
        line=command+' : '+COMMANDS[command][3]
        print(line)
    return

def list_files():
    global SUPPORTED_FILES
    for file in SUPPORTED_FILES:
        line = file+' : '+SUPPORTED_FILES[file][1]
        print(line)
    return

WELCOME="Welcome to the Mader word counter:\na free, work in progress word counter\nfor files on your computer"
SUPPORTED_FILES={'.txt':(txt_count,'plain text')}
COMMANDS={'close':(close,0,0,'close this program'),
          'sup':(list_files,0,0,'view list of supported file types'),
          'coms':(list_commands,0,0,'view this list of commands'),
          'nav':(navigate,0,1,'navigate to files that are to be word counted\n      use \'..\' to represent the above location\n      use \'/\' to separate folder names\n      encase spaces in \'\"\"\'(double quotation marks) to use spaces in file names'),
          'list':(list_files,0,0,'list files in current folder')}
DEFAULT_PATH=pathlib.Path().home()
file=DEFAULT_PATH
