import expenses_db
import expenses_utils
import datetime

# Contains all the menu functions for the expenses section of the tracker.

def main_menu():
    print("\nExpense Options")

    while True:
        user_input = input('''\nPlease select from one of the following options:
1 - Add an expense
2 - Delete an expense                           
3 - Edit an expense
4 - View all expenses
5 - View expenses by category
6 - Add a new expense category
7 - Delete an expense category                           
0 - Return to previous menu
: ''')

        # Add an expense.
        if user_input == '1':
            add_expense()

        # Delete an expense.
        if user_input == '2':
            delete_expense()

        # Edit an expense.
        if user_input == '3':
            edit_expense()

        # View all expenses.
        elif user_input == '4':
            view_all()

        # View expenses by category.
        elif user_input == '5':
            view_by_category()

        # Add a new expense category.
        elif user_input == '6':
            add_category()
        
        # Delete an expense category.
        elif user_input == '7':
            delete_category()

        # Return to previous menu.
        elif user_input == '0':
            return

# Adds an expense.     
def add_expense():
    # Get list of current expense categories.
    current_expense_cats = expenses_db.get_cat_list()
    # If the list is not empty (there might be no categories added).
    if len(current_expense_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_expense_cats[0] == 1:
            print("\nSorry, something went wrong accessing the expense categories database.")
            print(f"Error: {current_expense_cats[1]}")
            return
    
    # Get list of current expense names.
    current_expense_names = expenses_db.get_name_list()
    # If the list is not empty (there might be no expenses added).
    if len(current_expense_names) != 0:
        # If the get_cat_list() function has returned an error.
        if current_expense_names[0] == 1:
            print("\nSorry, something went wrong retrieving the expense names.")
            print(f"Error: {current_expense_names[1]}")
            return
    
    # Tells the user what's happening.
    print("\nAdding a new expense.")

    # If expense categories exist, print the current categories. Otherwise, return the user to the menu.
    if len(current_expense_cats) != 0:
        print("\nThe current expense categories are:")
        for expense_cat in current_expense_cats:
            print(expense_cat.capitalize())
    else:
        print("\nYou can't add an expense as you haven't added any expense categories.")
        return
    
    # Create an empty list to add the new expense data to.
    new_expense_info = []

    # Gets the expense category to add the expense to.
    new_expense_cat = expenses_utils.get_new_expense_cat(current_expense_cats)
    # If the result is 1, return to the previous menu.
    if new_expense_cat == 1:
        return
    else:
        new_expense_info.append(new_expense_cat)

    # Gets the name of the new expense.
    new_expense_name = expenses_utils.get_new_expense_name(current_expense_names)
    # If the result is 1, return to the previous menu.
    if new_expense_cat == 1:
        return
    else:
        new_expense_info.append(new_expense_name)

    # Gets the amount of the new expense
    new_expense_amount = expenses_utils.get_new_expense_amount()
    # If the result is 1, return to the previous menu.
    if new_expense_amount == 1:
        return
    else:
        new_expense_info.append(new_expense_amount)

    # Gets today's date.
    new_expense_date = datetime.datetime.today().strftime('%Y-%m-%d')
    new_expense_info.append(new_expense_date)

    #print(new_expense_info)

    # Adds the new expense to the tracker.
    add_expense_result = expenses_db.add_expense(new_expense_info)
    if add_expense_result[0] == 1:
        print("\nSorry, something went wrong adding the expense to the database.")
        print(f"Error: {add_expense_result[1]}")
        return
    elif add_expense_result[0] == 0:
        print(f"\n{new_expense_info[1].capitalize()} was successfully added to the database.")
        return
    else:
        print("\nSorry, an unexpected error has occurred and the expense could not be added to the database.")

# Deletes an expense
def delete_expense():
    # Get list of current expense names.
    current_expense_names = expenses_db.get_name_list()
    # If the list is not empty (there might be no expenses added).
    if len(current_expense_names) != 0:
        # If the get_cat_list() function has returned an error.
        if current_expense_names[0] == 1:
            print("\nSorry, something went wrong retrieving the expense names.")
            print(f"Error: {current_expense_names[1]}")
            return

    # Tells the user what's happening.
    print("\nDeleting an expense.")

    # Get the name of the expense to delete.
    expense_to_delete = expenses_utils.get_expense_to_delete(current_expense_names)
    # Returns to the previous menu if expense_to_delete returns 1.
    if expense_to_delete == 1:
        return
    
    # Tells the user what's happening.
    print(f"\nDeleting {expense_to_delete.capitalize()} from the database...")

    # Deletes the existing expense from the database.
    delete_expense_result = expenses_db.delete_expense(expense_to_delete)
    # Handles unexpected behaviour of the function not returning a list/anything.
    if len(delete_expense_result) == 0:
        print(f"\nAn unexpected error occurred while trying to delete {expense_to_delete.capitalize()} from the database.")
        return
    
    # If successful, the first index of the result list is 0.
    if delete_expense_result[0] == 0:
        print(f"\n{expense_to_delete.capitalize()} was successfully deleted from the database.")
        return
    # If unsuccessful, the first index will be 1.
    elif delete_expense_result[0] == 1:
        print(f"\nSorry, something went wrong and {expense_to_delete.capitalize()} could not be deleted from the database.")
        print(f"Error: {delete_expense_result[1]}")
        return
    # Handles behaviour if the result contains anything other than the expected conditions.
    else:
        print(f"\nAn unexpected error occurred while trying to delete {expense_to_delete.capitalize()} from the database.")
        return

# Edits an expense.
def edit_expense():
    # Get list of current expense categories.
    current_expense_cats = expenses_db.get_cat_list()
    # If the list is not empty (there might be no categories added).
    if len(current_expense_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_expense_cats[0] == 1:
            print("\nSorry, something went wrong accessing the expense categories database.")
            print(f"Error: {current_expense_cats[1]}")
            return
    
    # Get list of current expense names.
    current_expense_names = expenses_db.get_name_list()
    # If the list is not empty (there might be no expenses added).
    if len(current_expense_names) != 0:
        # If the get_cat_list() function has returned an error.
        if current_expense_names[0] == 1:
            print("\nSorry, something went wrong retrieving the expense names.")
            print(f"Error: {current_expense_names[1]}")
            return

    # Lists the current expenses.
    print("\nList of current expenses:\n")
    for expense in current_expense_names:
        print(expense.capitalize())

    # Gets the name of the expense to edit from the user.
    expense_name_to_edit = expenses_utils.get_expense_to_edit(current_expense_names)
    # If the result is 1, return to the previous menu.
    if expense_name_to_edit == 1:
        return

    # Tells the user what's happening.
    print(f"\nYou are editing the {expense_name_to_edit.capitalize()} expense.")

    # Gets the current info from the database of the expense that's going to be edited.
    expense_to_edit_current_info = expenses_db.get_expense(expense_name_to_edit)
    # If the list is not empty.
    if len(expense_to_edit_current_info) != 0:
        # If the get_expense() function has returned an error.
        if expense_to_edit_current_info[0] == 1:
            print(f"\nSorry, something went wrong retrieving {expense_to_edit_current_info.capitalize}'s information.")
            print(f"Error: {expense_to_edit_current_info[1]}")
            return

    # Create an empty list to add the new expense data to.    
    new_expense_info = []

    # Gets the change of expense category if required.
    edited_expense_cat = expenses_utils.get_edit_expense_cat(current_expense_cats, expense_to_edit_current_info[0])
    # If the result is 1, return to the previous menu.
    if edited_expense_cat == 1:
        return
    # If the result is 2, no change so add current info to new_expense_info
    elif edited_expense_cat == 2:
        new_expense_info.append(expense_to_edit_current_info[0][0])
    # Otherwise add the new expense category to new_expense_info.
    else:
        new_expense_info.append(edited_expense_cat)

    #print(new_expense_info)

    # Gets the change of name if required.
    edited_expense_name = expenses_utils.get_edit_expense_name(current_expense_names, expense_to_edit_current_info[0])
    # If the result is 1, return to the previous menu.
    if edited_expense_name == 1:
        return
    # If the result is 2, no change so add current info to new_expense_info
    elif edited_expense_name == 2:
        new_expense_info.append(expense_to_edit_current_info[0][1])
    # Otherwise add the new name to new_expense_info.
    else:
        new_expense_info.append(edited_expense_name)

    #print(new_expense_info)

    # Gets the change of value if required.
    edited_expense_amount = expenses_utils.get_edit_expense_amount(expense_to_edit_current_info[0])
    # If the result is 1, return to the previous menu.
    if edited_expense_amount == 1:
        return
    # If the result is 2, no change so add current info to new_expense_info
    elif edited_expense_amount == 2:
        new_expense_info.append(expense_to_edit_current_info[0][2])
    # Otherwise add the new amount to new_expense_info.
    else:
        new_expense_info.append(edited_expense_amount)

    #print(new_expense_info)

    # Gets today's date.
    new_expense_date = datetime.datetime.today().strftime('%Y-%m-%d')
    new_expense_info.append(new_expense_date)

    #print(new_expense_info)

    # Updates the expense with the new info.
    edit_expense_result = expenses_db.update_expense(new_expense_info, expense_to_edit_current_info[0][1])
    if edit_expense_result[0] == 1:
        print("\nSorry, something went wrong while updating the expense.")
        print(f"Error: {edit_expense_result[1]}")
        return
    if edit_expense_result[0] == 0:
        print(f"\n{new_expense_info[1].capitalize()} has been successfully updated.")
        return
    else:
        print("\nSorry, an unexpected error has occurred and the expense could not be updated.")    

# Views all expenses.
def view_all():
    # Get list of all expenses.
    expense_info = expenses_db.get_all_expenses()
    # If the list is empty.
    if len(expense_info) == 0:
        print("\nYou haven't added any expenses.")
        return
    # If get_all_expenses() has returned an error.
    if expense_info[0] == 1:
        print("\nSorry, something went wrong accessing the expenses database.")
        print(f"Error: {expense_info[1]}")
        return

    # Tells the user what's happening.
    print("\nViewing all expenses:\n")

    # Prints all the expenses.
    print("Name -- Category -- Amount -- Date Added")
    for expense in expense_info:
        print(f"{expense[1].capitalize()} -- {expense[0].capitalize()} -- {expense[2]} -- {expense[3]}")
    
    # Prints how many expenses have been added.
    if len(expense_info) == 1:
        print(f"\nYou have added 1 expense to the database.")
    else:
        print(f"\nYou have added {len(expense_info)} expenses to the database.")

# Views expenses by category.
def view_by_category():
    # Get list of current expense categories.
    current_expense_cats = expenses_db.get_cat_list()

    # If the list is empty.
    if len(current_expense_cats) == 0:
        print("\nYou haven't added any expense categories.")
        return
    # If the list is not empty.
    elif len(current_expense_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_expense_cats[0] == 1:
            print("\nSorry, something went wrong accessing the expense categories database.")
            print(f"Error: {current_expense_cats[1]}")
            return
    
    # Prints a list of expense categories.
    if len(current_expense_cats) != 0:
        print("\nThe current expense categories are:")
        for expense_cat in current_expense_cats:
            print(expense_cat.capitalize())

    while True:
        # Gets the expense category to view.
        cat_to_view = expenses_utils.get_cat_to_view(current_expense_cats)
        # If the result is 1, return to the previous menu.
        if cat_to_view == 1:
            return

        # Gets the expenses in that category.
        expense_info = expenses_db.get_expenses_from_category(cat_to_view)

        # If the category list is empty.
        if len(expense_info) == 0:
            print("\nYou haven't added any expenses to this category.")
            continue
        # If get_all_expenses() has returned an error.
        if expense_info[0] == 1:
            print("\nSorry, something went wrong accessing the expenses database.")
            print(f"Error: {expense_info[1]}")
            return
        break

    # Tells the user what's happening.
    print(f"\nViewing expenses in the {cat_to_view.capitalize()} category:\n")

    # Prints all the expenses.
    print("Name -- Category -- Amount -- Date Added")
    for expense in expense_info:
        print(f"{expense[1].capitalize()} -- {expense[0].capitalize()} -- {expense[2]} -- {expense[3]}")
    
    # Prints how many expenses have been added.
    if len(expense_info) == 1:
        print(f"\nThere is 1 expense in this category.")
    else:
        print(f"\nThere are {len(expense_info)} expenses in this category.")

# Adds a new expense category.
def add_category():
    # Get list of current expense categories.
    current_expense_cats = expenses_db.get_cat_list()
    # If the list is not empty.
    if len(current_expense_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_expense_cats[0] == 1:
            print("\nSorry, something went wrong accessing the expense categories database.")
            print(f"Error: {current_expense_cats[1]}")
            return

    # Tells the user what's happening.
    print("\nAdding a new expense category.")

    # If the list isn't empty, print the current categories.
    if len(current_expense_cats) != 0:
        print("\nThe current expense categories are:")
        for expense_cat in current_expense_cats:
            print(expense_cat.capitalize())

    # Get the name of the new expense category.
    new_expense_cat_name = expenses_utils.get_new_cat_name(current_expense_cats)
    # Returns to the previous menu if get_new_cat_name returns 1.
    if new_expense_cat_name == 1:
        return
    
    # Tells the user what's happening.
    print(f"\nAdding {new_expense_cat_name.capitalize()} to the database...")

    # Adds the expense category to the database.
    add_cat_result = expenses_db.add_expense_cat(new_expense_cat_name)
    # Handles unexpected behaviour of the function not returning a list/anything.
    if len(add_cat_result) == 0:
        print(f"\nAn unexpected error occurred while trying to add {new_expense_cat_name.capitalize()} to the database.")
        return
    
    # If successful, the first index of the result list is 0.
    if add_cat_result[0] == 0:
        print(f"\n{new_expense_cat_name.capitalize()} was successfully added to the database.")
        return
    # If unsuccessful, the first index will be 1.
    elif add_cat_result[0] == 1:
        print(f"\nSorry, something went wrong and {new_expense_cat_name.capitalize()} could not be added to the database.")
        print(f"Error: {add_cat_result[1]}")
        return
    # Handles behaviour if the result contains anything other than the expected conditions.
    else:
        print(f"\nAn unexpected error occurred while trying to add {new_expense_cat_name.capitalize()} to the database.")
        return

# Deletes an expense category.
def delete_category():
    # Get list of current expense categories.
    current_expense_cats = expenses_db.get_cat_list()
    # If the list is not empty.
    if len(current_expense_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_expense_cats[0] == 1:
            print("\nSorry, something went wrong accessing the expense categories database.")
            print(f"Error: {current_expense_cats[1]}")
            return

    # Tells the user what's happening.
    print("\nDeleting an expense category.")

    # If the list isn't empty, print the current categories.
    if len(current_expense_cats) != 0:
        print("\nThe current expense categories are:")
        for expense_cat in current_expense_cats:
            print(expense_cat.capitalize())

    # Get the name of the expense category to delete.
    expense_cat_to_delete = expenses_utils.get_cat_to_delete(current_expense_cats)
    # Returns to the previous menu if expense_cat_to_delete() returns 1.
    if expense_cat_to_delete == 1:
        return
    
    # Tells the user what's happening.
    print(f"\nDeleting {expense_cat_to_delete.capitalize()} from the database...")

    # Deletes the existing category from the database.
    delete_cat_result = expenses_db.delete_expense_cat(expense_cat_to_delete)
    # Handles unexpected behaviour of the function not returning a list/anything.
    if len(delete_cat_result) == 0:
        print(f"\nAn unexpected error occurred while trying to delete {expense_cat_to_delete.capitalize()} from the database.")
        return
    
    # If successful, the first index of the result list is 0.
    if delete_cat_result[0] == 0:
        print(f"\n{expense_cat_to_delete.capitalize()} was successfully deleted from the expense categories database.")
    # If unsuccessful, the first index will be 1.
    elif delete_cat_result[0] == 1:
        print(f"\nSorry, something went wrong and {expense_cat_to_delete.capitalize()} could not be deleted from the database.")
        print(f"Error: {delete_cat_result[1]}")
        return
    # Handles behaviour if the result contains anything other than the expected conditions.
    else:
        print(f"\nAn unexpected error occurred while trying to delete {expense_cat_to_delete.capitalize()} from the database.")
        return
    
    # Deletes the expenses associated with the category from the database.
    delete_expenses_result = expenses_db.delete_expenses(expense_cat_to_delete)
    # Handles unexpected behaviour of the function not returning a list/anything.
    if len(delete_expenses_result) == 0:
        print(f"\nAn unexpected error occurred while trying to delete expenses from the database.")
        return
    
    # If successful, the first index of the result list is 0.
    if delete_expenses_result[0] == 0:
        print(f"\nExpenses associated with {expense_cat_to_delete.capitalize()} were successfully deleted from the expense categories database.")
        return
    # If unsuccessful, the first index will be 1.
    elif delete_cat_result[0] == 1:
        print(f"\nSorry, something went wrong and the expenses could not be deleted from the database.")
        print(f"Error: {delete_cat_result[1]}")
        return
    # Handles behaviour if the result contains anything other than the expected conditions.
    else:
        print(f"\nAn unexpected error occurred while trying to delete expenses from the database.")
        return    