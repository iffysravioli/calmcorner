def main():
    entries = []
    # Main Menu
    while True: 
        print("Calm Corner")
        print("1. New entry")
        print("2. Save entry")
        print("3. Exit Calm Corner")
        # Main Menu Selection 
        selection = input("Please enter a selection:")
        # New Entry Selection
        if selection == "1":
            title = input("Please enter your title: ")
            body = input("Enter your entry: ")
            entry = {"title": title, "entry" : body}
            entries.append(entry)
            print("Thanks for sharing! Have a great day.")
        # Save the entries to a file
        elif selection == "2":
            filename = input("Enter the entry name: ")
            with open(filename, "w") as f: 
                for entry in entries: 
                    f.write(entry["title"] +"\n")
                    f.write(entry["entry"] +"\n")
            print("Entries saved!")
        # Exit app
        elif selection == "3":
            break 
        else:
            print("Please select only one number. 1, 2, or 3")
