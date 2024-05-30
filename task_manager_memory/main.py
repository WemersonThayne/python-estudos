import model.task as t
import utils.utils as util
import utils.print_table as ptable


tasks = list()


def generate_id():
    if not tasks:
        return 1
    else:
        task = tasks[len(tasks) - 1]
        return task.id + 1


def create_task():
    title = util.read_info("Enter title your task:")
    description = util.read_info("Enter description your task:")
    return t.Task(generate_id(), title, description, False)


def edit_task():
    print("What task do you want to edit?")
    id = int(util.read_info("Enter the task identify:"))
    for task in tasks:
        if int(task.id) == id:
            title = util.read_info("Enter new title your task:")
            description = util.read_info("Enter new description your task:")
            task.description = description
            task.title = title
            break


def show_tasks():

    print()
    print()
    if len(tasks) == 0:
        print("There are no tasks")
        return

    headers = ["Id", "Title", "Description", "Status"]
    attributes = ["id", "title", "description", "status"]
    ptable.print_table(tasks, headers, attributes)
    print()


def delete_task():
    print()
    if len(tasks) == 0:
        print("There are no tasks")
        return

    print("What task do you want to delete?")
    id = int(util.read_info("Enter the task identify:"))
    for task in tasks:
        if int(task.id) == id:
            tasks.remove(task)
            print("Task conclusion successfully")
            break


def mark_task():
    print()
    if len(tasks) == 0:
        print("There are no tasks")
        return

    print("What task do you want to mark?")
    id = int(util.read_info("Enter the task identify:"))
    for task in tasks:
        if int(task.id) == id:
            task.status = True
            print("Task edited successfully")
            break


def main():

    while True:
        util.menu()
        op = util.read_option_menu()

        if op == 1:
            task = create_task()
            tasks.append(task)
            print("Task created successfully")

        if op == 2:
            show_tasks()

        if op == 3:
            edit_task()

        if op == 4:
            delete_task()

        if op == 5:
            mark_task()

        if op == 0:
            print("Bye Bye!")
            break


main()
