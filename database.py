import sqlite3
import pandas as pd
from contextlib import contextmanager

DB_NAME = "peacepulse.db"

@contextmanager
def get_db_connection():
    """Provides a safe, contextual database connection."""
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row  # Return rows as dict-like objects
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    """Initializes the database schema if it doesn't exist."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Mood Logs Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mood_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_email TEXT NOT NULL,
                mood TEXT NOT NULL,
                comment TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Forum Posts Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS forum_posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                message TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                is_anonymous BOOLEAN DEFAULT 0
            )
        ''')
        
        # Chat History Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_email TEXT NOT NULL,
                role TEXT NOT NULL,
                message TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

# --- Mood Helper Functions ---

def insert_mood(user_email, mood, comment):
    """Inserts a new mood log for a specific user."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO mood_logs (user_email, mood, comment)
                VALUES (?, ?, ?)
            ''', (user_email, mood, comment))
            conn.commit()
        return True
    except Exception as e:
        print(f"Error inserting mood: {e}")
        return False

def get_user_moods(user_email):
    """Fetches all mood logs for a specific user as a pandas DataFrame."""
    try:
        with get_db_connection() as conn:
            # We use pandas directly with the connection for easy DataFrame conversion
            query = "SELECT mood, comment, timestamp FROM mood_logs WHERE user_email = ? ORDER BY timestamp DESC"
            df = pd.read_sql_query(query, conn, params=(user_email,))
            
            # Ensure timestamp is datetime
            if not df.empty:
                df['time'] = pd.to_datetime(df['timestamp'])
            return df
    except Exception as e:
        print(f"Error fetching moods: {e}")
        return pd.DataFrame() # Return empty dataframe on error

# --- Forum Helper Functions ---

def insert_forum_post(username, message, is_anonymous=False):
    """Inserts a new forum post."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO forum_posts (username, message, is_anonymous)
                VALUES (?, ?, ?)
            ''', (username, message, 1 if is_anonymous else 0))
            conn.commit()
        return True
    except Exception as e:
        print(f"Error inserting forum post: {e}")
        return False

def get_forum_posts():
    """Fetches all forum posts as a list of dicts."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT username, message, timestamp, is_anonymous 
                FROM forum_posts 
                ORDER BY timestamp ASC
            ''')
            rows = cursor.fetchall()
            # Convert to list of dicts for frontend
            return [dict(row) for row in rows]
    except Exception as e:
        print(f"Error fetching forum posts: {e}")
        return []

# --- Chatbot Helper Functions ---

def insert_chat_log(user_email, role, message):
    """Inserts a new chat log and trims history to maximum 100 messages per user."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO chat_history (user_email, role, message)
                VALUES (?, ?, ?)
            ''', (user_email, role, message))
            
            # Cleanup: Keep only the most recent 100 messages for this user
            cursor.execute('''
                DELETE FROM chat_history 
                WHERE id NOT IN (
                    SELECT id FROM chat_history 
                    WHERE user_email = ? 
                    ORDER BY timestamp DESC 
                    LIMIT 100
                ) AND user_email = ?
            ''', (user_email, user_email))
            
            conn.commit()
        return True
    except Exception as e:
        print(f"Error inserting chat log: {e}")
        return False

def get_recent_chat_history(user_email, limit=20):
    """Fetches the most recent chat messages for a user to initialize session state."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT role, message 
                FROM chat_history 
                WHERE user_email = ? 
                ORDER BY timestamp DESC 
                LIMIT ?
            ''', (user_email, limit))
            rows = cursor.fetchall()
            
            # Reverse to get chronological order
            chat_log = [{"role": row["role"], "content": row["message"]} for row in rows]
            return chat_log[::-1]
    except Exception as e:
        print(f"Error fetching chat history: {e}")
        return []
