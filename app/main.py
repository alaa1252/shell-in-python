import sys
import os
def main():
    while(True):
        sys.stdout.write("$ ")

        command = input()

        if(command == 'exit 0'):
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

        ex = parts[0]

        if len(parts) > 0 and ex != None:
            os.system(parts[0])
        else:
            print(f"{parts[0]}: command not found")
            continue

        print(f"{command}: command not found")

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
    paths = os.environ.get("PATH", "").split(os.pathsep)
    for path in paths:
        executable = os.path.join(path, command)
        if os.path.isfile(executable) and os.access(executable, os.X_OK):
            return executable
    return None


if __name__ == "__main__":
    main()
