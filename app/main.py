import sys
import shutil
import subprocess

def main():
    while(True):
        sys.stdout.write("$ ")

        command = input()

        if(command == 'exit'):
            break

        parts = command.split()

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

        my_execute(parts)

def my_type(command):
    defined = ['exit', 'echo', 'type']
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
    exe = find_executable(parts[0])
    if exe:
        try:
            subprocess.run(parts, shell=True)
        except Exception as err:
            print(f" Erorr excuting {parts}: {err}")
    else:
        print(f"{parts[0]}: command not found")

if __name__ == "__main__":
    main()
