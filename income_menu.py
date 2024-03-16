import income_db
import income_utils
import datetime

# Contains all the menu functions for the income section.

def main_menu():
    print("\nIncome Options")

    while True:
        user_input = input('''\nPlease select from one of the following options:
1 - Add an income
2 - Delete an income                           
3 - Edit an income
4 - View all incomes
5 - View income by category
6 - Add a new income category
7 - Delete an income category                           
0 - Return to previous menu
: ''')

        # Add an income.
        if user_input == '1':
            add_income()

        # Delete an income.
        if user_input == '2':
            delete_income()

        # Edit an income.
        if user_input == '3':
            edit_income()

        # View all incomes.
        elif user_input == '4':
            view_all()

        # View income by category.
        elif user_input == '5':
            view_by_category()

        # Add a new income category.
        elif user_input == '6':
            add_category()
        
        # Delete an income category.
        elif user_input == '7':
            delete_category()

        # Return to previous menu.
        elif user_input == '0':
            return

# Adds an income.     
def add_income():
    # Get list of current income categories.
    current_income_cats = income_db.get_cat_list()
    # If the list is not empty (there might be no categories added).
    if len(current_income_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_income_cats[0] == 1:
            print("\nSorry, something went wrong accessing the income categories database.")
            print(f"Error: {current_income_cats[1]}")
            return
    
    # Get list of current income names.
    current_income_names = income_db.get_name_list()
    # If the list is not empty (there might be no income added).
    if len(current_income_names) != 0:
        # If the get_cat_list() function has returned an error.
        if current_income_names[0] == 1:
            print("\nSorry, something went wrong retrieving the income names.")
            print(f"Error: {current_income_names[1]}")
            return
    
    # Tells the user what's happening.
    print("\nAdding a new income.")

    # If income categories exist, print the current categories. Otherwise, return the user to the menu.
    if len(current_income_cats) != 0:
        print("\nThe current income categories are:")
        for income_cat in current_income_cats:
            print(income_cat.capitalize())
    else:
        print("\nYou can't add an income as you haven't added any income categories.")
        return
    
    # Create an empty list to add the new income data to.
    new_income_info = []

    # Gets the income category to add the income to.
    new_income_cat = income_utils.get_new_income_cat(current_income_cats)
    # If the result is 1, return to the previous menu.
    if new_income_cat == 1:
        return
    else:
        new_income_info.append(new_income_cat)

    # Gets the name of the new income.
    new_income_name = income_utils.get_new_income_name(current_income_names)
    # If the result is 1, return to the previous menu.
    if new_income_cat == 1:
        return
    else:
        new_income_info.append(new_income_name)

    # Gets the amount of the new income
    new_income_amount = income_utils.get_new_income_amount()
    # If the result is 1, return to the previous menu.
    if new_income_amount == 1:
        return
    else:
        new_income_info.append(new_income_amount)

    # Gets today's date.
    new_income_date = datetime.datetime.today().strftime('%Y-%m-%d')
    new_income_info.append(new_income_date)

    #print(new_income_info)

    # Adds the new income to the tracker.
    add_income_result = income_db.add_income(new_income_info)
    if add_income_result[0] == 1:
        print("\nSorry, something went wrong adding the income to the database.")
        print(f"Error: {add_income_result[1]}")
        return
    elif add_income_result[0] == 0:
        print(f"\n{new_income_info[1].capitalize()} was successfully added to the database.")
        return
    else:
        print("\nSorry, an unexpected error has occurred and the income could not be added to the database.")

# Deletes an income
def delete_income():
    # Get list of current income names.
    current_income_names = income_db.get_name_list()
    # If the list is not empty (there might be no income added).
    if len(current_income_names) != 0:
        # If the get_cat_list() function has returned an error.
        if current_income_names[0] == 1:
            print("\nSorry, something went wrong retrieving the income names.")
            print(f"Error: {current_income_names[1]}")
            return

    # Tells the user what's happening.
    print("\nDeleting an income.")

    # Get the name of the income to delete.
    income_to_delete = income_utils.get_income_to_delete(current_income_names)
    # Returns to the previous menu if income_to_delete returns 1.
    if income_to_delete == 1:
        return
    
    # Tells the user what's happening.
    print(f"\nDeleting {income_to_delete.capitalize()} from the database...")

    # Deletes the existing income from the database.
    delete_income_result = income_db.delete_income(income_to_delete)
    # Handles unexpected behaviour of the function not returning a list/anything.
    if len(delete_income_result) == 0:
        print(f"\nAn unexpected error occurred while trying to delete {income_to_delete.capitalize()} from the database.")
        return
    
    # If successful, the first index of the result list is 0.
    if delete_income_result[0] == 0:
        print(f"\n{income_to_delete.capitalize()} was successfully deleted from the database.")
        return
    # If unsuccessful, the first index will be 1.
    elif delete_income_result[0] == 1:
        print(f"\nSorry, something went wrong and {income_to_delete.capitalize()} could not be deleted from the database.")
        print(f"Error: {delete_income_result[1]}")
        return
    # Handles behaviour if the result contains anything other than the expected conditions.
    else:
        print(f"\nAn unexpected error occurred while trying to delete {income_to_delete.capitalize()} from the database.")
        return

# Edits an income.
def edit_income():
    # Get list of current income categories.
    current_income_cats = income_db.get_cat_list()
    # If the list is not empty (there might be no categories added).
    if len(current_income_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_income_cats[0] == 1:
            print("\nSorry, something went wrong accessing the income categories database.")
            print(f"Error: {current_income_cats[1]}")
            return
    
    # Get list of current income names.
    current_income_names = income_db.get_name_list()
    # If the list is not empty (there might be no income added).
    if len(current_income_names) != 0:
        # If the get_cat_list() function has returned an error.
        if current_income_names[0] == 1:
            print("\nSorry, something went wrong retrieving the income names.")
            print(f"Error: {current_income_names[1]}")
            return

    # Lists the current income.
    print("\nList of current income:\n")
    for income in current_income_names:
        print(income.capitalize())

    # Gets the name of the income to edit from the user.
    income_name_to_edit = income_utils.get_income_to_edit(current_income_names)
    # If the result is 1, return to the previous menu.
    if income_name_to_edit == 1:
        return

    # Tells the user what's happening.
    print(f"\nYou are editing the {income_name_to_edit.capitalize()} income.")

    # Gets the current info from the database of the income that's going to be edited.
    income_to_edit_current_info = income_db.get_income(income_name_to_edit)
    # If the list is not empty.
    if len(income_to_edit_current_info) != 0:
        # If the get_income() function has returned an error.
        if income_to_edit_current_info[0] == 1:
            print(f"\nSorry, something went wrong retrieving {income_to_edit_current_info.capitalize}'s information.")
            print(f"Error: {income_to_edit_current_info[1]}")
            return

    # Create an empty list to add the new income data to.    
    new_income_info = []

    # Gets the change of income category if required.
    edited_income_cat = income_utils.get_edit_income_cat(current_income_cats, income_to_edit_current_info[0])
    # If the result is 1, return to the previous menu.
    if edited_income_cat == 1:
        return
    # If the result is 2, no change so add current info to new_income_info
    elif edited_income_cat == 2:
        new_income_info.append(income_to_edit_current_info[0][0])
    # Otherwise add the new income category to new_income_info.
    else:
        new_income_info.append(edited_income_cat)

    #print(new_income_info)

    # Gets the change of name if required.
    edited_income_name = income_utils.get_edit_income_name(current_income_names, income_to_edit_current_info[0])
    # If the result is 1, return to the previous menu.
    if edited_income_name == 1:
        return
    # If the result is 2, no change so add current info to new_income_info
    elif edited_income_name == 2:
        new_income_info.append(income_to_edit_current_info[0][1])
    # Otherwise add the new name to new_income_info.
    else:
        new_income_info.append(edited_income_name)

    #print(new_income_info)

    # Gets the change of value if required.
    edited_income_amount = income_utils.get_edit_income_amount(income_to_edit_current_info[0])
    # If the result is 1, return to the previous menu.
    if edited_income_amount == 1:
        return
    # If the result is 2, no change so add current info to new_income_info
    elif edited_income_amount == 2:
        new_income_info.append(income_to_edit_current_info[0][2])
    # Otherwise add the new amount to new_income_info.
    else:
        new_income_info.append(edited_income_amount)

    #print(new_income_info)

    # Gets today's date.
    new_income_date = datetime.datetime.today().strftime('%Y-%m-%d')
    new_income_info.append(new_income_date)

    #print(new_income_info)

    # Updates the income with the new info.
    edit_income_result = income_db.update_income(new_income_info, income_to_edit_current_info[0][1])
    if edit_income_result[0] == 1:
        print("\nSorry, something went wrong while updating the income.")
        print(f"Error: {edit_income_result[1]}")
        return
    if edit_income_result[0] == 0:
        print(f"\n{new_income_info[1].capitalize()} has been successfully updated.")
        return
    else:
        print("\nSorry, an unexpected error has occurred and the income could not be updated.")    

# Views all income.
def view_all():
    # Get list of all income.
    income_info = income_db.get_all_income()
    # If the list is empty.
    if len(income_info) == 0:
        print("\nYou haven't added any income.")
        return
    # If get_all_income() has returned an error.
    if income_info[0] == 1:
        print("\nSorry, something went wrong accessing the income database.")
        print(f"Error: {income_info[1]}")
        return

    # Tells the user what's happening.
    print("\nViewing all income:\n")

    # Prints all the income.
    print("Name -- Category -- Amount -- Date Added")
    for income in income_info:
        print(f"{income[1].capitalize()} -- {income[0].capitalize()} -- {income[2]} -- {income[3]}")
    
    # Prints how many income have been added.
    if len(income_info) == 1:
        print(f"\nYou have added 1 income to the database.")
    else:
        print(f"\nYou have added {len(income_info)} incomes to the database.")

# Views income by category.
def view_by_category():
    # Get list of current income categories.
    current_income_cats = income_db.get_cat_list()

    # If the list is empty.
    if len(current_income_cats) == 0:
        print("\nYou haven't added any income categories.")
        return
    # If the list is not empty.
    elif len(current_income_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_income_cats[0] == 1:
            print("\nSorry, something went wrong accessing the income categories database.")
            print(f"Error: {current_income_cats[1]}")
            return
    
    # Prints a list of income categories.
    if len(current_income_cats) != 0:
        print("\nThe current income categories are:")
        for income_cat in current_income_cats:
            print(income_cat.capitalize())

    while True:
        # Gets the income category to view.
        cat_to_view = income_utils.get_cat_to_view(current_income_cats)
        # If the result is 1, return to the previous menu.
        if cat_to_view == 1:
            return

        # Gets the income in that category.
        income_info = income_db.get_income_from_category(cat_to_view)

        # If the category list is empty.
        if len(income_info) == 0:
            print("\nYou haven't added any income to this category.")
            continue
        # If get_all_income() has returned an error.
        if income_info[0] == 1:
            print("\nSorry, something went wrong accessing the income database.")
            print(f"Error: {income_info[1]}")
            return
        break

    # Tells the user what's happening.
    print(f"\nViewing income in the {cat_to_view.capitalize()} category:\n")

    # Prints all the income.
    print("Name -- Category -- Amount -- Date Added")
    for income in income_info:
        print(f"{income[1].capitalize()} -- {income[0].capitalize()} -- {income[2]} -- {income[3]}")
    
    # Prints how many income have been added.
    if len(income_info) == 1:
        print(f"\nThere is 1 income in this category.")
    else:
        print(f"\nThere are {len(income_info)} income in this category.")

# Adds a new income category.
def add_category():
    # Get list of current income categories.
    current_income_cats = income_db.get_cat_list()
    # If the list is not empty.
    if len(current_income_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_income_cats[0] == 1:
            print("\nSorry, something went wrong accessing the income categories database.")
            print(f"Error: {current_income_cats[1]}")
            return

    # Tells the user what's happening.
    print("\nAdding a new income category.")

    # If the list isn't empty, print the current categories.
    if len(current_income_cats) != 0:
        print("\nThe current income categories are:")
        for income_cat in current_income_cats:
            print(income_cat.capitalize())

    # Get the name of the new income category.
    new_income_cat_name = income_utils.get_new_cat_name(current_income_cats)
    # Returns to the previous menu if get_new_cat_name returns 1.
    if new_income_cat_name == 1:
        return
    
    # Tells the user what's happening.
    print(f"\nAdding {new_income_cat_name.capitalize()} to the database...")

    # Adds the income category to the database.
    add_cat_result = income_db.add_income_cat(new_income_cat_name)
    # Handles unexpected behaviour of the function not returning a list/anything.
    if len(add_cat_result) == 0:
        print(f"\nAn unexpected error occurred while trying to add {new_income_cat_name.capitalize()} to the database.")
        return
    
    # If successful, the first index of the result list is 0.
    if add_cat_result[0] == 0:
        print(f"\n{new_income_cat_name.capitalize()} was successfully added to the database.")
        return
    # If unsuccessful, the first index will be 1.
    elif add_cat_result[0] == 1:
        print(f"\nSorry, something went wrong and {new_income_cat_name.capitalize()} could not be added to the database.")
        print(f"Error: {add_cat_result[1]}")
        return
    # Handles behaviour if the result contains anything other than the expected conditions.
    else:
        print(f"\nAn unexpected error occurred while trying to add {new_income_cat_name.capitalize()} to the database.")
        return

# Deletes an income category.
def delete_category():
    # Get list of current income categories.
    current_income_cats = income_db.get_cat_list()
    # If the list is not empty.
    if len(current_income_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_income_cats[0] == 1:
            print("\nSorry, something went wrong accessing the income categories database.")
            print(f"Error: {current_income_cats[1]}")
            return

    # Tells the user what's happening.
    print("\nDeleting an income category.")

    # If the list isn't empty, print the current categories.
    if len(current_income_cats) != 0:
        print("\nThe current income categories are:")
        for income_cat in current_income_cats:
            print(income_cat.capitalize())

    # Get the name of the income category to delete.
    income_cat_to_delete = income_utils.get_cat_to_delete(current_income_cats)
    # Returns to the previous menu if income_cat_to_delete() returns 1.
    if income_cat_to_delete == 1:
        return
    
    # Tells the user what's happening.
    print(f"\nDeleting {income_cat_to_delete.capitalize()} from the database...")

    # Deletes the existing category from the database.
    delete_cat_result = income_db.delete_income_cat(income_cat_to_delete)
    # Handles unexpected behaviour of the function not returning a list/anything.
    if len(delete_cat_result) == 0:
        print(f"\nAn unexpected error occurred while trying to delete {income_cat_to_delete.capitalize()} from the database.")
        return
    
    # If successful, the first index of the result list is 0.
    if delete_cat_result[0] == 0:
        print(f"\n{income_cat_to_delete.capitalize()} was successfully deleted from the income categories database.")
    # If unsuccessful, the first index will be 1.
    elif delete_cat_result[0] == 1:
        print(f"\nSorry, something went wrong and {income_cat_to_delete.capitalize()} could not be deleted from the database.")
        print(f"Error: {delete_cat_result[1]}")
        return
    # Handles behaviour if the result contains anything other than the expected conditions.
    else:
        print(f"\nAn unexpected error occurred while trying to delete {income_cat_to_delete.capitalize()} from the database.")
        return
    
    # Deletes the income associated with the category from the database.
    delete_income_result = income_db.delete_income(income_cat_to_delete)
    # Handles unexpected behaviour of the function not returning a list/anything.
    if len(delete_income_result) == 0:
        print(f"\nAn unexpected error occurred while trying to delete income from the database.")
        return
    
    # If successful, the first index of the result list is 0.
    if delete_income_result[0] == 0:
        print(f"\nincome associated with {income_cat_to_delete.capitalize()} were successfully deleted from the income categories database.")
        return
    # If unsuccessful, the first index will be 1.
    elif delete_cat_result[0] == 1:
        print(f"\nSorry, something went wrong and the income could not be deleted from the database.")
        print(f"Error: {delete_cat_result[1]}")
        return
    # Handles behaviour if the result contains anything other than the expected conditions.
    else:
        print(f"\nAn unexpected error occurred while trying to delete income from the database.")
        return    