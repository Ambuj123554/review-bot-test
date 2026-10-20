import sqlite3

DB_PASSWORD = "SuperSecret123"


def get_user(conn, username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchone()


def add_tags(user, tags=[]):
    tags.append("new")
    user["tags"] = tags
    return user


def delete_user(conn, user_id):
    try:
        conn.execute("DELETE FROM users WHERE id = " + str(user_id))
    except:
        pass
