import goals_db
import goals_utils
import income_db
import global_utils

# Contains all the menu functions for the goals section.

def main_menu():
    print("\nGoal Options")

    while True:
        user_input = input('''\nPlease select from one of the following options:
1 - Create a saving goal
2 - Create an income goal
3 - Edit a goal
4 - Delete a goal
5 - Add money to saving goal
6 - View all goals 
0 - Return to previous menu
: ''')

        # Creates a saving goal.
        if user_input == '1':
            create_saving_goal()

        # Creates an income goal.
        elif user_input == '2':
            create_income_goal()

        # Edits a goal.
        elif user_input == '3':
            edit_goal()

        # Deletes a goal.
        elif user_input == '4':
            delete_goal()

        # Adds money to a saving goal.
        elif user_input == '5':
            add_to_saving_goal()

        # Views all goals.
        elif user_input == '6':
            view_all_goals()

        # Return to previous menu.
        elif user_input == '0':
            return

# Creates a saving goal.
def create_saving_goal():
    # Get list of current saving goals.
    current_saving_goals = goals_db.get_goals_list('saving')
    # If the list is not empty (there might be no goals added).
    if len(current_saving_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_saving_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the saving goal names from the database.")
            print(f"Error: {current_saving_goals[1]}")
            return
    
    # Tells the user what's happening.
    print("\nAdding a new saving goal.")

    # If there are goals already in the database, print them out to the user.
    if len(current_saving_goals) != 0:
        print("\nCurrent Saving Goals:")
        print("Name -- Goal Amount -- Current Progress")
        for goal in current_saving_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")

    new_goal_info = []

    # Gets the name of the new goal.
    new_goal_name = goals_utils.get_new_saving_goal_name(current_saving_goals)
    # If the result is 1, return to the previous menu.
    if new_goal_name == 1:
        return
    else:
        new_goal_info.append(new_goal_name)

    # Adds the category of goal to new_goal_info.
    new_goal_info.append('saving')

    # Gets the amount of the new goal.
    new_goal_amount = goals_utils.get_new_goal_amount()
    # If the result is 1, return to the previous menu.
    if new_goal_amount == 1:
        return
    else:
        new_goal_info.append(new_goal_amount)

    # Adds 0.0 to the progress index of the saving goal.
    new_goal_info.append(0.0)

    # Adds the new income to the tracker.
    add_new_goal_result = goals_db.add_goal(new_goal_info)
    if add_new_goal_result[0] == 1:
        print("\nSorry, something went wrong adding the goal to the database.")
        print(f"Error: {add_new_goal_result[1]}")
        return
    elif add_new_goal_result[0] == 0:
        print(f"\n{global_utils.name_capitalise(new_goal_info[0])} was successfully added to the database.")
        return
    else:
        print("\nSorry, an unexpected error has occurred and the goal could not be added to the database.")    

# Creates an income goal.
def create_income_goal():
    # Get list of current income goals.
    current_income_goals = goals_db.get_goals_list('income')
    # If the list is not empty (there might be no goals added).
    if len(current_income_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_income_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the income goals from the database.")
            print(f"Error: {current_income_goals[1]}")
            return
    
    # Get list of current income categories.
    current_income_cats = income_db.get_cat_list()
    # If the list is not empty (there might be no categories added).
    if len(current_income_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_income_cats[0] == 1:
            print("\nSorry, something went wrong accessing the income categories database.")
            print(f"Error: {current_income_cats[1]}")
            return
    
    # Tells the user what's happening.
    print("\nAdding a new income goal.")

    # If there are goals already in the database, print them out to the user.
    if len(current_income_goals) != 0:
        print("\nCurrent Income Goals:")
        print("Category -- Target Income -- Current Progress")
        for goal in current_income_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")

    # If the list isn't empty, print the current categories.
    if len(current_income_cats) != 0:
        print("\nThe current income categories are:")
        for income_cat in current_income_cats:
            print(global_utils.name_capitalise(income_cat))

    new_goal_info = []

    # Gets the name of the category to add the goal to.
    cat_name = goals_utils.get_cat_name(current_income_cats)
    # If the result is 1, return to the previous menu.
    if cat_name == 1:
        return
    else:
        new_goal_info.append(cat_name)

    # Adds the category of goal to new_goal_info.
    new_goal_info.append('income')

    # Gets the amount of the new goal.
    new_goal_amount = goals_utils.get_new_goal_amount()
    # If the result is 1, return to the previous menu.
    if new_goal_amount == 1:
        return
    else:
        new_goal_info.append(new_goal_amount)

    # Gets the total income of a category.
    new_goal_progress = goals_utils.get_income_of_category(cat_name)
    if new_goal_progress == 1:
        return
    new_goal_info.append(new_goal_progress)

    # Adds the new income to the tracker.
    add_new_goal_result = goals_db.add_goal(new_goal_info)
    if add_new_goal_result[0] == 1:
        print("\nSorry, something went wrong adding the goal to the database.")
        print(f"Error: {add_new_goal_result[1]}")
        return
    elif add_new_goal_result[0] == 0:
        print(f"\nAn income goal for {global_utils.name_capitalise(new_goal_info[0])} was successfully added to the database.")
        return
    else:
        print("\nSorry, an unexpected error has occurred and the goal could not be added to the database.") 

# Edits a goal.
def edit_goal():
    pass

# Deletes a goal.
def delete_goal():
    # Get list of current saving goals.
    current_saving_goals = goals_db.get_goals_list('saving')
    # If the list is not empty (there might be no goals added).
    if len(current_saving_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_saving_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the saving goal names from the database.")
            print(f"Error: {current_saving_goals[1]}")
            return
        
    # Get list of current income goals.
    current_income_goals = goals_db.get_goals_list('income')
    # If the list is not empty (there might be no goals added).
    if len(current_income_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_income_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the income goal names from the database.")
            print(f"Error: {current_income_goals[1]}")
            return
        
    # If neither list has any goals, tell the user and return.
    if len(current_income_goals) == 0 and len(current_saving_goals) == 0:
        print("\nYou don't have any goals to delete.")
        return
    
    print("\nCurrent Saving Goals:")
    # If there are goals already in the database, print them out to the user.
    if len(current_saving_goals) != 0:
        print("Name -- Goal Amount -- Current Progress")
        for goal in current_saving_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")
    # Otherwise, tell the user.
    else:
        print("No saving goals present.")

    print("\nCurrent Income Goals:")
    # If there are goals already in the database, print them out to the user.
    if len(current_income_goals) != 0:
        print("Category -- Current Income -- Current Progress")
        for goal in current_income_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")
    # Otherwise, tell the user.
    else:
        print("No income goals present.")

    # Get the name and category of the goal to delete.
    goal_to_delete = goals_utils.get_goal_to_delete(current_income_goals, current_saving_goals)
    # Returns to the previous menu if goal_to_delete returns 1.
    if goal_to_delete == 1:
        return
    
    # Tells the user what's happening.
    print(f"\nDeleting {global_utils.name_capitalise(goal_to_delete[0])} from the database...")

    # Deletes the existing goal from the database.
    delete_goal_result = goals_db.delete_goal(goal_to_delete[0], goal_to_delete[1])
    # Handles unexpected behaviour of the function not returning a list/anything.
    if len(delete_goal_result) == 0:
        print(f"\nAn unexpected error occurred while trying to delete {global_utils.name_capitalise(goal_to_delete[0])} from the database.")
        return
    
    # If successful, the first index of the result list is 0.
    if delete_goal_result[0] == 0:
        print(f"\n{global_utils.name_capitalise(goal_to_delete[0])} was successfully deleted from the database.")
    # If unsuccessful, the first index will be 1.
    elif delete_goal_result[0] == 1:
        print(f"\nSorry, something went wrong and {global_utils.name_capitalise(goal_to_delete[0])} could not be deleted from the database.")
        print(f"Error: {delete_goal_result[1]}")
        return
    # Handles behaviour if the result contains anything other than the expected conditions.
    else:
        print(f"\nAn unexpected error occurred while trying to delete {global_utils.name_capitalise(goal_to_delete[0])} from the database.")
        return
    

# Adds money to a saving goal.
def add_to_saving_goal():
    pass

# Views all goals.
def view_all_goals():
    # Get list of current saving goals.
    current_saving_goals = goals_db.get_goals_list('saving')
    # If the list is not empty (there might be no goals added).
    if len(current_saving_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_saving_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the saving goal names from the database.")
            print(f"Error: {current_saving_goals[1]}")
            return
        
    # Get list of current income goals.
    current_income_goals = goals_db.get_goals_list('income')
    # If the list is not empty (there might be no goals added).
    if len(current_income_goals) != 0:
        # If the get_goals_list() function has returned an error.
        if current_income_goals[0] == 1:
            print("\nSorry, something went wrong retrieving the income goal names from the database.")
            print(f"Error: {current_income_goals[1]}")
            return
        
    # If neither list has any goals, tell the user and return.
    if len(current_income_goals) == 0 and len(current_saving_goals) == 0:
        print("\nYou don't have any goals to view.")
        return
    
    print("\nCurrent Saving Goals:")
    # If there are goals already in the database, print them out to the user.
    if len(current_saving_goals) != 0:
        print("Name -- Goal Amount -- Current Progress")
        for goal in current_saving_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")
    # Otherwise, tell the user.
    else:
        print("No saving goals present.")

    print("\nCurrent Income Goals:")
    # If there are goals already in the database, print them out to the user.
    if len(current_income_goals) != 0:
        print("Category -- Current Income -- Current Progress")
        for goal in current_income_goals:
            print(f"{global_utils.name_capitalise(goal[0])} -- {global_utils.amount_format(goal[2])} -- {global_utils.amount_format(goal[3])}")
    # Otherwise, tell the user.
    else:
        print("No income goals present.")