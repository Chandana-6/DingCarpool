import mariadb

def connect_to_db():
    try:
        conn = mariadb.connect(
            user="root",
            password="Chands@m1",
            host="localhost",
            port=3306,
            database="ding_db"
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        return None

def handle_request(request_type, data):
    if request_type == "database_acc_register":
        return handle_account_register(data)

def handle_account_register(data):
    # Implement logic to register account
    pass


