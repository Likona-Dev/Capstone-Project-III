user_dict = {}
username_list = []
with open('user.txt', 'r+', encoding='utf-8') as ufile:
    for line in ufile:
        key, value = line.strip('\n').split(', ')
        user_dict[key] = value

        username = input("Enter username: ")

        if username in user_dict.keys():
            password = input("Enter password: ")

            while password != user_dict[username]:
                password = input("Wrong password, try again: ")

            else:
                menu = input("""\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
st - statistics
e - exit \n""")
                if menu == "r":
                    if username == "admin": # check if user has authority to register users.
                        new_user = input("Enter your new username: ")

                        while new_user in user_dict: # check if username is in 'user.txt' file
                            new_user = input("Username already exists, try again: ") # have user enter another username.

                        if new_user not in user_dict:
                            new_pass = input("Enter your new password: ")
                            pass_confirm = input("Enter password again to confirm: ")

                            while new_pass != pass_confirm: # check if passwords match, if not loop until passwords match.
                                print("\nPassword don't match!")
                                new_pass = input("Enter your new password: ") # ask user to enter new password
                                pass_confirm = input("Enter password again to confirm: ")

                            else:
                                with open('user.txt', 'a', encoding='utf-8') as afile:
                                    ufile.write('\n')
                                    ufile.write(new_user)
                                    ufile.write(', ')
                                    ufile.write(new_pass)
                                    print("User successfully registered.")

                    else:
                        print("You are not authorised to register users.")
                
                elif menu == "a":
                    task_info = []
                    labels = ["Username:\t", "Task: \t", "Date Assigned:\t", "Due Date:\t", "Task Complete:\t", "Description:\t"]
    
                    # make the range the number of items in 'labels' list.
                    for x in range(0, 6): 
                        while True:
                            data = input(f"{labels[x]}")

                            if data == "": # if user input is empty print error message.
                                print("\nInvalid input")

                            else:
                                task_info.append(data)
                                break
                                
                        tfile = open('tasks.txt', 'a', encoding='utf-8')
                        task_info = ', '.join(task_info)
                        tfile.write(task_info)        

                elif menu == "va":
                    if username == "admin":
                        tfile = open('tasks.txt', 'r', encoding='utf-8')
                        tasks = tfile.readlines()
                        tasks = [x.strip().split(", ") for x in tasks]

                         

                    

                        for line in (tasks):

                        
                    
                            print("----------------------------------------------------")
                            print("Username:     \t" + line[0])
                            print("Task Title:   \t" + line[1])
                            print("Description:  \t" + line[2])
                            print("Date Assigned:\t" + line[3])
                            print("Due Date:     \t" + line[4])
                            print("Completed:    \t" + line[5])
                            print("----------------------------------------------------")
                            tfile.close()
                    
                        

                    if username != "admin":
                        print("You are not authorised to register users.")
                        

                elif menu == "vm":
                    user_found = False
                    my_tasks = []
                    tfile = open('tasks.txt', 'r', encoding='utf-8')
                    tasks = tfile.readlines()
                    tasks = [x.strip().split(", ") for x in tasks]
                    for x in range(0, len(tasks)):
                        if username == tasks[x][0]:
                            my_tasks.append(tasks[x])
                            user_found = True

                        # If the user is found, print each task assigned to the current
                        # user and add a task number to each task
                        if user_found:
                            for x in range(0, len(my_tasks)):
                               
                                print("----------------------------------------------------")
                                print("Username:     \t" + my_tasks[x][0])
                                print("Task Title:   \t" + my_tasks[x][1])
                                print("Description:  \t" + my_tasks[x][2])
                                print("Date Assigned:\t" + my_tasks[x][3])
                                print("Due Date:     \t" + my_tasks[x][4])
                                print("Completed:    \t" + my_tasks[x][5])
                                print("----------------------------------------------------")
                                break

                elif menu == "st":
                    tfile = open('tasks.txt', 'r', encoding='utf-8')
                    tasks = tfile.readlines()
                    tasks = [x.strip().split(", ") for x in tasks]

                    # count number of users,tasks in task manager.
                    count1 = len(tasks)
                    count2 = len(user_dict)
                    print(f"The number of users is: {count2}, and the number of tasks is: {count1}")                    
                
                elif menu == "e":
                    break                
                                


        else:
            print("\nUsername not found.")
