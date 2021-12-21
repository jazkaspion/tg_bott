import sqlite3

con = sqlite3.connect('register.db', check_same_thread=False)
cur = con.cursor()


def creat_table():
    cur.execute(""" 
            CREATE TABLE "user" (
            "user_id"	INTEGER,
            "user_naim"	TEXT UNIQUE,
            "firstname"	TEXT,
            "number"	TEXT,
            PRIMARY KEY("user_id")
            );
            
            """)

    con.commit()
    return True


def create_table_log():
    cur.execute("""
            CREATE TABLE "Log"(
            "user_id" INTEGER,
            "message"  TEXT,
            PRIMARY KEY("user_id")
            );
            """)


def get_one(pk):
    cur.execute("select * from user where user_id=%s", {pk})
    root = cur.fetchone()
    return root


def create_user(user_id, username):
    sql = f"insert into user (user_id, user_name) values ({user_id}, '{username}')"
    cur.execute(sql)
    con.commit()
    return get_one(user_id)


def create_user_Log(user_id):
    a = '{\'state\': 0}'
    sql = "insert into Log (user_id, message) values (%s, \"%s\") " % (user_id, a)
    cur.execute(sql)
    con.commit()


def get_user_Log(user_id):
    cur.execute(f"select message from Log where user_id={user_id}")
    return cur.fetchone()


def change_Log(user_id, message):
    print(message, type(message))
    sql = f""" 
    update Log
    set message = \"{message}\"
    where user_id = {user_id}
    """
    cur.execute(sql)
    print("A")
    con.commit()
    return get_user_Log(user_id)


def clear_state(user_id):
    a = {'state': 0}
    sql = f""" 
      update Log
      set message = \"{a}\"
      where user_id = {user_id}
      """
    cur.execute(sql)
    con.commit()

    return get_user_Log(user_id)


def edit_user(log, user_id):
    sql = f"""
    update user
    set first_naime='{log.get("ism" "")} {log.get("familiya" "")}'
    number ='{log.get("ism", "")}', location = '{log.get("familiya", "")}'
    where user_id={user_id}
    
    """
