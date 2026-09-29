from database import connection
from task_repository import get_tasks, create_task, mark_task_completed, delete_task_by_id, update_task_title, get_task_by_id, get_task_by_title

def show_tasks():

    tasks = get_tasks()

    for task in tasks:
        if task[2]:
            result = "✓ Выполнено"
        else:
            result = "✗ Не Выполнено"
        print(f"ID: {task[0]} | Задача: {task[1]} | Статус: {result} | Время создания: {task[3].strftime('%d.%m.%Y %H:%M')}")


def add_task():

    title = input("Введите задачу: ")

    cursor.execute(
        "INSERT INTO tasks (title, completed) VALUES (%s, %s)",
        (title, False)
    )

    connection.commit()

def complete_task():

    try:
        task_id = int(input("Введите id задачи: "))
    except ValueError:
        print("Нужно ввести число!")
        return

    result = mark_task_completed(task_id)

    if result == 0:
        print("Такой задачи нет!")
    else:
        print("Задача выполнена!")

def delete_task():
    try:
        task_id = int(input("Введите id задачи: "))
    except ValueError:
        print("Нужно ввести число!")
        return

    result = delete_task_by_id(task_id)

    if result == 0:
        print("Такой задачи нет!")
    else:
        print("Задача удалена!")

def edit_task():
    try:
        task_id = int(input("Введите id задачи: "))
    except ValueError:
        print("Нужно ввести число!")
        return

    task = get_task_by_id(task_id)

    if task is None:
        print("Такой задачи нет!")
    else:
        connection.commit()
        print("Задача изменена!")

def find_task():

    try:
        task_id = int(input("Введите id задачи: "))
    except ValueError:
        print("Нужно ввести число!")
        return
    
    task = get_task_by_id(task_id)

    if task is None:
        print("Такой задачи нет!")
        return
    
    if task[2]:
        result = "✓ Выполнено"
    else:
        result = "✗ Не Выполнено"
    print(f"Id: {task[0]} | Название: {task[1]} | Статус: {result} | Время создания: {task[3].strftime('%d.%m.%Y %H:%M')}")

while True:

    print("--------TODO--------")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выполнить задачу")
    print("4. Удалить задачу")
    print("5. Редактировать задачу")
    print("6. Найти задачу")
    print("7. Выйти")

    try:
        choice = int(input("Выберите действие: "))
    except ValueError:
        print("Нужно ввести число!")
        continue  

    if choice == 1:

        add_task()

    elif choice == 2:

        show_tasks()

    elif choice == 3:

        complete_task()

    elif choice == 4:

        delete_task()

    elif choice == 5:

        edit_task()

    elif choice == 6:

        find_task()

    elif choice == 7:

        break
    else:
        print("Такого пункта нет!")

connection.close()
print("Программа завершена!")