from database import connection, cursor

def get_tasks():
    cursor.execute(
        "SELECT * FROM tasks ORDER BY id"
    )

    return cursor.fetchall()


def create_task(title):
    
    cursor.execute(
        "INSERT INTO tasks (title, completed) VALUES (%s, %s)",
        (title, False)
    )

    connection.commit()

def mark_task_completed(task_id):
    cursor.execute(
        "UPDATE tasks SET completed = True WHERE id = %s",
        (task_id,)
    )

    connection.commit()

    return cursor.rowcount

def delete_task_by_id(task_id):
    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (task_id,)
    )

    connection.commit()

    return cursor.rowcount

def update_task_title(task_id, new_title):
    cursor.execute(
        "UPDATE tasks SET title = %s WHERE id = %s",
        (new_title, task_id)
    )

    connection.commit()

    return cursor.rowcount

def get_task_by_id(task_id):
    cursor.execute(
        "SELECT * FROM tasks WHERE id = %s",
        (task_id,)
    )

    return cursor.fetchone()

def get_task_by_title(title):
    cursor.execute(
        "SELECT * FROM tasks WHERE LOWER(title) = LOWER(%s)",
        (title,)
    )

    return cursor.fetchone()