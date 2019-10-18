command = ""
started = False
while True:
    command = input("> ").lower()
    if command.lower() == "start":
        if started:
            print("Car already started")
        else:
            started=True
            print("Car  has been started.....")
    elif command.lower() == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
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
