# Contains all the functions that interact with the income table in the db.

## Imports ##

import sqlite3
import os

## Functions ##

# Creates income database if it doesn't exist.
def create_income():
    try:
        db = sqlite3.connect('data/tracker')
    except sqlite3.OperationalError:
        os.mkdir('data')
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS income(
                        category TEXT,
                        name TEXT UNIQUE PRIMARY KEY,
                        amount TEXT,
                        date_added TEXT)''')
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()

    return [0, 0]

# Creates income_cats database if it doesn't exist.
def create_income_cats():    
    try:
        db = sqlite3.connect('data/tracker')
    except sqlite3.OperationalError:
        os.mkdir('data')
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS income_cats(name TEXT)')
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()

    return [0, 0]

# Gets a list of categories.
def get_cat_list():
    cat_list = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT name
                          FROM income_cats''')
        for row in cursor:
            for category in row:
                cat_list.append(category)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return cat_list

# Gets a list of income names.
def get_name_list():
    name_list = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT name
                          FROM income''')
        for row in cursor:
            for name in row:
                name_list.append(name)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return name_list
        
# Gets specific income data.
def get_income(search_term):
    income_info = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM income WHERE 
                       category = ? OR name = ? OR amount = ? OR date_added = ?''',
                       (search_term, search_term, search_term, search_term))
        for row in cursor:
            income_info.append(row)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return income_info

# Gets all income data.
def get_all_income():
    income_info = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM income')
        for row in cursor:
            income_info.append(row)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return income_info

# Gets income from a single category.
def get_income_from_category(category):
    income_info = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM income WHERE
                       category = ?''',
                       (category,))
        for row in cursor:
            income_info.append(row)
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return income_info    

# Adds an income.
def add_income(income_info):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO income
                       (category, name, amount, date_added)
                       VALUES(?, ?, ?, ?)''',
                       (income_info[0], income_info[1], income_info[2], income_info[3]))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Deletes an income.
def delete_income(name):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM income WHERE
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

# Updates the information of an income.
def update_income(updated_income_info, income_name):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''UPDATE income SET
                       category = ?, name = ?, amount = ?, date_added = ?
                       WHERE name = ?''',
                       (updated_income_info[0], updated_income_info[1], updated_income_info[2], updated_income_info[3], income_name))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Deletes income associated with a category.
def delete_income(category):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM income WHERE
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

# Adds a new income category.
def add_income_cat(name):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO income_cats(name)
                          VALUES(?)''', (name,))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Deletes an income category.
def delete_income_cat(name):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''DELETE FROM income_cats WHERE
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
