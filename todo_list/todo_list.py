from datetime import datetime
import os
import sqlite3
from tabulate import tabulate

# connection to db
con = sqlite3.connect(".//task.db")

# some cursor used in using the db
cur = con.cursor()

class Task():
    
    def display(self):

        # query result
        res = cur.execute(
            """SELECT COUNT(*) 
            FROM tasks"""
            ).fetchall()

        # display query result
        if res[0][0]==0:
            print("You have no tasks.")
        else:
            data = [[task_id, name, date] for task_id, name, date in cur.execute(
                """SELECT id, name, date 
                FROM tasks 
                ORDER BY date 
                DESC"""
                )]
            print(tabulate(
                data, 
                headers=["S/N", "Task Name", "Date Added"], 
                tablefmt="outline"
                ))
        print()

        print("type: a - add task, e - edit task, d - delete task, x - exit todo")
    
    # add task to db
    def add_task(self):
        name = input("Task Name: ")

        detail = (name, datetime.strftime(datetime.now(), "%m/%d/%Y"))

        if name:
            cur.execute(
                """INSERT INTO tasks 
                (name, date) 
                VALUES(?, ?)""", 
                detail
                )
            con.commit()
        
        os.system('cls||clear')

    # edit task in db
    def edit_task(self):
        task_no = int(input("Task S/N: "))
        task_nos = [task_id[0] for task_id in cur.execute("SELECT id FROM tasks")]

        if task_no in task_nos:
            new_name = input("New Task Name: ")

            detail = (new_name, task_no)

            cur.execute("""UPDATE tasks set name = ? WHERE id = ?""", detail)
            con.commit()

            os.system('cls||clear')
    
    # delete task from db
    def delete_task(self):
        task_no = int(input("Task S/N: "))
        task_nos = [task_id[0] for task_id in cur.execute("SELECT id FROM tasks")]

        if task_no in task_nos:
            print("Are you sure you want to delete this task?")
            print("y - yes, n - no")
            print()

            command = input(">> ")
            if command == "y":
                cur.execute("""DELETE FROM tasks WHERE id = ?""", str(task_no))
                con.commit()

                os.system('cls||clear')


def main():
    print("Todo List")
    print("----------")
    print()

    todo = Task()

    # program loop
    while True:
        todo.display()

        command = input(">> ")
        print()
        
        if command == "a":
            todo.add_task()
        elif command == "e":
            todo.edit_task()
        elif command == "d":
            todo.delete_task()
        elif command == "x":
            break


main()