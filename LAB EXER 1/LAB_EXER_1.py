incident = [
    ["INC1392939", "BOT-Inventory", "Failed to generate the daily report"],
    ["INC1392940", "BOT-Email", "Failed to send the scheduled notification"],
    ["INC1392941", "BOT-DataSync", "Encountered an error during data transfer"],
    ["INC1392942", "BOT-Invoice", "Failed to process an invoice"],
    ["INC1392943", "BOT-Report", "Failed to generate the weekly report"],
    ["INC1392944", "BOT-FileTransfer", "Failed to upload the required file"],
    ["INC1392945", "BOT-DataEntry", "Encountered an error while entering records"],
    ["INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"],
    ["INC1392947", "BOT-Validation", "Failed to validate the submitted records"],
    ["INC1392948", "BOT-Notification", "Failed to send the system alert"],
]

while True:
    print("\n1. Add  \n2. Display  \n3. Search  \n4. Remove  \n5. Count  \n6. Exit")
    choice = input("Choice: ")

    if choice == "1":
        new_id = input("Incident ID: ")
        bot = input("Bot: ")
        desc = input("Short Description: ")
        incident.append([new_id, bot, desc])
        print("Ticket added.")

    elif choice == "2":
        if not incident:
            print("No active incident tickets.")
        else:
            for t in incident:
                print(t[0], "|", t[1], "|", t[2])

    elif choice == "3":
        search_id = input("Incident ID: ")
        for t in incident:
            if t[0] == search_id:
                print("Found:", t[0], "|", t[1], "|", t[2])
                break
        else:
            print("Not found.")

    elif choice == "4":
        remove_id = input("Incident ID to remove: ")
        for i in range(len(incident)):
            if incident[i][0] == remove_id:
                incident.pop(i)
                print("Ticket removed.")
                break
        else:
            print("Not found.")

    elif choice == "5":
        print("Active tickets:", len(incident))

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice, please try again.")