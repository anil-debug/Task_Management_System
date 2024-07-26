import psycopg2
from psycopg2 import OperationalError

class PostgreSQLInteraction:
    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host, port=self.port)
            self.cur = self.conn.cursor()
            print("Connected to PostgreSQL!")
        except OperationalError as e:
            print(f"Error connecting to PostgreSQL: {e}")

    def create_table(self, table_name):
        """
        Create tables for the task management system.
        """
        table_name = table_name.lower()

        # Define SQL schemas for different tables
        table_schemas = {
            'users': """
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(80) UNIQUE NOT NULL,
                    email VARCHAR(120) UNIQUE NOT NULL
                );
            """,
            'tasks': """
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(120) NOT NULL,
                    description TEXT,
                    due_date TIMESTAMP,
                    status VARCHAR(20) DEFAULT 'Pending',
                    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
                );
            """
        }

        # Create the table
        if table_name in table_schemas:
            sql = table_schemas[table_name]
            try:
                self.cur.execute(sql)
                self.conn.commit()
                print(f"Table '{table_name}' created or already exists.")
            except psycopg2.Error as e:
                print(f"Error creating table '{table_name}': {e}")
        else:
            print(f"Table '{table_name}' is not defined in the schemas.")

    def get_tables(self):
        """Fetch existing tables in the database."""
        try:
            self.cur.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public';
            """)
            tables = [row[0] for row in self.cur.fetchall()]
            return tables
        except psycopg2.Error as e:
            print(f"Error fetching tables: {e}")
            return []
