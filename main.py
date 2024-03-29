## Overview ##
# The bookstore_main program has been split up into three modules to try and keep the main program clean.
# The menu.py module contains the top-level menu functions, which call seperate functions to get information from the user and pass that information into the database.
# The user.py module contains the functions that interact with the user.
# The db.py module contains the functions that interact with the database.


## Imports ##
import expenses_menu
import income_menu
import budget_menu
import goals_menu
import expenses_db
import income_db
import budget_db
import goals_db
            
## Main Code ##

# Introduction.
print('\nSaving and Expense Tracker')

# db creation error count.
db_errors = 0

# Expenses table.
db_expenses_result = expenses_db.create_expenses()
if db_expenses_result[0] == 1:
    print("\nSorry, we couldn't create the expenses database table.")
    print(f"Error: {db_expenses_result[1]}")
    db_errors += 1
# Expense categories table.
db_expense_cat_result = expenses_db.create_expense_cats()
if db_expense_cat_result[0] == 1:
    print("\nSorry, we couldn't create the expense category database table.")
    print(f"Error: {db_expense_cat_result[1]}")
    db_errors += 1

# Income table.
db_income_result = income_db.create_income()
if db_income_result[0] == 1:
    print("\nSorry, we couldn't create the income database table.")
    print(f"Error: {db_income_result[1]}")
    db_errors += 1
# Income categories table.
db_income_cat_result = income_db.create_income_cats()
if db_income_cat_result[0] == 1:
    print("\nSorry, we couldn't create the income category database table.")
    print(f"Error: {db_income_cat_result[1]}")
    db_errors += 1

# Budget db.
db_budget_result = budget_db.create()
if db_budget_result[0] == 1:
    print("\nSorry, we couldn't create the budget database.")
    print(f"Error: {db_budget_result[1]}")
    db_errors += 1

# Goals db.
db_goals_result = goals_db.create()
if db_goals_result[0] == 1:
    print("\nSorry, we couldn't create the goals database.")
    print(f"Error: {db_goals_result[1]}")
    db_errors += 1

# Quits if errors found.
if db_errors != 0:
    print("\nErrors have been found when creating the databases. The program will quit.")
    quit()

# Main menu.
while True:
    user_input = input('''\nPlease select from one of the following options:
1 - View expense options
2 - View income options
3 - View budgeting options
4 - View financial goal options
0 - Exit the program
: ''')

    # View expense options.
    if user_input == '1':
        expenses_menu.main_menu()
    
    # View income options.
    elif user_input == '2':
        income_menu.main_menu()

    # View budgeting options.
    elif user_input == '3':
        income_menu.main_menu()

    # View financial goal options.
    elif user_input == '4':
        income_menu.main_menu()    

    # Exit program.
    elif user_input == '0':
        print('\nLogging off...')
        exit()