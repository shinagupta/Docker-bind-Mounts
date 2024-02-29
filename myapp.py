def read_servers():
    try:
        with open("servers.txt", "r") as file:
            servers = file.readlines()
            if not servers:
                print("No servers recorded yet.")
            else:
                print("List of Servers:")
                for server in servers:
                    print(server.strip())
    except FileNotFoundError:
        print("No servers recorded yet.")

def create_servers_file():
    with open("servers.txt", "w") as file:
        print("Created an empty servers.txt file.")

def main():
    # Check if servers.txt exists, create if not
    try:
        with open("servers.txt", "r"):
            pass
    except FileNotFoundError:
        create_servers_file()

    print("Options:")
    print("1. Display List of Servers")
    print("2. Quit")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        read_servers()
    elif choice == "2":
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please enter a valid option (1/2).")

if __name__ == "__main__":
    main()


