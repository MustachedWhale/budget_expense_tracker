import expenses_db
import datetime

# Contains all the menu functions for the goals section.

def main_menu():
    print("\nGoal Options")

    while True:
        user_input = input('''\nPlease select from one of the following options:
1 - Create a saving goal
2 - Create an income goal
3 - Add money to saving goal
4 - View all goals 
0 - Return to previous menu
: ''')

        # Creates a saving goal.
        if user_input == '1':
            create_saving_goal()

        # Creates an income goal.
        elif user_input == '2':
            create_income_goal()

        # Adds money to a saving goal.
        elif user_input == '3':
            add_to_saving_goal()

        # Views all goals.
        elif user_input == '4':
            view_all_goals()

        # Return to previous menu.
        elif user_input == '0':
            return

# Creates a saving goal.
def create_saving_goal():
    pass

# Creates an income goal.
def create_income_goal():
    pass

# Adds money to a saving goal.
def add_to_saving_goal():
    pass

# Views all goals.
def view_all_goals():
    pass