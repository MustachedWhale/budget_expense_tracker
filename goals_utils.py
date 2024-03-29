import income_db

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
    # If get_income_from_category() has returned an error.
    if category_income[0] == 1:
        print("\nSorry, something went wrong getting the category's income.")
        print(f"Error: {category_income[1]}")
        return 1
    return category_income