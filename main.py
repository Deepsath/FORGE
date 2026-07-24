import os
import json




# ---------------- FILE NAMES ----------------


# ---------------- GLOBAL LISTS ----------------
goals = []
completed_goals = []
DATABASE_FILE = "forge.json"


# ---------------- CLEAR SCREEN ----------------
# Clears the terminal screen.
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ---------------- WELCOME SCREEN ----------------
# Displays the welcome page.
def welcome():

    clear_screen()

    print()
    print("╔════════════════════════════════════════════╗")
    print("║                                            ║")
    print("║                 ⚒ FORGE                    ║")
    print("║                                            ║")
    print("║        Build Yourself. Every Day.          ║")
    print("║                                            ║")
    print("╚════════════════════════════════════════════╝")

    print()
    print('"Small progress every day leads to big results."')
    print()

    input("Press ENTER to begin...")


# ---------------- LOAD DATA ----------------
# Loads saved goals from the JSON database
def load_data():

    global goals
    global completed_goals

    try:

        with open(DATABASE_FILE, "r") as file:
            data = json.load(file)

        goals = data["active_goals"]
        completed_goals = data["completed_goals"]

    except (FileNotFoundError, json.JSONDecodeError):
        goals = []
        completed_goals = []

# ---------------- SAVE DATA----------------
def save_data():
    data = {
        "active_goals": goals,
        "completed_goals": completed_goals
        }

    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)




# ---------------- GOAL OPTIONS ----------------
# Displays all available actions for a selected goal.
def goal_options(index):

    while True:

        clear_screen()

        print("══════════════════════════════")
        print("       ⚙ GOAL OPTIONS")
        print("══════════════════════════════")

        print(f"\n🏷 Selected Goal : {goals[index]}")

        print("\n1. ✅ Complete Goal")
        print("2. ✏ Rename Goal")
        print("3. 🗑 Delete Goal")
        print("4. 🔙 Back")

        choice = input("\nChoose an option ➜ ")

        if choice == "1":
            complete_goal(index)
            break

        elif choice == "2":
            rename_goal(index)
            break

        elif choice == "3":
            delete_goal(index)
            break

        elif choice == "4":
            break

        else:
            print("\n❌ Invalid choice.")
            input("\nPress ENTER to continue...")


# ---------------- COMPLETE GOAL ----------------
# Moves the selected goal from active to completed.
def complete_goal(index):

    item = goals.pop(index)

    completed_goals.append(item)

    save_data()

    clear_screen()

    print("══════════════════════════════")
    print("      🎉 GOAL COMPLETED")
    print("══════════════════════════════")

    print()
    print(f'🏆 "{item}"')
    print("has been completed successfully!")

    print()
    print("⚒ Keep Building Yourself!")

    input("\nPress ENTER to continue...")


# ---------------- RENAME GOAL ----------------
# Renames the selected goal.
def rename_goal(index):

    clear_screen()

    print("══════════════════════════════")
    print("        ✏ RENAME GOAL")
    print("══════════════════════════════")

    print(f"\nCurrent Goal : {goals[index]}")

    new_goal = input("\nEnter new goal name ➜ ")

    goals[index] = new_goal

    save_data()

    print(f'\n✅ Goal renamed to "{new_goal}"')

    input("\nPress ENTER to continue...")


# ---------------- DELETE GOAL ----------------
# Permanently deletes the selected goal.
def delete_goal(index):

    clear_screen()

    item = goals[index]

    print("══════════════════════════════")
    print("        🗑 DELETE GOAL")
    print("══════════════════════════════")

    print(f'\nSelected Goal : "{item}"')

    confirm = input("\nDelete this goal? (Y/N): ")

    if confirm.lower() == "y":

        goals.pop(index)

        save_data()

        print(f'\n🗑 "{item}" deleted successfully.')

    else:

        print("\n👍 Deletion cancelled.")

    input("\nPress ENTER to continue...")


# ---------------- CREATE GOAL ----------------
# Creates a new goal and saves it.
def create_goal():

    clear_screen()

    print("══════════════════════════════")
    print("        ➕ CREATE GOAL")
    print("══════════════════════════════")

    while True:
        goal_name = input("\nEnter your goal ➜ ").strip()

        if goal_name == "":
            print("❌ Please enter a valid goal.")

        elif goal_name.lower() in [goal.lower() for goal in goals]:
            print("⚠️ Goal already exists.")

        else:
            goals.append(goal_name)

            save_data()
            break
    


    print(f'\n✅ Goal "{goal_name}" created successfully!')

    input("\nPress ENTER to continue...")


# ---------------- ACTIVE GOALS ----------------
# Displays all active goals and lets the user
# choose one for more actions.
def active_goals():

    clear_screen()

    print("════════ ACTIVE GOALS ════════\n")

    if len(goals) == 0:

        print("🎉 Amazing!")
        print()
        print("You don't have any active goals.")
        print("Create a new goal")
        print("and continue building yourself!")

        input("\nPress ENTER to return...")
        return

    for index, goal in enumerate(goals, start=1):
        print(f"{index}. {goal}")

    print("\n──────────────────────────────")

    choice = input("Select a goal\nor B to go back ➜ ")

    if choice.lower() == "b":
        return

    try:

        index = int(choice) - 1

        if 0 <= index < len(goals):

            goal_options(index)

        else:

            print("\n❌ Invalid goal number.")
            input("Press ENTER to continue...")

    except ValueError:

        print("\n❌ Please enter a valid number.")
        input("Press ENTER to continue...")

# ---------------- HOME ----------------
# Displays the home page with a quick summary.
def home():

    clear_screen()

    print("══════════════════════════════")
    print("          🏠 HOME")
    print("══════════════════════════════")

    print(f"📌 Active Goals    : {len(goals)}")
    print(f"🏆 Completed Goals : {len(completed_goals)}")

    print("══════════════════════════════")
    print("⚒ FORGE v1.0")
    print("══════════════════════════════")


# ---------------- COMPLETED GOALS ----------------
# Displays all completed goals.
def view_completed_goals():

    clear_screen()

    print("══════ COMPLETED GOALS ══════\n")

    if len(completed_goals) == 0:

        print("🏆 No completed goals yet.\n")
        print("Complete your first goal")
        print("and begin your journey!")

    else:

        for index, goal in enumerate(completed_goals, start=1):
            print(f"🏆 {index}. {goal}")

    input("\nPress ENTER to return...")


# ---------------- DASHBOARD ----------------
# Displays goal statistics.
def view_progress():

    clear_screen()

    total = len(goals) + len(completed_goals)

    print("════════ DASHBOARD ════════\n")

    print(f"🎯 Total Goals     : {total}")
    print(f"📌 Active Goals    : {len(goals)}")
    print(f"🏆 Completed Goals : {len(completed_goals)}")

    if total > 0:

        progress = (len(completed_goals) / total) * 100

        print(f"📈 Completion Rate : {progress:.0f}%")

    else:

        print("📈 Completion Rate : 0%")

    print("\n══════════════════════════════")
    print("🔥 Keep Building Yourself!")
    print("══════════════════════════════")

    input("\nPress ENTER to return...")


# ---------------- MENU ----------------
# Main navigation menu.
def menu():

    while True:

        home()

        print()
        print("1. ➕ Create Goal")
        print("2. 🎯 Active Goals")
        print("3. 🏆 Completed Goals")
        print("4. 📊 Dashboard")
        print("5. 🚪 Exit")

        try:

            choice = int(input("\nChoose an option ➜ "))

            if choice == 1:

                create_goal()

            elif choice == 2:

                active_goals()

            elif choice == 3:

                view_completed_goals()

            elif choice == 4:

                view_progress()

            elif choice == 5:

                confirm = input("\nAre you sure you want to exit? (Y/N): ")

                if confirm.lower() == "y":

                    clear_screen()

                    print()
                    print("══════════════════════════════")
                    print("     Thanks for using FORGE")
                    print("══════════════════════════════")
                    print()
                    print("⚒ Keep Building Yourself!")
                    print()

                    break

            else:

                print("\n❌ Invalid choice.")
                input("Press ENTER to continue...")

        except ValueError:

            print("\n❌ Please enter a number between 1 and 5.")
            input("Press ENTER to continue...")


# ---------------- MAIN ----------------
# Program starting point.
def main():

    welcome()

    load_data()

    menu()


# ---------------- START PROGRAM ----------------
main()