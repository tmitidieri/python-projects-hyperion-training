# ===== importing libraries ======

from datetime import date, datetime
from os.path import exists


# ==== util functions ====

def print_tasks(tasks_list): # Format and print tasks
    for pos, line in enumerate(tasks_list, 1):
        split_task_parts = line.split(', ')

        output = f'---------------- [ {pos} ] ----------------\n'
        output += '\n'
        output += f'Task:\t\t\t{split_task_parts[0]}\n'
        output += f'Assigned to:\t\t{split_task_parts[1]}\n'
        output += f'Date Assigned:\t\t{split_task_parts[2]}\n'
        output += f'Due date:\t\t{split_task_parts[3]}\n'
        output += f'Task Complete?\t\t{split_task_parts[5]}'
        output += f'Task Description:\t{split_task_parts[4]}\n'

        print(output)

    print('---------------- [ END ] ----------------\n\n')


def print_and_append(array_to_append,item_to_append):
    print(item_to_append)
    array_to_append.append(item_to_append)


# ==== main functions ====

def view_menu():
    if name == 'admin':
        menu = input('''
------- [ SELECT AN OPTION ] -------
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    ds - display statistics
    e - Exit
    : \n''').lower()


    else:
        menu = input('''
------- [ SELECT AN OPTION ] -------
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : \n''').lower()


    if menu == 'r':
        pass
        reg_user()

    elif menu == 'a':
        pass
        add_task()

    elif menu == 'va':
        pass
        view_all()
        view_menu()

    elif menu == 'vm':
        pass
        view_mine()

    elif menu == 'gr':
        pass
        gen_reports()

    elif menu == 'ds':
        pass
        display_stats()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("Option Invalid, Please Try Again.\n")


def reg_user():
    new_user = input('Please, create a user name: ')
    new_pass = input('Please, create your password: ')
    pass_confirmation = input('Please, confirm your password: ')

    if new_pass != pass_confirmation: # Checking passwords matches
        print("Your password confirmation doesn't match. Try again.")
        new_pass = input('Please, create your password: ')
        pass_confirmation = input('Please, confirm your password: ')

    else:  # Open users file, saving inputs and closing file with success message.
        users_add = open('./user.txt', 'a')
        users_add.write(new_user + ', ' + new_pass + '\n')
        users_add.close()
        print('Your user was registered with success!\n')


def add_task():
    task_title = input("Insert the title of the task: ")
    task_username = input("Please, insert the username of the person whom the task is assigned to: ")
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")  # Format date to dd-mm-yyyy
    due_date = input("Insert the due date: ")
    task_status = 'No'
    task_description = input("Insert the task description: ")

    # Open tasks file, saving inputs and closing with success message.
    tasks_add_f = open('./tasks.txt', 'a')
    tasks_add_f.write(
        task_title + ', ' + task_username + ', ' + current_date + ', ' + due_date + ', ' + task_description + ', ' + task_status + '\n')
    tasks_add_f.close()
    print('Your task was registered with success!\n')


def view_all():
    all_tasks_f = open('./tasks.txt', 'r')
    task_parts = all_tasks_f.readlines()

    print_tasks(task_parts)
    all_tasks_f.close()

def display_stats():
    tasks_overview_f = ''
    users_overview_f = ''
    has_tasks_overview = exists('./task_overview.txt')
    has_users_overview = exists('./users_overview.txt')

    if has_tasks_overview and has_users_overview:
        tasks_overview_f = open('./task_overview.txt','r')
        users_overview_f = open('./users_overview.txt','r')

        print('-------- [ TASKS OVERVIEW ] --------\n')
        for line in tasks_overview_f:
            print(line)

        print('-------- [ USERS OVERVIEW ] --------\n')
        for line in users_overview_f:
            print(line)

    else:
        print('Please generate reports by selecting "gr" option.')
        view_menu()


def view_mine():
    all_tasks_f = open('./tasks.txt', 'r+')
    all_tasks_list = all_tasks_f.readlines()
    my_tasks = []


    for line in all_tasks_list:
        split_task_parts_2 = line.split(', ')

        if split_task_parts_2[1] == name: # Check if task name the same of the login
            my_tasks.append(line)


    print_tasks(my_tasks)
    all_tasks_f.close()


    while True:
        user_input_choice = int(input('Select a task number to edit or -1 to return: '))
        choice_task = user_input_choice -1

        if user_input_choice == -1: # Option to return to main menu
            view_menu()
            break

        if choice_task < 0 or choice_task > len(my_tasks):
            print("You have entered an invalid option. Try again.")
            continue

        task_to_edit_items = my_tasks[choice_task].split(', ')

        if task_to_edit_items[5] == 'Yes\n':
            print("The task selected is completed and can not be edited.\n")
            continue

        break


    while True:
        output = f'------- [ SELECT AN OPTION ] -------\n'
        output += '\n'
        output += '-1 - Go back to main menu\n'
        output += '1 - Edit details\n'
        output += '2 - Mark as completed\n'
        output += '-----------------------------------\n'

        choice_edit = int(input(output))

        if choice_edit == 0 or choice_edit >= 3 or choice_edit <= -2:
            print("You have entered an invalid option. Try again.")
            continue

        if choice_edit == 1:
            task_username = input("Change the assigned username to: ")
            task_due_date = input("Change the due date to: ")
            task_to_edit_items[1] = task_username
            task_to_edit_items[3] = task_due_date

        elif choice_edit == 2:
            task_to_edit_items[-1] = "Yes\n"


        all_tasks_list[all_tasks_list.index(my_tasks[choice_task])] = ', '.join(task_to_edit_items)

        all_tasks_f = open('./tasks.txt', 'w+')
        all_tasks_f.write(''.join(all_tasks_list))
        all_tasks_f.close()

        print("Your task is updated.\n")
        view_menu()
        break


def gen_reports():
    users_f = open('./user.txt', 'r')
    tasks_f = open('./tasks.txt', 'r')
    users_list = users_f.readlines()
    tasks_list = tasks_f.readlines()

    total_tasks = len(tasks_list)
    total_users = len(users_list)
    today_date = datetime.today()
    users_report = []
    task_report = []

    print_and_append(users_report, f"Total users on the system: {total_users}\n")
    print_and_append(task_report, f"Total tasks on the system: {total_tasks}\n")

    # ==== Users Reports ====
    # For every user we are looping over tasks and if task belongs to that user, we save some info into variables 
    for user in users_list:
        user_name = user.split(', ')[0]
        user_tasks = []
        user_tasks_completed_count = 0
        user_tasks_overdue_count = 0

        for task in tasks_list:
            task_items = task.split(', ')
            task_owner = task_items[1]
            task_date = datetime.strptime(task_items[3], "%d/%m/%Y")

            if task_owner == user_name:
                user_tasks.append(task)

                if task_items[-1] == 'Yes\n':
                    user_tasks_completed_count =+ 1

                if task_date > today_date:
                    user_tasks_overdue_count += 1


        if len(user_tasks) == 0:
            print_and_append(users_report, f'User {user_name} has no tasks.\n')

        else:
            # run some calculations and print based on the tasks gathered PER user
            user_tasks_count = len(user_tasks)
            task_assigned_percentage = round((user_tasks_count / total_tasks) * 100, 1)
            task_uncompleted_count = user_tasks_count - user_tasks_completed_count
            task_completed_percentage = round((user_tasks_completed_count / user_tasks_count) * 100, 1)
            task_uncompleted_percentage = round((task_uncompleted_count / user_tasks_count) * 100, 1)
            task_overdue_percentage = round((user_tasks_overdue_count / user_tasks_count) * 100, 1)

            print_and_append(users_report, f'''User {user_name} details: \n
▪ Total tasks: {user_tasks_count}
▪ The percentage of tasks assigned: {task_assigned_percentage}
▪ The percentage of the tasks completed: {task_completed_percentage}
▪ The percentage of the tasks uncompleted: {task_uncompleted_percentage}
▪ The percentage of the tasks overdue: {task_overdue_percentage}\n
''')

    users_report.append(f"_____Report generated on {date.today()}_____\n\n")

    # ==== Tasks Reports ====
    tasks_complete_count = 0
    tasks_overdue_count = 0

    for task in tasks_list:
        task_items = task.split(', ')
        task_date = datetime.strptime(task_items[3], "%d/%m/%Y")

        if task.split(', ')[5] == 'Yes\n':
            tasks_complete_count += 1

        if task_date > today_date:
            tasks_overdue_count += 1

    tasks_uncompleted_count = total_tasks - tasks_complete_count
    tasks_uncomplete_percentage = round((tasks_uncompleted_count / total_tasks) * 100, 1)
    overdue_percentage = round((tasks_overdue_count / total_tasks) * 100, 1)

    print_and_append(task_report, f"Number of uncompleted tasks: {tasks_uncompleted_count}\n")
    print_and_append(task_report, f"Number of completed tasks: {tasks_complete_count}\n")
    print_and_append(task_report, f"Percentage of incomplete: {tasks_uncomplete_percentage}\n")
    print_and_append(task_report, f"Number of overdue tasks: {tasks_overdue_count}\n")
    print_and_append(task_report, f"Percentage of overdue tasks: {overdue_percentage}\n")

    task_report.append(f"_____Report generated on {date.today()}_____\n\n")


    # Saves all information into overview files
    tasks_report_update_f = open('./task_overview.txt', 'a+')
    tasks_report_update_f.write(''.join(task_report))
    tasks_report_update_f.close()

    users_report_update_f = open('./users_overview.txt', 'a+')
    users_report_update_f.write(''.join(users_report))
    users_report_update_f.close()

    users_f.close()
    tasks_f.close()


# ==== Login Section ====
users_f = open('./user.txt', 'r+')
list_of_users = {}

for line in users_f: # Saves all users in a dictionary
    item_list = line.split(', ')
    name = item_list[0]
    password = item_list[1].replace('\n', '')
    list_of_users[name] = password

need_name = True
need_password = True
name = 'admin'
password = 'adm1n'

while need_name: # While loop to request user name
    print('Please, insert your name and password to login:')
    name = input('Name: ').lower()

    if name in list_of_users.keys():
        need_name = False
    else:
        print('Try again')

while need_password: # While loop to request user password
    password = input('Password: ').lower()
    if list_of_users[name] != password:
        print('Password incorrect')
        continue
    else:
        print(f'Welcome, {name}, you are logged in\n')
    need_password = False


while True: # Always show menu after login
    view_menu()
