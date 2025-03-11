import sys


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
                print(type(parts[1]))
            else:
                print(f"{parts[0]}: command not found")
            continue

        print(f"{command}: command not found")

def type(command):
    defined = ['exit', 'echo', 'type']
    if command in defined:
        return command + ' is a shell builtin'
    else:
        return command + ': not found' 
    

if __name__ == "__main__":
    main()
