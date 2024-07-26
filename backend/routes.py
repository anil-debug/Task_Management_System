from flask import request, jsonify
from app import app, db
from services.db_interaction import PostgreSQLInteraction

# Initialize PostgreSQL interaction
try:
    PostgreSQL = PostgreSQLInteraction(
        dbname='postgres',
        user='postgres',
        password='mysecretpassword',
        host='postgres',  # Use Docker service name
        port=5432
    )
    PostgreSQL.connect()
    all_tables = ["users", "tasks"]
    for table_name in all_tables:
        PostgreSQL.create_table(table_name)
except Exception as e:
    print(f"Error initializing PostgreSQLInteraction: {e}")
    PostgreSQL = None

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if PostgreSQL:
        try:
            query = """
                INSERT INTO users (username, email)
                VALUES (%s, %s) RETURNING id;
            """
            PostgreSQL.cur.execute(query, (data['username'], data['email']))
            user_id = PostgreSQL.cur.fetchone()[0]
            PostgreSQL.conn.commit()
            return jsonify({'message': 'User created successfully', 'id': user_id}), 201
        except Exception as e:
            PostgreSQL.conn.rollback()
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'Database connection failed'}), 500

@app.route('/users', methods=['GET'])
def get_users():
    if PostgreSQL:
        try:
            query = "SELECT id, username, email FROM users;"
            PostgreSQL.cur.execute(query)
            users = PostgreSQL.cur.fetchall()
            return jsonify([{
                'id': user[0],
                'username': user[1],
                'email': user[2]
            } for user in users]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'Database connection failed'}), 500

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if PostgreSQL:
        try:
            query = """
                INSERT INTO tasks (title, description, due_date, user_id)
                VALUES (%s, %s, %s, %s) RETURNING id;
            """
            PostgreSQL.cur.execute(query, (data['title'], data['description'], data['due_date'], data['user_id']))
            task_id = PostgreSQL.cur.fetchone()[0]
            PostgreSQL.conn.commit()
            return jsonify({'message': 'Task created successfully', 'id': task_id}), 201
        except Exception as e:
            PostgreSQL.conn.rollback()
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'Database connection failed'}), 500

@app.route('/tasks/<int:user_id>', methods=['GET'])
def get_tasks(user_id):
    if PostgreSQL:
        try:
            query = "SELECT id, title, description, due_date, status FROM tasks WHERE user_id = %s;"
            PostgreSQL.cur.execute(query, (user_id,))
            tasks = PostgreSQL.cur.fetchall()
            return jsonify([{
                'id': task[0],
                'title': task[1],
                'description': task[2],
                'due_date': task[3],
                'status': task[4]
            } for task in tasks]), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'Database connection failed'}), 500

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task_status(task_id):
    data = request.get_json()
    new_status = data.get('status')
    
    if PostgreSQL:
        try:
            query = "UPDATE tasks SET status = %s WHERE id = %s;"
            PostgreSQL.cur.execute(query, (new_status, task_id))
            PostgreSQL.conn.commit()
            if PostgreSQL.cur.rowcount > 0:
                return jsonify({'message': 'Task status updated successfully'}), 200
            else:
                return jsonify({'error': 'Task not found'}), 404
        except Exception as e:
            PostgreSQL.conn.rollback()
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'Database connection failed'}), 500