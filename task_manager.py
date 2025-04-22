from colorama import Fore, Style


def add_task(tasks, description):
    task = {
        'description': description,
        'done': False
    }
    tasks.append(task)
    print(f'Added task: "{description}"')


def list_tasks(tasks):
    if not tasks:
        print(Fore.YELLOW + "No tasks currently.")
        return

    for i, task in enumerate(tasks, start=1):
        status = f"{Fore.GREEN}✅" if task["done"] else f"{Fore.RED}[ ]"
        desc = f"{Style.BRIGHT}{Fore.WHITE}{task['description']}"
        print(f"{Fore.CYAN}{i}. {status} {desc}")


def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        print(Fore.GREEN + f'Marked task {index + 1} as done.')
    else:
        print(Fore.RED + "Task number is out of range.")


def mark_undone(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = False
        print(Fore.GREEN + f'Marked task {index + 1} as not done.')
    else:
        print(Fore.RED + "Task number is out of range.")


def remove_task(tasks, index):
    if 0 <= index < len(tasks):
        removed = tasks[index]['description']
        del tasks[index]
        print(Fore.GREEN + f'Task "{removed}" was deleted.')
    else:
        print(Fore.RED + "Task number is out of range.")
