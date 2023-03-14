# =====importing libraries======
from datetime import date


# ====functions====
# function to format array into a defined layout
def print_tasks(tasks_list):
    for pos, line in enumerate(tasks_list, 1):
        split_task_parts = line.split(', ')

        output = f'----------------[{pos}]----------------\n'
        output += '\n'
        output += f'Task:\t\t\t\t{split_task_parts[0]}\n'
        output += f'Assigned to:\t\t{split_task_parts[1]}\n'
        output += f'Date Assigned:\t\t{split_task_parts[2]}\n'
        output += f'Due date:\t\t\t{split_task_parts[3]}\n'
        output += f'Task Complete?\t\t{split_task_parts[4]}\n'
        output += f'Task Description:\t{split_task_parts[5]}\n'
        output += '\n'
        output += '-----------------------------------\n'

        print(output)


# ====Login Section====
"""Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
"""
# Saves all users name and password in a dictionary
users_f = open('./user.txt', 'r+')
list_of_users = {}

for line in users_f:
    item_list = line.split(', ')
    name = item_list[0]
    password = item_list[1].replace('\n', '')
    list_of_users[name] = password

print(list_of_users)

# Login
# Setting variables to be used on the input block
need_name = True
need_password = True
name = ''
password = ''

# While loop to request inputs for name, password and error management
while need_name:
    print('Please, insert your name and password to login:')
    name = input('Name: ').lower()

    if name in list_of_users.keys():
        need_name = False
    else:
        print('Try again')

while need_password:
    password = input('Password: ').lower()
    if list_of_users[name] != password:
        print('Password incorrect')
        continue
    else:
        print('You are logged in\n')
    need_password = False

while True:
    # Presenting the menu to the admin user with access to register user and see stats.
    # Making sure that the user input is converted to lower case.
    if name == 'admin':
        menu = input('''Select one of the following Options below:
        r - Registering a user
        s - Statistics
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()
    # Presenting the menu to other users.
    else:
        menu = input('''
        Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()

    if menu == 'r':
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

        new_user = input('Please, create a user name: ')
        new_pass = input('Please, create your password: ')
        pass_confirmation = input('Please, confirm your password: ')

        # Checking passwords matches
        if new_pass != pass_confirmation:
            print("Your password confirmation doesn't match. Try again.")
            new_pass = input('Please, create your password: ')
            pass_confirmation = input('Please, confirm your password: ')
        else:  # Open users file, saving inputs and closing file with success message.
            users_add = open('./user.txt', 'a')
            users_add.write(new_user + ', ' + new_pass + '\n')
            users_add.close()
            print('Your user was registered with success!\n')

    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

        task_title = input("Insert the title of the task: ")
        task_username = input("Please, insert the username of the person whom the task is assigned to: ")
        today = date.today()  # Using datetime module
        current_date = str(today.strftime("%d/%m/%Y"))  # Converting the datetime to dd-mm-yy
        task_due_date = input("Insert the due date: ")
        task_status = 'No'
        task_description = input("Insert the task description: ")

        # Open tasks file, saving inputs and closing with success message.
        tasks_add = open('./tasks.txt', 'a')
        tasks_add.write(
            task_title + ', ' + task_username + ', ' + current_date + ', ' + task_due_date + ', ' + task_status + ', ' + task_description + '\n')
        tasks_add.close()
        print('Your task was registered with success!\n')

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

        # Open tasks file and reading lines.
        all_tasks = open('./tasks.txt', 'r')
        task_parts = all_tasks.readlines()

        print_tasks(task_parts)
        all_tasks.close()

    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

        all_tasks = open('./tasks.txt', 'r')

        for line in all_tasks:
            split_task_parts_2 = line.split(', ')
            my_tasks = []
            if split_task_parts_2[1] == name:  # Checking if name on the reading file is the same of the login
                my_tasks.append(line)  # Add into the empty list the matched task
            print_tasks(my_tasks)  # Using function to print the task lists in the requested format

        all_tasks.close()

    elif menu == 's':
        tasks_read = open('./tasks.txt', 'r')
        tasks_list = tasks_read.readlines()
        total_tasks = len(tasks_list)  # Calculates how many lines == tasks the tasks file has
        tasks_read.close()
        users_read = open('./user.txt', 'r')
        users_list = users_read.readlines()
        total_users = len(users_list)  # Calculates how many lines == users the user file has
        users_read.close()
        print(f'The total number of tasks is: {total_tasks} \nThe total number of users is: {total_users}\n')

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again.\n")
