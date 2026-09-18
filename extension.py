def main():
    state = "idle"

    print("Character State Machine")
    print("States: idle, walking, attacking, resting\n")

    while True:
        if state == "idle":
            print("\nThe character is standing idle.")
            while True:
                event = input("Event (move / enemy_nearby): ").lower()
                if event == "move":
                    state = "walking"
                    break
                elif event == "enemy_nearby":
                    state = "attacking"
                    break
                else:
                    print("Invalid event, try again.")

        elif state == "walking":
            print("\nThe character is walking.")
            while True:
                event = input("Event (stop / enemy_nearby): ").lower()
                if event == "stop":
                    state = "idle"
                    break
                elif event == "enemy_nearby":
                    state = "attacking"
                    break
                else:
                    print("Invalid event, try again.")

        elif state == "attacking":
            print("\nThe character is attacking!")
            while True:
                event = input("Event (enemy_defeated / low_energy): ").lower()
                if event == "enemy_defeated":
                    state = "idle"
                    break
                elif event == "low_energy":
                    state = "resting"
                    break
                else:
                    print("Invalid event, try again.")

        elif state == "resting":
            print("\nThe character is resting.")
            while True:
                event = input("Event (energy_restored / enemy_nearby): ").lower()
                if event == "energy_restored":
                    state = "idle"
                    break
                elif event == "enemy_nearby":
                    state = "attacking"
                    break
                else:
                    print("Invalid event, try again.")

if __name__ == "__main__":
    main()