#=====importing libraries===========

from datetime import date, datetime

#====Function Section====

#-----------------reg_user function that is called when the user selects ‘r’ to register a new user---------------#
def reg_user(): 
    while True:
        new_username = input("\nUsername to add: ")

# make sure that you don’t duplicate usernames when you add a new user to user.txt
        if new_username in user_dict:
            print("Username already exists. Please try again.")
            continue

        new_password = input("Password to add: ")
        password_confirm = input("Confirm password: ")

# then if username is new, check passwords match
        if new_password != password_confirm:
            print("Passwords don't match.")

# if input is valid, append new user to user.txt
        else:
            users = open('user.txt', 'a+', encoding='utf-8')
            users.write(new_username + ", " + new_password + "\n")
            users.close()
            print("New user added.")
            return

#---------------add_task function that is called when a user selects ‘a’ to add a new task to tasks.txt----------#
def add_task():
    from datetime import date, datetime # this isn't accessing the global function and can't work out why, had 1:1 and mentor couldn't either
# new list to hold the task details
    new_task = []
# collect new information and append to the list
# add error handling in case of error in task list?
    task_user = input("Please assign the new task to a user. Enter username: ")  # need error check that user exists?
    new_task.append(task_user)
    task_title = input("What is the title of the task? ")
    new_task.append(task_title)
    description = input("Please describe the task: ") 
    new_task.append(description)
    today = date.today()	
    date = today.strftime("%d %b %Y")
    new_task.append(date)
# run error handling for date input
    while True:
        due_date = input("What is the task due date? (in DD/MM/YY) ")
        try:    
            due_date = datetime.strptime(due_date, "%d/%m/%y")
            due_date = due_date.strftime("%d %b %Y")
            break
        except Exception:
            print("Oops! That was not a valid date input, try again using DD/MM/YYYY")
    new_task.append(due_date)
    new_task.append("No\n")
    new_task = ", ".join(new_task)

# add the new task to the file
    tasks = open("tasks.txt", "a")
    tasks.write(new_task)
    tasks.close()
    print("Task added.")

#---------------view_all function that is called when users type ‘va’ to view all the tasks listed in ‘tasks.txt’-------------#
def view_all():
    tasks_read = open("tasks.txt", "r")
    tasks = tasks_read.readlines()
    for pos, line in enumerate(tasks, 1):
        split_tasks = line.split(", ")
        output = f"─────────[{pos}]─────────────\n"
        output += "\n"
        output += f"Assigned to \t\t{split_tasks[0]}\n"
        output += f"Task:\t\t\t{split_tasks[1]}\n"
        output += f"Description:\t\t{split_tasks[2]}\n"
        output += f"Assigned Date:\t\t{split_tasks[3]}\n"
        output += f"Due Date:\t\t{split_tasks[4]}\n"
        output += f"Is completed:\t\t{split_tasks[5]}\n"
        output += "\n"
        print(output)
    tasks_read.close()

#--------------view_mine function that is called when users type ‘vm’ to view all the tasks that have been assigned to them.-----------#
def view_mine():
    tasks_read = open("tasks.txt", "r")
    tasks = tasks_read.readlines()

# create a new list to hold user tasks- only add tasks with matching username
    user_task_list = []
    for line in tasks:
        split_tasks = line.split(", ")
        if username == split_tasks[0]:
            new_tasks = ", ".join(split_tasks)
            user_task_list.append(new_tasks)

# print and label user tasks, so user can choose one to edit
    for pos, line in enumerate(user_task_list, 1):
        split_tasks = line.split(", ")
        output = f"─────────[{pos}]─────────────\n"
        output += "\n"
        output += f"Assigned to \t\t{split_tasks[0]}\n"
        output += f"Task:\t\t\t{split_tasks[1]}\n"
        output += f"Description:\t\t{split_tasks[2]}\n"
        output += f"Assigned Date:\t\t{split_tasks[3]}\n"
        output += f"Due Date:\t\t{split_tasks[4]}\n"
        output += f"Is completed:\t\t{split_tasks[5]}\n"
        output += "\n"
        print(output)

# Allow the user to select either a specific task to edit (by entering a number) or input ‘-1’ to return to the main menu.
    while True:
        index_choice = int(input("Please select a task number to edit, or type -1 to return to the main menu: "))
        print(f"You have chosen to edit task {index_choice}")
        if index_choice == -1:
            break

        elif index_choice == 0 or index_choice <= -2 or index_choice > len(user_task_list):
            print("You have selected an invalid option, please try again.")
            continue

        elif index_choice > 0 and index_choice <= len(user_task_list):
# variable holds the line for the task they want to edit
            edited_task = user_task_list[index_choice -1]    

# If the user selects a specific task, they should be able to choose to either mark the task as complete or edit the task. 
# If edit a task, the username of the person to whom the task is assigned or the due date of the task can be edited. 

        output = "─────────[SELECT AN OPTION]─────────────\n"
        output += "1- Edit user that task is assigned to \n"
        output += "2- Edit due date \n"
        output += "3- Mark as completed \n"
        output += "──────────────────────────\n"

        editing_choice = int(input(output))

# error message if choice is out of range
        if editing_choice <= 0 or editing_choice >=4:
            print("You have selected an invalid option, please try again.")
            continue

# change who the task is assigned to
        elif editing_choice == 1: 
            split_edited_task = edited_task.split(", ")

# The task can only be edited if it has not yet been completed.
            if split_edited_task[5] == "Yes\n":
                print("This task has already been completed and cannot be changed.")
                continue

            else:
                new_user = input("Which user would you like to assign this to? ") # need error check user exists

# new list to hold updated task list- cycle through tasks to append and rebuild correctly
                updated_tasks = []
                for line in tasks:
                    split_tasks = line.split(", ")

# need to swap in the new user to the correct line in the original task list- do check to find the matching line
                    if split_tasks[0] == username: 
                        if split_tasks[1] == split_edited_task[1] and split_tasks[2] == split_edited_task[2]: # I think this is enough of a check?
                            split_tasks[0] = new_user
                            joined_tasks = ", ".join(split_tasks)
                            updated_tasks.append(joined_tasks)
                        else:
                            joined_tasks = ", ".join(split_tasks)
                            updated_tasks.append(joined_tasks)

                    else:
                        joined_tasks = ", ".join(split_tasks)
                        updated_tasks.append(joined_tasks)
                 
# write the updated tasks in tasks.txt
            tasks_write = open("tasks.txt", "w")
            for line in updated_tasks:  
                tasks_write.write(line)
            print("User task is assigned to is updated.")
            break

# change the task due date
        elif editing_choice == 2: 
            split_edited_task = edited_task.split(", ")

# The task can only be edited if it has not yet been completed.
            if split_edited_task[5] == "Yes\n":
                print("This task has already been completed and cannot be changed.")
                continue

            else:
                while True:
# error handling for due date input
                    new_due_date = input("What is the task due date? (in DD/MM/YYYY) ")
                    try:    
                        new_due_date = datetime.strptime(new_due_date, "%m/%d/%y")
                        new_due_date = new_due_date.strftime("%d %b %Y")
                        break
                    except Exception:
                        print("Oops! That was not a valid date input, try again using DD/MM/YYYY")

# new list to hold updated task list- cycle through tasks to append and rebuild correctly
                updated_tasks = []
                for line in tasks:
                    split_tasks = line.split(", ")

# need to swap in this new user to the correct line in the original task list- do check to find the matching line
                    if split_tasks[0] == username: 
                        if split_tasks[1] == split_edited_task[1] and split_tasks[2] == split_edited_task[2]: # enough of a check?
                            split_tasks[4] = new_due_date
                            joined_tasks = ", ".join(split_tasks)
                            updated_tasks.append(joined_tasks)

                        else:
                            joined_tasks = ", ".join(split_tasks)
                            updated_tasks.append(joined_tasks)

                    else:
                        joined_tasks = ", ".join(split_tasks)
                        updated_tasks.append(joined_tasks)
                 
# write the updated tasks in tasks.txt
            tasks_write = open("tasks.txt", "w")
            for line in updated_tasks:  
                tasks_write.write(line)
            print("Task due date updated.")
            break

# mark task complete
        elif editing_choice == 3:             
            split_edited_task = edited_task.split(", ")

# The task can only be edited if it has not yet been completed.
            if split_edited_task[5] == "Yes\n":
                print("This task has already been completed")
                continue

            else:
# new list to hold updated task list- cycle through tasks to append and rebuild correctly
                updated_tasks = []
                for line in tasks:
                    split_tasks = line.split(", ")

# need to update task complete to the correct line in the original task list- do check to find the matching line
                    if split_tasks[0] == username: 
                        if split_tasks[1] == split_edited_task[1] and split_tasks[2] == split_edited_task[2]: # enough of a check?
                            split_tasks[5] = "Yes\n"
                            joined_tasks = ", ".join(split_tasks)
                            updated_tasks.append(joined_tasks)

                        else:
                            joined_tasks = ", ".join(split_tasks)
                            updated_tasks.append(joined_tasks)

                    else:
                        joined_tasks = ", ".join(split_tasks)
                        updated_tasks.append(joined_tasks)

# write the updated tasks in tasks.txt
            tasks_write = open("tasks.txt", "w")
            for line in updated_tasks:  
                tasks_write.write(line)
            print("Task updated to complete.")
            break

#-----------gen_task_overview function that is called when users type ‘gr’ to create and view reports-----------#
def gen_task_overview():

    tasks_read = open("tasks.txt", "r")
    tasks = tasks_read.readlines()

# create variables to count information for the report
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

# loop through the tasks to count task information
    for line in tasks:
        total_tasks += 1

# format the data ready for the for loop
        split_tasks = line.split(", ")
        today = datetime.today()
        today_date = today.strftime("%d %b %Y")

# count complete and incomplete tasks
        if split_tasks[5].strip("\n") == "Yes":
            completed_tasks += 1
        elif split_tasks[5].strip("\n") == "No":
            uncompleted_tasks += 1

        due = datetime.strptime(split_tasks[4], "%d %b %Y")
        if due.date() < today.date() and split_tasks[5].strip("\n") == "No":
            overdue_tasks += 1

    tasks_read.close()

# create a report
    task_report = []
    task_report.append("\t\t─────────[TASK REPORT]─────────────\n")

    total_tracked = f"Total number of tasks generated and tracked using task_manager.py:\t{total_tasks}"
    task_report.append(total_tracked)

    total_complete = f"Total number of completed tasks:\t\t\t\t\t{completed_tasks}"
    task_report.append(total_complete)

    total_uncomplete = f"Total number of uncompleted tasks:\t\t\t\t\t{uncompleted_tasks}"
    task_report.append(total_uncomplete)

    total_overdue = f"Total number of overdue tasks:\t\t\t\t\t\t{overdue_tasks}"
    task_report.append(total_overdue)

    perc_incomplete = f"Percentage of tasks that are incomplete:\t\t\t\t{round(int((uncompleted_tasks / total_tasks) * 100))}%"
    task_report.append(perc_incomplete)

    perc_overdue = f"Percentage of tasks that are overdue:\t\t\t\t\t{round(int((overdue_tasks / total_tasks) * 100))}%\n"
    task_report.append(perc_overdue)

# write the report to a new file
    task_report = "\n".join(task_report)
    tasks_overview = open("task_overview.txt", "w", encoding = "utf-8")
    tasks_overview.write(task_report)
    tasks_overview.close()

# print the report from the file
    tasks = open("task_overview.txt", "r", encoding = "utf-8")
    tasks_overview = tasks.readlines()

    for line in tasks_overview:
        print(line.strip("\n")) # why is this not removing the \n to print here?
    tasks.close()
    print()

#-----------gen_user_overview function that is called when users type ‘gr’ to create and view reports-----------#
def gen_user_overview():
    user_read = open("user.txt", "r")
    users = user_read.readlines()
    tasks_read = open("tasks.txt", "r")
    tasks = tasks_read.readlines()

# create variables to count information for the report
    total_users = 0
    total_tasks = 0

# count the total number of users registered with task_manager.py.
    for line in users:
        total_users += 1

# count the total number of tasks that have been generated and tracked using task_manager.py.
    for line in tasks:
        total_tasks += 1

# create a list of users to work from 
    user_list = []
    for line in users:
        split_users = line.split(", ")
        user_list.append(split_users[0])

# Dictionary to count the total number of tasks assigned to each user
    user_task_dict = {}
    for line in tasks:
        split_tasks = line.split(", ")
        if split_tasks[0] in user_task_dict:
            user_task_dict[split_tasks[0]] += 1
        else:
            user_task_dict[split_tasks[0]] = 1

# create a zero value tuple for any users with no tasks
    for i in user_list:
        if i in user_task_dict:
            continue
        else:
            user_task_dict[i] = 0

# Dictionary to count completed tasks for the percentage of the tasks assigned to that user that have been completed
    complete_task_dict = {}
    for line in tasks:
        split_tasks = line.split(", ")
        if split_tasks[0] and split_tasks[5].strip("\n") == "Yes":
            if split_tasks[0] in complete_task_dict:
                complete_task_dict[split_tasks[0]] += 1
            else:
                complete_task_dict[split_tasks[0]] = 1

# create a zero value tuple for any users with no tasks
    for i in user_list:
        if i in complete_task_dict:
            continue
        else:
            complete_task_dict[i] = 0

# Dictionary to count uncompleted tasks for the percentage of the tasks assigned to that user that must still be completed
    uncomplete_task_dict = {}
    for line in tasks:
        split_tasks = line.split(", ")
        if split_tasks[0] and split_tasks[5].strip("\n") == "No":
            if split_tasks[0] in uncomplete_task_dict:
                uncomplete_task_dict[split_tasks[0]] += 1
            else:
                uncomplete_task_dict[split_tasks[0]] = 1

# create a zero value tuple for any users with no tasks
    for i in user_list:
        if i in uncomplete_task_dict:
            continue
        else:
            uncomplete_task_dict[i] = 0

# Dictionary to count overdue tasks for the percentage of the tasks assigned to that user that have not yet been completed and are overdue
    overdue_task_dict = {}
    today = datetime.today()
    today_date = today.strftime("%d %b %Y")
    for line in tasks:
        # print(line)
        split_tasks = line.split(", ")
        due = datetime.strptime(split_tasks[4], "%d %b %Y")
        if due.date() < today.date() and split_tasks[5].strip("\n") == "No":
            if split_tasks[0] in overdue_task_dict:
                overdue_task_dict[split_tasks[0]] += 1
            else:
                overdue_task_dict[split_tasks[0]] = 1

# create a zero value tuple for any users with no tasks
    for i in user_list:
        if i in overdue_task_dict:
            continue
        else:
            overdue_task_dict[i] = 0

# create a report to hold the user information
    user_report = []
    user_report.append("\t\t─────────[USER REPORT]─────────────\n")

    total_users_registered = (f"the total users registered with task_manager are: {total_users}") # append straight to it?
    user_report.append(total_users_registered)

    total_tasks_tracked = (f"the total tasks registered with task_manager are: {total_tasks}\n")
    user_report.append(total_tasks_tracked)

# collect desired informatin and append it to the new report list
    for x in user_task_dict:
        user_tasks = (f"Username {x} has:\t\tbeen assigned {user_task_dict[x]} tasks")  
        user_report.append(user_tasks)

# with zero division error check for those with 0 tasks
        try:
            perc_tasks = (f"\t\t\t\tbeen assigned {round((user_task_dict[x] / total_tasks) * 100)}% of the total tasks")
            user_report.append(perc_tasks)
        except ZeroDivisionError:
            perc_tasks = (f"\t\t\t\tbeen assigned 0% of the total tasks")
            user_report.append(perc_tasks)  

        try:
            complete_tasks = (f"\t\t\t\t{round((complete_task_dict[x] / user_task_dict[x]) * 100)}% of their tasks complete")
            user_report.append(complete_tasks)
        except ZeroDivisionError:
            complete_tasks = (f"\t\t\t\tno tasks assigned to complete")
            user_report.append(complete_tasks)

        try:
            uncomplete_tasks = (f"\t\t\t\t{round((uncomplete_task_dict[x] / user_task_dict[x]) * 100)}% of their tasks still to complete")
            user_report.append(uncomplete_tasks)
        except ZeroDivisionError:
            uncomplete_tasks = (f"\t\t\t\tno tasks assigned to have uncomplete")
            user_report.append(uncomplete_tasks)

        try:
            overdue_tasks = (f"\t\t\t\t{round((overdue_task_dict[x] / user_task_dict[x]) * 100)}% of their tasks overdue\n")
            user_report.append(overdue_tasks)
        except ZeroDivisionError:
            overdue_tasks = (f"\t\t\t\tno tasks assigned to have overdue\n")
            user_report.append(overdue_tasks) 

# write the report to a new file
    user_report = "\n".join(user_report)
    user_overview = open("user_overview.txt", "w", encoding = "utf-8")
    user_overview.write(user_report)
    user_overview.close()

# print the report from the file
    users = open("user_overview.txt", "r", encoding = "utf-8")
    user_report = users.readlines()

    for line in user_report:
        print(line.strip("\n"))
    users.close()
    print()

#-----------display_stats function that is called when users type ‘ds’ to print reports-----------#
def display_stats():
# first call task_overview.txt to print
    try:
        tasks = open("task_overview.txt", "r", encoding = "utf-8")
        tasks_overview = tasks.readlines()

        for line in tasks_overview:
            print(line.strip("\n"))
        tasks.close()
        print()

# If these text files don’t exist (because the user hasn’t selected to generate them yet), first call the code to generate the text files.
    except FileNotFoundError:
        gen_task_overview()

# then call task_overview.txt to print
    try:
        users = open("user_overview.txt", "r", encoding = "utf-8")
        user_report = users.readlines()

        for line in user_report:
            print(line.strip("\n"))
        users.close()
        print()

# If these text files don’t exist (because the user hasn’t selected to generate them yet), first call the code to generate the text files.
    except FileNotFoundError:
        gen_user_overview()

#====Login Section====

# loop back to log in at very end?

user_read = open("user.txt", "r")
users = user_read.readlines()

user_dict = {}

for detail in users:
    k, v = detail.split(", ")
    user_dict[k] = v.strip("\n")   

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    correct_pass = user_dict.get(username)
    if correct_pass == password:
        print(f"Welcome {username}. You are now logged in.\n")
        break
    else:
        print(f"Please try again")

user_read.close()

#====Menu Section====

# Have an option to generate reports to the main menu of the application for the admin
while True:
    if username == "admin":
        menu = input('''Select one of the options below:
        r - \tRegistering a user  
        a - \tAdding a task
        va - \tView all tasks
        vm - \tView my task
        gr - \tGenerate reports
        ds - \tDisplay statistics
        e - \tExit
        : ''').lower()
        print()
# why does removing \t move it forwards?
    else:
        menu = input('''Select one of the options below:
        r - \tRegistering a user
        a - \tAdding a task
        va - \tView all tasks
        vm - \tView my task
        e - \tExit
        : ''').lower()
        print()
 
 # menu choices calling functions
    while True:

# register user
        if menu == 'r': 
            reg_user()
            break

        elif menu == 'a':
            add_task()
            break

        elif menu == 'va':
            view_all()
            break 

        elif menu == 'vm':
            view_mine()
            break

# generate a report for tasks and users, split into 2 seperate functions
        elif menu == 'gr': 
            gen_task_overview()
            gen_user_overview()
            break 

# display statistics so that the reports generated are read from task_overview.txt and user_overview.txt and displayed
        elif menu =="ds":
            display_stats()
            break

# menu exit option
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

# error handling
        else:
            print("Option invalid, please try again.\n")
            break
# ADD RETURN TO LOG IN 
