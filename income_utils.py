# Utility functions for the income part of the tracker.

# Gets the name of a new category.
def get_new_cat_name(current_income_cats):
    while True:
        print('')
        cat_input = input('''Please enter a single word to describe the income category. It must be unique.
Enter 0 to return to the previous menu.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_income_cats:
            print("\nThe category you entered matches an existing category.")
            continue
        if cat_input.isalpha():
            return cat_input
        else:
            print("\nPlease only use one word to describe the category.")

# Gets the name of an income category for a new income.
def get_new_income_cat(current_income_cats):
    while True:
        print('')
        cat_input = input('''Please enter the name of the category you wish to add the income to. Enter 0 to cancel.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_income_cats:
            return cat_input
        else:
            print("\nYou did not enter the name of a category.")

# Gets the name of a new income.
def get_new_income_name(current_income_names):
    while True:
        print('')
        name_input = input('''Please enter a single word to describe the income. It must be unique.
Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        if name_input in current_income_names:
            print("\nThe income name you entered matches an existing name.")
            continue
        if name_input.isalpha():
            return name_input
        else:
            print("\nPlease only use one word to describe the income.")

# Gets the amount of a new income.
def get_new_income_amount():
    while True:
        print('')
        amount_input = input('''Please enter the amount of the income. Enter 0 to return to the previous menu.
: ''').lower()
        error_count = 0
        if amount_input == '0':
            return 1
        try:
            float(amount_input)
        except ValueError:
            error_count += 1
        try:
            int(amount_input)
        except ValueError:
            error_count += 1
        if error_count == 2:
            print("\nPlease enter a value for the income.")
        else:
            return str(amount_input)

# Gets the category for an income edit. 
def get_edit_income_cat(current_income_cats, current_income_info):
    # Checks if the user wants to edit the income category.
    while True:
        print('')
        confirm_input = input(f'''The current category is {current_income_info[0].capitalize()}.
Would you like to change it? Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            break
        elif confirm_input == 'no' or confirm_input == 'n':
            return 2
        else:
            print("\nPlease enter yes or no.")

    # Prints the current income categories.
    print('\nThe current income categories are:')
    for income_cat in current_income_cats:
        print(income_cat.capitalize())

    # Gets the name of the new category.
    while True:
        print('')
        new_cat_input = input(f'''Please enter the category you wish to change the income to. Enter 0 to return to the previous menu.
: ''').lower()
        if new_cat_input == '0':
            return 1
        elif new_cat_input in current_income_cats:
            return new_cat_input
        else:
            print("\nYou did not enter the name of a category.")

# Gets a new name for an income edit.
def get_edit_income_name(current_income_names, current_income_info):
    # Checks if the user wants to edit the income name.    
    while True:
        print('')
        confirm_input = input(f'''The name of the income is {current_income_info[1].capitalize()}.
Would you like to change it? Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            break
        elif confirm_input == 'no' or confirm_input == 'n':
            return 2
        else:
            print("\nPlease enter yes or no.")

    # Prints a list of current income names.
    print('\nThe current income names are:')
    for name in current_income_names:
        print(name.capitalize())

    # Gets a new name if needed.
    while True:
        print('')
        new_name_input = input(f'''Please enter a new name for the income. It must be unique.
Enter 0 to return to the previous menu.
: ''').lower()
        if new_name_input == '0':
            return 1
        if new_name_input in current_income_names:
            print("\nThe income name you entered matches an existing name.")
            continue
        if new_name_input.isalpha():
            return new_name_input
        else:
            print("\nPlease only use one word to describe the income.")

# Gets a new amount for an income edit.
def get_edit_income_amount(current_income_info):
    # Checks if the user wants to edit the income amount.
    while True:
        print('')
        confirm_input = input(f'''The value of the income is {current_income_info[2]}.
Would you like to change it? Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            break
        elif confirm_input == 'no' or confirm_input == 'n':
            return 2
        else:
            print("\nPlease enter yes or no.")

    # Gets a new income amount if required.
    while True:
        print('')
        new_amount_input = input('''Please enter the new amount of the income. Enter 0 to return to the previous menu.
: ''').lower()
        error_count = 0
        if new_amount_input == '0':
            return 1
        try:
            float(new_amount_input)
        except ValueError:
            error_count += 1
        try:
            int(new_amount_input)
        except ValueError:
            error_count += 1
        if error_count == 2:
            print("\nPlease enter a value for the income.")
        else:
            return str(new_amount_input)
        
# Gets the name of the income to edit.        
def get_income_to_edit(current_income_names):
    while True:
        print('')
        name_input = input('''Please enter the name of the income you want to edit. Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        if name_input in current_income_names:
            return name_input
        else:
            print("\nYou did not enter the name of a income.")     

# Gets the name of the income to delete.
def get_income_to_delete(current_income_names):
    while True:
        print('')
        name_input = input('''Please enter the name of the income you want to delete. Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        if name_input in current_income_names:
            return name_input
        else:
            print("\nYou did not enter the name of a income.")   

# Gets the name of the category to view.
def get_cat_to_view(current_income_cats):
    while True:
        print('')
        cat_input = input('''Please enter the name of the category you want to view. Enter 0 to return to the previous menu.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_income_cats:
            return cat_input
        else:
            print("\nYou did not enter the name of a category.") 

# Gets the name of the category to delete.
def get_cat_to_delete(current_income_cats):
    # Gets the name.
    while True:
        print('')
        cat_input = input('''Please enter the name of the category you want to delete. Enter 0 to return to the previous menu.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_income_cats:
            break
        else:
            print("\nYou did not enter the name of a category.")
    
    # Confirms that the user does want to delete the category.
    while True:
        confirm_input = input(f'''\nAre you sure you want to delete the {cat_input.capitalize()} category? All income in this
category will also be deleted. Please enter yes or no.
: ''').lower()
        if confirm_input == 'yes' or confirm_input == 'y':
            return cat_input
        elif confirm_input == 'no' or confirm_input == 'n':
            return 1
        else:
            print("\nPlease enter yes or no.")