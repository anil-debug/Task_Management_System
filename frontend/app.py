import streamlit as st
from streamlit_option_menu import option_menu
import requests
from datetime import datetime
from PIL import Image
import os
BASE_URL = "http://backend:5000"

class TaskManagementSystem:
    def __init__(self):
        # Ensure session state has a 'name' key
        if 'name' not in st.session_state:
            st.session_state['name'] = "User"

        self.menu = ["Home", "Create User", "Create Task", "View Tasks", "Update Task Status"]
        self.menu_icon = ["house", "person", "plus", "list", "edit"]
        
        with st.sidebar:
            st.markdown(f"<h4 style='text-align: center;font-style: italic;'>Welcome {st.session_state['name']}</h4>", unsafe_allow_html=True)
            self.mode = option_menu(None, self.menu,
                                        icons=self.menu_icon,
                                        menu_icon="app-indicator", default_index=0,
                                        styles={"container": {"padding": "0!important", "background-color": "transparent"},
                                                "icon": {"color": "orange", "font-size": "28px"},
                                                "nav-link": {"font-size": "16px", "text-align": "left",
                                                             "margin": "0px",
                                                             "--hover-color": "#8e9297",
                                                             "display": "flex", "align-items": "center"},
                                                "nav-link-selected": {"background-color": "#2C3845"}})
        self.run()

    def run(self):
        st.title("Task Management System")
        if self.mode == "Home":
            self.show_home()
        elif self.mode == "Create User":
            self.create_user()
        elif self.mode == "Create Task":
            self.create_task()
        elif self.mode == "View Tasks":
            self.view_tasks()
        elif self.mode== "Update Task Status":
            self.update_task_status()

    def show_home(self):
        st.subheader("Welcome to the Task Management System")

        # Path to the image file
        image_path = "logos/task.jpg"  # Replace with your actual image file name

        if os.path.exists(image_path):
            # Open and display the image
            image = Image.open(image_path)
            st.image(image, caption='System Logo', use_column_width=True)
        else:
            st.error("Image file not found.")

    def create_user(self):
        st.subheader("Create New User")
        col1, col2 = st.columns([1, 2])  # Create columns for better layout
        with col1:
            username = st.text_input("Username")
        with col2:
            email = st.text_input("Email")
        
        if st.button("Create"):
            try:
                response = requests.post(f"{BASE_URL}/users", json={"username": username, "email": email})
                response.raise_for_status()  # Raise an HTTPError for bad responses
                st.success("User created successfully!")
                st.write(response.json())
            except requests.exceptions.RequestException as e:
                st.error(f"Failed to create user: {e}")

    def create_task(self):
        st.subheader("Create New Task")
        
        # Create a form for better alignment
        with st.form(key='create_task_form'):
            # Title input
            title = st.text_input("Title", max_chars=100)
            
            # User ID input
            user_id = st.number_input("User ID", min_value=1)
            
            # Description input
            description = st.text_area("Description", height=150)
            
            # Due Date input
            due_date = st.date_input("Due Date", min_value=datetime.today())
            
            # Submit button
            submit_button = st.form_submit_button(label="Create Task")
            
            if submit_button:
                try:
                    response = requests.post(f"{BASE_URL}/tasks", json={
                        "title": title, 
                        "description": description, 
                        "due_date": due_date.isoformat(), 
                        "user_id": user_id
                    })
                    response.raise_for_status()
                    st.success("Task created successfully!")
                    st.write(response.json())
                except requests.exceptions.RequestException as e:
                    st.error(f"Failed to create task: {e}")

    def view_tasks(self):
        st.subheader("View Tasks")
        user_id = st.number_input("User ID", min_value=1)
        if st.button("View"):
            try:
                response = requests.get(f"{BASE_URL}/tasks/{user_id}")
                response.raise_for_status()
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
            except requests.exceptions.RequestException as e:
                st.error(f"Failed to retrieve tasks: {e}")

    def update_task_status(self):
        st.subheader("Update Task Status")
        col1, col2 = st.columns([1, 2])  # Create columns for better layout
        with col1:
            task_id = st.number_input("Task ID", min_value=1)
        with col2:
            status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])
        
        if st.button("Update Status"):
            try:
                response = requests.patch(f"{BASE_URL}/tasks/{task_id}", json={"status": status})
                response.raise_for_status()
                st.success("Task status updated successfully!")
                st.write(response.json())
            except requests.exceptions.RequestException as e:
                st.error(f"Failed to update task status: {e}")

if __name__ == "__main__":
    TaskManagementSystem()
