command = ""
started = False
while True:
    command = input("Command > ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car already stopped.")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit the program
        """)
    elif command == "quit":
        print("Quitted")
        break
    else:
        print("Sorry, I don't understand")

