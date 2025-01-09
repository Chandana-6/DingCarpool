import mariadb
from database import connect_to_db

def process_match(user1_id, user2_id, match_criteria):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            # Example match criteria logic
            cursor.execute(
                "SELECT * FROM matches WHERE user1_id=? AND user2_id=? AND criteria=?",
                (user1_id, user2_id, match_criteria)
            )
            match = cursor.fetchone()
            if match:
                return "Match already exists"
            else:
                cursor.execute(
                    "INSERT INTO matches (user1_id, user2_id, criteria) VALUES (?, ?, ?)",
                    (user1_id, user2_id, match_criteria)
                )
                conn.commit()
                return "Match created successfully"
        except mariadb.Error as e:
            return f"Database error: {e}"
        finally:
            conn.close()
    else:
        return "Database connection failed"

def reject_match(match_id):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM matches WHERE id=?", (match_id,))
            conn.commit()
            return "Match rejected and removed"
        except mariadb.Error as e:
            return f"Database error: {e}"
        finally:
            conn.close()
    else:
        return "Database connection failed"


