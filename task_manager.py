import os
from datetime import datetime
import time

# initialise variables to be used during the program.
current_path = os.path.dirname(__file__)
delay_memu  = 3
delay_login_exit = 1
first_login = True

# Login System
# start/create function.
def login():
    print("Welcome to the Task Manager.")
    print("\nPlease login...\n")

    user_pass = False
    pass_pass = False

    # Loop until user account(username) is recognized.
    while not user_pass:
        user_name = input("Username: ")
        for x in range(0, len(users)):
            if users[x][0] == user_name:
                user_pass = True

                if user_pass:

                  # Loop intil correct password to the username is entered.
                  while not pass_pass:
                      password = input("Password: ")
                      if users[x][1] == password:
                          pass_pass = True

                          if not pass_pass:
                              print("\nPassword incorrect. Try again.")

        if not user_pass:
            print("\nUsername incorrect. Try again.")

        # if login successful.
        else:
            print("Logged in.")
            time.sleep(delay_login_exit)
            print("\nWelcome!")
            print("Enter \"-1\" at any time to return to the Main Menu")
            time.sleep(delay_login_exit+1)

    # Return the username to the variable
    return user_name


# 'r' menu choice.
def reg_user():
    user_unique = False
    verify_pass = False

    # Check if the current user is "admin". If not don't
    # give access to the function and print not authorised.
    if user_name == "admin":
        

        # Loop until the user enters an unique username
        while not user_unique:
            unique = True
            new_user = input("Username:\t\t")

            # Break and return to main menu if the user ever enters "-1"
            if new_user == "-1":
                break
            
            # Ensure the user enters something, otherwise loop back and let
            # them try again
            elif new_user == "":
                print("\nPlease enter a valid username...\n")
            
            # Check if the username already exists.
            else:
                for x in range(0, len(users)):
                    if users[x][0] == new_user:
                        print("\nThe username already exists. Please choose a different username.\n")
                        unique = False
                if unique:
                    user_unique = True

        if new_user == "-1":
            pass

        else:
            # Loop until the user correctly confirms the password.
            while not verify_pass:
                new_pass1 = input("Password:\t\t")
                if new_pass1 == "":
                    print("\nPlease enter a valid password.\n")
                elif new_pass1 == "-1":
                    break
                else:
                    new_pass2 = input("Confirm Password:\t")

                    if new_pass2 == "-1":
                        break

                    # If the usernames match print the new user details to screen
                    # and add the new user to the file
                    elif new_pass1 == new_pass2:
                        verify_pass = True
                        user.write(f"\n{new_user}, {new_pass1}")
                        print(f"\nNew user has been added\nUsername:\t{new_user}\nPassword:\t{new_pass1}")

                    else:
                        print("\nPasswords do not match. Please retry.\n")

        # Write the username and password to the file.\
        verify_pass = False

    else:
        print("\nYou are not authorised to register new users.")
    delay_menu = 2
    print(f"\nReturning to menu in {delay_menu} seconds...")
    time.sleep(delay_menu)


# 'a' menu choice.
def add_task():
    print("\nAdd Task\nPlease enter the details of new task")
    
    # Create the variables to save the data input from the user.
    info = []
    info_title = ["Username:\t", "Task Title:\t", "Description:\t", "Date Assigned:\t", "Due Date:\t", "Completed:\t"]
    skip = False

    # Loop through each input and save it in a list.
    for x in range(0, 6):
        while True:
            data = input(f"{info_title[x]}")
            
            # Make sure the user has entered valid data.
            if data == "":
                print("\nInvalid input. Please try again.\n")
            else:
                info.append(data)
                break
        
        
        # exit option
        if info[x] == "-1":
            skip = True
            break

    # Check if the user wishes to return to the menu.
    if not skip:

        # Write the task to the file.
        task.write(f"\n{info[0]}, {info[1]}, {info[2]}, {info[3]}, {info[4]}, {info[5]}")

        # Confirm the details by printing to the screen.
        print("\nNew task has been added")
        print("----------------------------------------------------")
        print("Username:\t" + info[0])
        print("Task Title:\t" + info[1])
        print("Description:\t" + info[2])
        print("Date Assigned:\t" + info[3])
        print("Due Date:\t" + info[4])
        print("Completed:\t" + info[5])
        print("----------------------------------------------------")

    print(f"\nReturning to menu in {delay_menu} seconds...")
    time.sleep(delay_menu)

# If the user inputs 'va' the details of all tasks
# for all users are printed to the screen.
def view_all():
    print("\nView All Tasks")

    # Loop through each line of the 'tasks' list and
    # print to the screen.
    for line in tasks:
        print("----------------------------------------------------")
        print("Username:\t" + line[0])
        print("Task Title:\t" + line[1])
        print("Description:\t" + line[2])
        print("Date Assigned:\t" + line[3])
        print("Due Date:\t" + line[4])
        print("Completed:\t" + line[5])
        print("----------------------------------------------------")
    delay_menu = 2
    print(f"\nReturning to menu in {delay_menu} seconds...")
    time.sleep(delay_menu)


# 'vm' menu choice.
def view_mine():
    user_found = False
    my_tasks = []
    user_name = ""
    print("\nView My Tasks")

    # Loop through all the tasks in the list and add the tasks
    # relating to the current user to the new "my_tasks" variable.
    for x in range(0, len(tasks)):
        if user_name == tasks[x][0]:
            my_tasks.append(tasks[x])
            user_found = True

    # If the user is found, print each task assigned to the current
    # user and add a task number to each task
    if user_found:
        for x in range(0, len(my_tasks)):
            print(f"\nTask {x+1}")
            print("----------------------------------------------------")
            print("Username:\t" + my_tasks[x][0])
            print("Task Title:\t" + my_tasks[x][1])
            print("Description:\t" + my_tasks[x][2])
            print("Date Assigned:\t" + my_tasks[x][3])
            print("Due Date:\t" + my_tasks[x][4])
            print("Completed:\t" + my_tasks[x][5])
            print("----------------------------------------------------")

        # Request the user to input the task they wish to edit and
        # loop until they choose a valid task number or enter "-1"
        # to return to the main menu.
        while True:
            # Add a try / except block in case the user doesn't enter
            # anything and presses enter. This would return an error
            # so we catch the error and break the loop instead, returning
            # to the main menu.
            try:
                task_num = int(input("Please enter a task number to edit: "))
                if task_num == -1:
                    break

                # Check that the task number is within the available tasks
                # per the file. This is to ensure we don't get any error.
                elif task_num > 0 and task_num <= len(my_tasks):
                    
                    # If the user enters a valid task number, we want to remove
                    # that task from the "tasks" list. This is because we are going
                    # to edit the task using "my_tasks" and then add the newly edited
                    # task back to "tasks" and print the entire list to the tasks.txt
                    # file again. This is easier than trying to edit the individual task
                    # in the "tasks" list.
                    for x in range(0, len(my_tasks)):
                        tasks.remove(my_tasks[x])

                    # Loop until the user enters a valid option
                    while True:
                        print("\nPlease choose an option")
                        print("m - mark task as complete\ne - edit the task")
                        menu_choice = input()

                        # If the user chooses "m", edit the Completed to "Yes".
                        # Not going to check whether it is already "Yes" since
                        # not changing any other variables based on this.
                        if menu_choice == "m":
                            my_tasks[task_num-1][5] = "Yes"
                            print(f"\nTask {task_num} has been marked as complete.")
                            break

                        # exit menu choice.
                        elif menu_choice == "-1":
                            break

                        # 'e' menu choice
                        elif menu_choice == "e":
                            if my_tasks[task_num-1][5] == "Yes":
                                print("\nThe task has been completed. Unable to edit.")
                                break
                            else:
                                print("\nPlease enter the new Username and Due Date (leave blank if no change required).")
                                user_name = input("Edit Username:\t")
                                due_date = input("Edit Due Date:\t")
                                
                                # Check if the users inputs are blank.
                                if user_name != "":
                                    my_tasks[task_num-1][0] = user_name
                                if due_date != "":
                                    my_tasks[task_num-1][4] = due_date

                                print("\nUpdated details")
                                print("Username:\t" + my_tasks[task_num-1][0])
                                print("Due Date:\t" + my_tasks[task_num-1][4])
                                break
                        
                        # Print input is not recognised
                        else:
                            print("\nUnrecognized input.")
                            time.sleep(delay_login_exit)

                    
                    # Write all the tasks back to the text file.
                    task.seek(0)
                    task.truncate(0)
                    for x in range(0, len(my_tasks)):
                        tasks.append(my_tasks[x])
                    for x in range(0, len(tasks)):
                        task.write(", ".join(tasks[x]))
                        if x != len(tasks)-1:
                            task.write("\n")
                    
                    break
                
                # Let the user know if the task entered does not exist.
                else:
                    print("\nThe selected task does not exist. Please try again.\n")
            except:
                print("\nNo task number entered. Please try again.\n")

                
    if not user_found:
        print("No tasks found for current user.")
    delay_menu = 2
    print(f"\nReturning to menu in {delay_menu} seconds...")
    time.sleep(delay_menu)

# 'ds' menu choice.
def display_statistics():
    
    # If the user is "admin" generate reports.
    if user_name == "admin":
        
        generate_reports()

        # Open generated report files.
        task_over_r = open(os.path.join(current_path, "task_overview.txt"), "r+")
        user_over_r = open(os.path.join(current_path, "user_overview.txt"), "r+")
        
        delay_menu = 2
        print(f"\nOpening task_overview.txt in {delay_menu} seconds...\n")
        time.sleep(delay_menu)

        for line in task_over_r:
            if "Total" in line or "Overdue Tasks" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t"))
            else:
                print(line.strip().replace("\t", "").replace(":", ":\t"))
        delay_menu = 2
        print(f"\nOpening user_overview.txt in {delay_menu} seconds...\n")
        time.sleep(delay_menu)

        for line in user_over_r:
            if "User:" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t\t"))
            elif "User Tasks" in line or "Overdue Tasks" in line:
                print(line.strip().replace("\t", "").replace(":", ":\t\t"))
            else:
                print(line.strip().replace("\t", "").replace(":", ":\t"))

    # Print you are not authorised.
    else:
        print("\nYou are not authorised to view statistics.\n")
    
    delay_menu = 2
    print(f"Returning to menu in {delay_menu} seconds...")
    time.sleep(delay_menu)

# If the user inputs 'gr' reports are generated with statistics
# about the tasks and each user. The logged in user must be "admin"
# to access this function.
def generate_reports():

    # Check if the logged in user is "admin"
    if user_name == "admin":

        # Open the files and set them to write. If the files don't exist they
        # will be created automatically.
        task_over_w = open(os.path.join(current_path, "task_overview.txt"), "w+")
        user_over_w = open(os.path.join(current_path, "user_overview.txt"), "w+")
        
        # initialise variables to be used.
        total_tasks = len(tasks)
        num_completed = 0
        num_incomplete = 0
        num_inc_overdue = 0
        per_incomplete = 0
        per_overdue = 0

        for x in range(0, len(tasks)):
            if tasks[x][5] == "Yes":
                num_completed += 1
            elif tasks[x][5] == "No":
                num_incomplete += 1

                # Convert the Due Date to a datetime object and compare
                # the current date to the due date.
                task_date = datetime.strptime(tasks[x][4], '%d %b %Y')
                if datetime.date(datetime.now()) < task_date.date():
                    num_inc_overdue += 1

        # Calculate statistics.
        if total_tasks == 0:
            per_incomplete = 0
            per_overdue = 0
        else:
            per_incomplete = round(100*num_incomplete/total_tasks)
            per_overdue = round(100*num_inc_overdue/total_tasks)

        # Write the statistics calculated above to the file.
        task_over_w.write("Task Overview - Statistics relating to all tasks in task_manager.py\n\n")
        task_over_w.write(f"Total Tasks:\t\t{total_tasks}\nCompleted Tasks:\t{num_completed}\nIncomplete Tasks:\t{num_incomplete}\nOverdue Tasks:\t\t{num_inc_overdue}\nPortion Incomplete:\t{per_incomplete}%\nPortion Overdue:\t{per_overdue}%")


        num_users = len(users)
        user_over_w.write("User Overview - Statistics relating to all users in task_manager.py\n\n")
        user_over_w.write(f"Total Users:\t\t{num_users}\n")
        user_over_w.write(f"Total Tasks:\t\t{total_tasks}")

        # Loop through each user and reset the variables
        for x in range(0, len(users)):
            num_tasks = 0
            num_completed = 0
            num_incomplete = 0
            num_inc_overdue = 0
            per_incomplete = 0
            per_overdue = 0
            per_completed = 0
            por_tasks = 0

            user_over_w.write("\n----------------------------------------------------\n")
            user_over_w.write(f"User:\t\t\t\t\t{users[x][0]}\n")

            # Loop through each task
            for y in range(0, len(tasks)):

                
                if users[x][0] == tasks[y][0]:
                    num_tasks +=1
                    if tasks[y][5] == "Yes":
                        num_completed += 1
                    elif tasks[y][5] == "No":
                        num_incomplete += 1
                        task_date = datetime.strptime(tasks[y][4], '%d %b %Y')
                        if datetime.date(datetime.now()) < task_date.date():
                            num_inc_overdue += 1
                            
            # Calculate statistics.
            if num_tasks == 0:
                per_incomplete = 0
                per_overdue = 0
                per_completed = 0
            else:
                per_incomplete = round(100*num_incomplete/num_tasks)
                per_overdue = round(100*num_inc_overdue/num_tasks)
                per_completed = round(100*num_completed/num_tasks)

            if total_tasks == 0:
                por_tasks = 0
            else:
                por_tasks = round(100*num_tasks/total_tasks)

            # Write the statistics calculated above to the file.
            user_over_w.write(f"User Tasks:\t\t\t\t{num_tasks}\nPortion Total Tasks:\t{por_tasks}%\nPortion Completed:\t\t{per_completed}%\nPortion Incomplete:\t\t{per_incomplete}%\nPortion Overdue:\t\t{per_overdue}%")
            user_over_w.write("\n----------------------------------------------------\n")
        
        # Close the files
        print("\nReports have been generated: task_overview.txt, user_overview.txt")
        task_over_w.close()
        user_over_w.close()

    # You are not authorised.
    else:
        print("\nYou are not authorised to generate reports.\n")


# This is the program loop which runs until the program is exited.
while True:

    # Open the text files and read the contents.
    user = open(os.path.join(current_path, "user.txt"), "r+")
    users = user.readlines()
    users = [x.strip().split(", ") for x in users]

    task = open(os.path.join(current_path, "tasks.txt"), "r+")
    tasks = task.readlines()
    tasks = [x.strip().split(", ") for x in tasks]

    if first_login:
        user_name = login()
        first_login = False    
    
    # menu options for admin and a normal user.
    if user_name == "admin":
        print("\nPlease select one of the following options:")
        print("r - register user\na - add task\nva - view all tasks\nvm - view my tasks\ngr - generate reports\nds - display statistics\ne - exit")
        menu = input("")
    else:
        print("\nPlease select one of the following options:")
        print("a - add task\nva - view all tasks\nvm - view my tasks\ne - exit")
        menu = input("")

    # Call the applicable function based on the users menu input.
    if menu == "r":
        reg_user()

    elif menu == "a":
        add_task()

    elif menu == "va":
        view_all()

    elif menu == "vm":
        view_mine()

    elif menu == "ds":
        display_statistics()

    elif menu == "gr":
        generate_reports()
        
        delay_menu = 2
        print(f"Returning to menu in {delay_menu} seconds...")
        time.sleep(delay_menu)

    # If the user inputs 'e' the main loop is stopped. 
    elif menu == "e":
        print("\nExiting...")
        time.sleep(delay_login_exit)
        break

    else:
        print("\nInvalid input. Try again.")
        time.sleep(delay_login_exit)

    # The files are closed to ensure all new data is written.
    user.close()
    task.close()
