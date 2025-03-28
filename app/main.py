import sys
import shutil
import subprocess
import os
import shlex

def main():
    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()

        if(command == 'exit 0'):
            break

        parts = shlex.split(command)

        if len(parts) > 0 and parts[0] == 'echo':
            if len(parts) > 1:
                print(" ".join(parts[1:]))
            else:
                print(" ")
            continue

        if len(parts) > 0 and parts[0] == 'type':
            if len(parts) > 1:
                print(my_type(parts[1]))
            else:
                print(f"{parts[0]}: command not found")
            continue

        if len(parts) > 0 and parts[0] == 'pwd':
            print(os.getcwd())
            continue

        if len(parts) > 0 and parts[0] == 'cd':
            my_cd(parts)
            continue

        my_execute(parts)

def my_type(command):
    defined = ['exit', 'echo', 'type', 'pwd']
    path = find_executable(command)
    if command in defined:
        return command + ' is a shell builtin'
    elif path:
        return command + ' is ' + path
    else:
        return command + ': not found' 
    

def find_executable(command):
    if shutil.which(command):
        return shutil.which(command)
    extensions = ['.exe', '.cmd', '.bat']
    for ex in extensions:
        if shutil.which(command + ex):
            return shutil.which(command + ex)

    return None    

def my_execute(parts):
    if not parts:
        return
    
    prog_name = parts[0]
    exe = find_executable(prog_name)
    if exe:
        try:
            subprocess.run([prog_name] + parts[1:], env=None, check=False)
        except Exception as err:
            print(f" Erorr excuting {prog_name}: {err}")
    else:
        print(f"{prog_name}: command not found")

def my_cd(command):
    if len(command) < 2 or command[1] == '~':
        home = os.path.expanduser("~")
        os.chdir(home)
        return 
    path = command[1]
    if(os.path.exists(path) and os.path.isdir(path)):
        os.chdir(path)
    else:
        print('cd: ' + path + ': No such file or directory')       

if __name__ == "__main__":
    main()
