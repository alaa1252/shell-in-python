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

        print(f"{command}: command not found")


if __name__ == "__main__":
    main()
