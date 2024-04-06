import income_db
import goals_db
import global_utils

# Gets the name of a new saving goal.
def get_new_saving_goal_name(current_saving_goals):
        while True:
            print('')
            name_input = input('''Please describe the goal. The name must be unique.
Enter 0 to return to the previous menu.
: ''').lower()
            if name_input == '0':
                return 1
            if name_input in current_saving_goals:
                print("\nThe income name you entered matches an existing name.")
                continue
            return name_input
        
# Gets the amount of a new goal.
def get_new_goal_amount():
    while True:
        print('')
        amount_input = input('''Please enter a target amount. Enter 0 to return to the previous menu.
: ''').lower()
        if amount_input == '0':
            return 1
        if len(amount_input[amount_input.rfind('.')+1:]) != 2:
            print("\nPlease enter a valid amount.")
            continue
        try:
            amount = float(amount_input)
        except ValueError:
            print("\nPlease enter a valid amount.")
            continue
        return amount

# Gets the name of an income category for a new goal.
def get_cat_name(current_income_cats):
    while True:
        print('')
        cat_input = input('''Please enter the name of the category you wish to add a goal to. Enter 0 to cancel.
: ''').lower()
        if cat_input == '0':
            return 1
        if cat_input in current_income_cats:
            return cat_input
        else:
            print("\nYou did not enter the name of a category.")

# Gets the total income of an income category.
def get_income_of_category(category):
    category_income = income_db.get_cat_income(category)
    if type(category_income) == float:
        return category_income
    # If get_income_from_category() has returned an error.
    if category_income[0] == 1:
        print("\nSorry, something went wrong getting the category's income.")
        print(f"Error: {category_income[1]}")
        return 1

# Gets the name of the goal to delete.
def get_goal_to_delete(income_goals, saving_goals):
    while True:
        print('')
        name_input = input('''Please enter the name of the goal you want to delete. Enter 0 to return to the previous menu.
: ''').lower()
        if name_input == '0':
            return 1
        income_count = 0
        saving_count = 0
        for goal in income_goals:
            if name_input == goal[0]:
                income_count += 1
        for goal in saving_goals:
            if name_input == goal[0]:
                saving_count += 1
        if income_count == 1 and saving_count == 0:
            return [name_input, 'income']
        elif income_count == 0 and saving_count == 1:
            return [name_input, 'saving']
        elif income_count == 1 and saving_count == 1:
            choice_result = choose_income_or_savings(name_input, income_goals, saving_goals)
            if choice_result == 'income' or choice_result == 'saving':
                return [name_input, choice_result]
            else:
                return 1
        else:
            print("\nYou did not enter the name of a goal.")

# Gets the choice if a goal is present in both the income and saving goals lists.
def choose_income_or_savings(name, income_goals, saving_goals):
    print(f"\n{global_utils.name_capitalise(name)} is present as both a saving goal and an income goal.")
    while True:
        choice_input = input('''Please enter 'saving' to select the saving goal, or 'income' to select the income goal.
Enter 0 to return to the previous menu.
: ''').lower()
        if choice_input == '0':
            return 1
        elif choice_input == 'saving':
            return 'saving'
        elif choice_input == 'income':
            return 'income'
        else:
            print('\nYour answer was not recognised.\n')

# Updates the income goals when income is updated.
def update_income_goals():
    # Get list of current income categories.
    current_income_cats = income_db.get_cat_list()
    # If the list is not empty (there might be no categories added).
    if len(current_income_cats) != 0:
        # If the get_cat_list() function has returned an error.
        if current_income_cats[0] == 1:
            print("\nSorry, something went wrong accessing the income categories database.")
            print(f"Error: {current_income_cats[1]}")
            return
    else:
        # Returns if there are no income categories.
        return

    for cat in current_income_cats:
        # Gets the goal info for a category if it exists.
        old_goal_info = goals_db.get_goal_info(cat)
        if len(old_goal_info) == 0:
            continue
        # Gets the total income for that category.
        cat_income = income_db.get_cat_income(cat)
        # Makes the tuple of old_goal_info into a list.
        new_goal_info = []
        for goal in old_goal_info:
            for item in goal:
                new_goal_info.append(item)
        # Removes the progress number from goal_info and adds on the new. updated number. 
        new_goal_info.pop()
        new_goal_info.append(cat_income)

        # Updates the goal in the database.
        update_goal_result = goals_db.update_goal(cat, new_goal_info)
        # If update_goal() has returned an error.
        if update_goal_result[0] == 1:
            print(f"\nSorry, something went wrong updating the {global_utils.name_capitalise(cat)} goal.")
            print(f"Error: {update_goal_result[1]}")
             