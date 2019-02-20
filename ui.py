import sys
import pathlib
import commands

def command(com:str):
    #refine user input
    com=com.strip()
    command=com.partition(' ')[0]
    args=com.partition(' ')[2]
    arguments=[]
    arg=''
    ignore=False
    i=0
    while i<len(args):
        char=args[i]
        if char==' ' and (not ignore):
            arguments.append(arg)
            arg=''
        elif char=='"':
            ignore=not ignore
        else:
            arg+=char
        if i>=len(args)-1:
            arg
            arguments.append(arg)
        i+=1
    #check command existence
    if not command in commands.COMMANDS:
        print('!command not recognised')
        return
    #check command argument specifications
    min_args=commands.COMMANDS[command][1]
    max_args=commands.COMMANDS[command][2]
    if len(arguments)<min_args:
        print('!too few arguments for \''+command+'\' command, should be at least '+str(min_args))
        return
    if len(arguments)>max_args:
        print('!too many arguments for \''+command+'\' command, should be no more than '+str(max_args))
        return
    #reform string
    com=command+'('
    for arg in arguments:
        com+=repr(arg)+','
    if com.endswith(','):
        com=com[0:-1]
    com+=')'
    #attempt execution
    print('|executing \''+com+'\'...\n')
    try:
        commands.COMMANDS[command][0](*arguments)
    except SystemExit:
        raise
    except:
        print(sys.exc_info()[1])
    return

def main():
    print(commands.WELCOME)
    print()
    commands.list_commands()
    print()
    print('|file location defaulting to \''+str(commands.file)+'\'...')
    print()
    while True:
        command(input('command> '))
        print()
    return
main()
