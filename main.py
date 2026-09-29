def main():

    PrintMainMenu()
    TakeUserInput()


def PrintMainMenu():
    print(f"\nWelcome to chad! You're using version TODO.\n")

def TakeUserInput():
    allowedCommands = ['m', 'q']

    print("Command (m for help): ", end='')
    userInput = input()

    if (len(userInput) != 1 or userInput not in allowedCommands):
        print(f"Invalid command. Please use m for help.")
        TakeUserInput()

    HandleCommand(userInput)

def HandleCommand(command):
    match command:
        case 'm':
            HandleMenu()
        case 'q':
            HandleQuit()

    TakeUserInput()

def HandleMenu():
    #TODO
    print()

def HandleQuit():
    quit()

if __name__ == "__main__":
    main()