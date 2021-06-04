# Capstone-Project-III

## Task Manager

## Project Details:

### Description

This program is for a small business it can help it to manage tasks assigned to each member of the team.

### Functionality

This program works with four text files, user.txt, user_overview.txt, tasks.txt and task_overview.txt 

tasks.txt:
Stores a list of all the tasks that the team is working on.
The data for each task is stored on a separate line in the text file.

user.txt:
Stores the username and password for each user that has
permission to use your program (task_manager.py).

When the user chooses to generate reports, two text files, called
task_overview.txt and user_overview.txt are created.

Program on startup:

Login. The user is prompted to enter a username and
password. A list of valid usernames and passwords are stored in a
text file called user.txt. 
The user is repeatedly asked to enter a valid username and password until they provide
appropriate credentials.
A menu is displayed once the user has successfully logged in.

**Standard Account Menu:**
a - add task, 
vm - view my tasks, 
e - exit

**Admin Account Menu:**
r - register user, 
a - add task, 
va - view all tasks, 
vm - view my tasks, 
gr - generate reports, 
ds - display statistics, 
e - exit

**Data stored in each line(tasks.txt):**

The username of the person to whom the task is assigned.
The title of the task.
A description of the task.
The date that the task was assigned to the user.
The due date for the task.
Either a ‘Yes’ or ‘No’ value that specifies if the task has been
completed yet.

**Data stored in each line(user.txt):**

First, the username followed by a comma, a space and then
the password.
One username and corresponding password per line.

### How can I use it?

Firstly, you need to clone this repository with the Task Manager program and related text files 
to a local repository on your computer, so that you can access and run the program. If you need 
help, follow the instructions as set out github help webpage:

* https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository

You will also need to download the Python interpreter program onto your computer's operating system (OS) 
so that you can view and run the Task Manager code. The existing and generated text files can be viewed 
with a simple Notepad app which comes with Windows OS or you can download an appropriate Notepad app.

* https://www.python.org/downloads/ - Navigate here to download the appropriate Python interpreter for your OS (i.e. Windows, Mac, Linux)

* https://notepad-plus-plus.org/downloads/ - Navigate here to download Notepad for the text files if you don't already have it.

Once you have the Task Manager folder with all it's files on your computer and you have succesfully downloaded Python and/or 
Notepad, you need to open the IDLE file within the Python programs on your local machine that was downloaded automatically 
with Python. This is an Integrated Development Environment which allows you to view and run Python programs. When 
you open the IDLE file, a Python 'shell' window will appear. You can then click on the 'file' and 'open' tabs on 
the top toolbar to navigate to the 'taskmanager.py' python program file to open it. It will be displayed in another 
window separate to the shell window.

### Contributions

This program was created by me as my last level 1 Capstone Project for the sofware engineering bootcamp I'm enrolled in. 
This program has been reviewed and commented on by the Hyperion Development Sofware Engineering Bootcamp mentors.
