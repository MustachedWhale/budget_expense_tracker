# Contains all the functions that interact with the goals table in the db.

## Imports ##

import sqlite3
import os

## Functions ##

# Creates database if it doesn't exist.
def create():
    try:
        db = sqlite3.connect('data/tracker')
    except sqlite3.OperationalError:
        os.mkdir('data')
    finally:
        db = sqlite3.connect('data/tracker')
    try:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS goals(
                        name TEXT UNIQUE PRIMARY KEY,
                        category TEXT,
                        amount FLOAT,
                        progress FLOAT)''')
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]

# Gets goals info based on the category.
def get_goals_list(category):
    income_info = []
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM goals WHERE
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

# Adds a goal.
def add_goal(goal_info):
    try:
        db = sqlite3.connect('data/tracker')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO goals
                       (name, category, amount, progress)
                       VALUES(?, ?, ?, ?)''',
                       (goal_info[0], goal_info[1], goal_info[2], goal_info[3]))
        db.commit()
    except Exception as e:
        db.rollback()
        db.close()
        return [1, e]
    finally:
        db.close()
    return [0, 0]