command = ""
while True:
    command = input("> ").lower()
    if command.lower() == "start":
        print("Car  has been started.....")
    elif command.lower() == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
start - start car
stop - stop car
quite - to end the program
        """)
    elif command == "quit":
        break
    else:
        print("invalid command")