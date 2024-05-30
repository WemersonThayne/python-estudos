def read_info(msg):
    print(msg)
    read = input()
    return read


def read_option_menu():
    return int(read_info("Enter desired option:"))


def menu():
    print("###### MENU ##########")
    print(" 1 - CREATE TASK")
    print(" 2 - LIST TASKS")
    print(" 3 - EDIT TASK")
    print(" 4 - DELETE TASK")
    print(" 5 - CHECKED TASK")
    print(" 0 - QUIT \n")

