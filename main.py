from task_data import load_tasks, save_tasks
from task_manager import add_task, list_tasks, mark_done, mark_undone, remove_task
from colorama import init, Fore, Style
init(autoreset=True)


def main():
    tasks = load_tasks()

    print("📋 Welcome to the CLI To-Do List!")
    print("Type 'help' to see available commands.\n")

    while True:
        user_input = input("> ").strip()

        if not user_input:
            continue

        parts = user_input.split(maxsplit=1)
        command = parts[0].lower()
        argument = parts[1] if len(parts) > 1 else ""

        if command == "add":
            if argument:
                add_task(tasks, argument)
                save_tasks(tasks)
            else:
                print(Fore.YELLOW + "Usage: add <task description>")

        elif command == "list":
            list_tasks(tasks)

        elif command == "done":
            if argument.isdigit():
                index = int(argument) - 1
                mark_done(tasks, index)
                save_tasks(tasks)
            else:
                print(Fore.GREEN + "Usage: done <task number>")

        elif command == "undone":
            if argument.isdigit():
                index = int(argument) - 1
                mark_undone(tasks, index)
                save_tasks(tasks)
            else:
                print(Fore.GREEN + "Usage: undone <task number>")

        elif command == "remove":
            if argument.isdigit():
                index = int(argument) - 1
                remove_task(tasks, index)
                save_tasks(tasks)
            else:
                print(Fore.GREEN + "Usage: remove <task number>")

        elif command in ["exit", "quit"]:
            print("Goodbye!")
            break

        elif command == "help":
            print("""Available commands:
  add <task>        - Add a new task
  list              - List all tasks
  done <number>     - Mark a task as done
  undone <number>   - Mark a task as not done
  remove <number>   - Delete a task
  exit / quit       - Exit the app
""")
        else:
            print("Unknown command. Type 'help' to see available options.")


if __name__ == "__main__":
    main()
