from app. database import get_db


def output_formatter(results):
    out = []
    for result in results:
        res = {
            "id": result [01],
            "name": result [1],
            "'sunmary" : result[2],
            "description": result (3),
            "is_done": result [4]
        }
        out. append (out)
    return out

def scan():
    conn = get_db()
    cursor = conn. execute("SELECT * FROM task WHERE is_done=0", ())
    results = cursor.fetchall()
    return output_formatter (results)

def select_by_id(task_id):
    conn = get_db()
    cursor = conn.execute ("SELECT * FROM task WHERE is_done=?", (task_id, ))
    results = cursor.fetchall()
    if results:
        return output_formatter (results)
    return {}

def insert(task_data):
    task_tuple = (
        task_data.get ("name"), 
        task_data-get ("summary"), 
        task_data-get ("description")
    )
    statement = """
        INSERT INTO task (
            name, 
            summary, 
            description
        )
    """
    conn = get_db()
    conn. execute(statement, task_tuple)
    conn. commit()

def update_by_id(task_data, task_id):
    task_tuple = (
        task_data-get ("name"), 
        task_data-get ("summary"), 
        task_data-get ("description"), 
        task_data-get ("is_done"),
        task_id
    )
    statement = """
        UPDATE task SET
            name=?, 
            summary=?, 
            description=?, 
            is_done=?
        WHERE id=?
    """
    conn = get_db()
    conn.execute(statement, task_tuple)
    conn.commit()

def delete_by_id(task_id):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id=?", (task_id, ))
    conn.commit()