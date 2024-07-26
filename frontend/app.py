# import streamlit as st
# import requests

# BASE_URL = "http://backend:5000"

# class TaskManagementSystem:
#     def __init__(self):
#         self.menu = ["Create User", "Create Task", "View Tasks"]
#         self.run()

#     def run(self):
#         st.title("Task Management System")
#         choice = st.sidebar.selectbox("Menu", self.menu)
#         if choice == "Create User":
#             self.create_user()
#         elif choice == "Create Task":
#             self.create_task()
#         elif choice == "View Tasks":
#             self.view_tasks()

#     def create_user(self):
#         st.subheader("Create New User")
#         username = st.text_input("Username")
#         email = st.text_input("Email")
#         if st.button("Create"):
#             response = requests.post(f"{BASE_URL}/users", json={"username": username, "email": email})
#             if response.status_code == 201:
#                 st.success("User created successfully!")
#             else:
#                 st.error("Failed to create user.")
#             st.write(response.json())

#     def create_task(self):
#         st.subheader("Create New Task")
#         title = st.text_input("Title")
#         description = st.text_area("Description")
#         due_date = st.date_input("Due Date")
#         user_id = st.number_input("User ID", min_value=1)
#         if st.button("Create"):
#             response = requests.post(f"{BASE_URL}/tasks", json={"title": title, "description": description, "due_date": due_date.isoformat(), "user_id": user_id})
#             if response.status_code == 201:
#                 st.success("Task created successfully!")
#             else:
#                 st.error("Failed to create task.")
#             st.write(response.json())

#     def view_tasks(self):
#         st.subheader("View Tasks")
#         user_id = st.number_input("User ID", min_value=1)
#         if st.button("View"):
#             response = requests.get(f"{BASE_URL}/tasks/{user_id}")
#             if response.status_code == 200:
#                 tasks = response.json()
#                 if tasks:
#                     for task in tasks:
#                         st.write(f"Title: {task['title']}")
#                         st.write(f"Description: {task['description']}")
#                         st.write(f"Due Date: {task['due_date']}")
#                         st.write(f"Status: {task['status']}")
#                         st.write("---")
#                 else:
#                     st.write("No tasks found.")
#             else:
#                 st.error("Failed to retrieve tasks.")

# if __name__ == "__main__":
#     TaskManagementSystem()
import streamlit as st
import requests

BASE_URL = "http://backend:5000"

class TaskManagementSystem:
    def __init__(self):
        self.menu = ["Create User", "Create Task", "View Tasks", "Update Task Status"]
        self.run()

    def run(self):
        st.title("Task Management System")
        choice = st.sidebar.selectbox("Menu", self.menu)
        if choice == "Create User":
            self.create_user()
        elif choice == "Create Task":
            self.create_task()
        elif choice == "View Tasks":
            self.view_tasks()
        elif choice == "Update Task Status":
            self.update_task_status()

    def create_user(self):
        st.subheader("Create New User")
        username = st.text_input("Username")
        email = st.text_input("Email")
        if st.button("Create"):
            response = requests.post(f"{BASE_URL}/users", json={"username": username, "email": email})
            if response.status_code == 201:
                st.success("User created successfully!")
            else:
                st.error("Failed to create user.")
            st.write(response.json())

    def create_task(self):
        st.subheader("Create New Task")
        title = st.text_input("Title")
        description = st.text_area("Description")
        due_date = st.date_input("Due Date")
        user_id = st.number_input("User ID", min_value=1)
        if st.button("Create"):
            response = requests.post(f"{BASE_URL}/tasks", json={"title": title, "description": description, "due_date": due_date.isoformat(), "user_id": user_id})
            if response.status_code == 201:
                st.success("Task created successfully!")
            else:
                st.error("Failed to create task.")
            st.write(response.json())

    def view_tasks(self):
        st.subheader("View Tasks")
        user_id = st.number_input("User ID", min_value=1)
        if st.button("View"):
            response = requests.get(f"{BASE_URL}/tasks/{user_id}")
            if response.status_code == 200:
                tasks = response.json()
                if tasks:
                    for task in tasks:
                        st.write(f"Title: {task['title']}")
                        st.write(f"Description: {task['description']}")
                        st.write(f"Due Date: {task['due_date']}")
                        st.write(f"Status: {task['status']}")
                        st.write("---")
                else:
                    st.write("No tasks found.")
            else:
                st.error("Failed to retrieve tasks.")

    def update_task_status(self):
        st.subheader("Update Task Status")
        task_id = st.number_input("Task ID", min_value=1)
        status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])
        if st.button("Update Status"):
            response = requests.patch(f"{BASE_URL}/tasks/{task_id}", json={"status": status})
            if response.status_code == 200:
                st.success("Task status updated successfully!")
            else:
                st.error(f"Failed to update task status: {response.text}")
            st.write(response.json())

if __name__ == "__main__":
    TaskManagementSystem()
