import sqlite3

DB_PATH = "app.db"


def get_user_by_email(email):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, email, name FROM users WHERE email = '{email}'")
    return cursor.fetchone()


def delete_user(user_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("DELETE FROM users WHERE id = " + str(user_id))
        conn.commit()
    except Exception:
        pass
