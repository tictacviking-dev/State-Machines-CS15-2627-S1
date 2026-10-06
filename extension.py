state = "idle"
while True:
    if state == "idle":
        print("Character is idle")
        print("Type walk or jump:")
        action = input()
        if action == "walk":
            state = "walking"
        elif action == "jump":
            state = "jumping"
        else:
            print("Fake action.")
    elif state == "walking":
        print("Character is walking")
        print("Type run, jump, or stop:")
        action = input()
        if action == "run":
            state = "running"
        elif action == "jump":
            state = "jumping"
        elif action == "stop":
            state = "idle"
        else:
            print("Invalid action")
    elif state == "running":
        print("Character is running")
        print("Type slow or jump:")
        action = input()
        if action == "slow":
            state = "walking"
        elif action == "jump":
            state = "jumping"
        else:
            print("Fake action")
    elif state == "jumping":
        print("Character is jumping")
        print("Type land or run:")
        action = input()
        if action == "land":
            state = "idle"
        elif action == "run":
            state = "running"
        else:
            print("Fake action")