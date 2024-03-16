import expenses_db
import datetime

# Contains all the menu functions for the budget section.

def main_menu():
    print("\nBudgeting Options")

    while True:
        user_input = input('''\nPlease select from one of the following options:
1 - Set a budget
2 - View budgets
0 - Return to previous menu
: ''')

        # Set a budget.
        if user_input == '1':
            set_budget()

        # View all budgets.
        elif user_input == '2':
            view_budget()

        # Return to previous menu.
        elif user_input == '0':
            return
        
# Sets a budget.
def set_budget():
    pass

# Views budgets.
def view_budget():
    pass
