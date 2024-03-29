# Contains all the functions that interact with the expenses table in the db.

## Imports ##

import sqlite3
import os

## Functions ##

# Creates expenses database if it doesn't exist.
def create_expenses():
    try:
        db = sqlite3.connect('data/tracker')
    except sqlite3.OperationalError:
        os.mkdir('data')
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS expenses(
                        category TEXT,
                        name TEXT UNIQUE PRIMARY KEY,
                        amount FLOAT,
                        date_added TEXT)''')
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()

    return [0, 0]

# Creates expense_cats database if it doesn't exist.
def create_expense_cats():    
    try:
        db = sqlite3.connect('data/tracker')
    except sqlite3.OperationalError:
        os.mkdir('data')
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS expense_cats(name TEXT, budget FLOAT)')
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()

    return [0, 0]

# Gets a list of category names.
def get_cat_names():
    cat_names = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('SELECT name FROM expense_cats')
        for row in cursor:
            for category in row:
                cat_names.append(category)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return cat_names

# Gets a list of categories.
def get_cat_list():
    cat_list = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM expense_cats')
        for row in cursor:
            cat_list.append(row)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return cat_list

# Gets a list of expense names.
def get_name_list():
    name_list = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT name
                          FROM expenses''')
        for row in cursor:
            for expense in row:
                name_list.append(expense)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return name_list
        
# Gets specific expense data.
def get_expense(search_term):
    expense_info = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM expenses WHERE 
                       category = ? OR name = ? OR amount = ? OR date_added = ?''',
                       (search_term, search_term, search_term, search_term))
        for row in cursor:
            expense_info.append(row)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return expense_info

# Gets all expense data.
def get_all_expenses():
    expense_info = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM expenses')
        for row in cursor:
            expense_info.append(row)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return expense_info

# Gets expenses from a single category.
def get_expenses_from_category(category):
    expense_info = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM expenses WHERE
                       category = ?''',
                       (category,))
        for row in cursor:
            expense_info.append(row)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return expense_info    

# Adds an expense.
def add_expense(expense_info):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO expenses
                       (category, name, amount, date_added)
                       VALUES(?, ?, ?, ?)''',
                       (expense_info[0], expense_info[1], expense_info[2], expense_info[3]))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Deletes an expense.
def delete_expense(name):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM expenses WHERE
                       name = ?''',
                       (name,))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Updates the information of an expense.
def update_expense(updated_expense_info, expense_name):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''UPDATE expenses SET
                       category = ?, name = ?, amount = ?, date_added = ?
                       WHERE name = ?''',
                       (updated_expense_info[0], updated_expense_info[1], updated_expense_info[2], updated_expense_info[3], expense_name))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Deletes expenses associated with a category.
def delete_expenses(category):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM expenses WHERE
                       category = ?''',
                       (category,))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Adds a new expense category.
def add_expense_cat(name, budget):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO expense_cats(name,budget)
                          VALUES(?, ?)''', (name, budget))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Updates the budget of an expense.
def update_cat_budget(name, new_budget):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''UPDATE expense_cats SET
                       budget = ? WHERE name = ?''',
                       (new_budget, name))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Deletes an expense category.
def delete_expense_cat(name):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM expense_cats WHERE
                       name = ?''',
                       (name,))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]
