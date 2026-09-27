from database import connection, cursor

def show_tasks():
    cursor.execute(
        "SELECT * FROM tasks ORDER BY id"
    )

    tasks = cursor.fetchall()
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

    cursor.execute(
        "UPDATE tasks SET completed = True WHERE id = %s",
        (task_id,)
    )    

    if cursor.rowcount == 0:
        print("Такой задачи нет!")
    else:
        connection.commit()
        print("Задача выполнена!")

def delete_task():
    try:
        task_id = int(input("Введите id задачи: "))
    except ValueError:
        print("Нужно ввести число!")
        return

    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (task_id,)
        )

    if cursor.rowcount == 0:
        print("Такой задачи нет!")
    else:
        connection.commit()
        print("Задача удалена!")

def edit_task():
    try:
        task_id = int(input("Введите id задачи: "))
    except ValueError:
        print("Нужно ввести число!")
        return

    new_title = input("Введите новое название задачи: ")

    cursor.execute(
        "UPDATE tasks SET title = %s WHERE id = %s",
        (new_title, task_id)
    )

    if cursor.rowcount == 0:
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
    
    cursor.execute(
        "SELECT * FROM tasks WHERE id = %s",
        (task_id,)
        )

    task = cursor.fetchone()

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

cursor.close()
connection.close()
print("Программа завершена!")