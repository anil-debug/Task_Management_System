import streamlit as st
import requests

BASE_URL = "http://backend:5000"


def main():
    st.title("Task Management System")

    menu = ["Create User", "Create Task", "View Tasks"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create User":
        st.subheader("Create New User")
        username = st.text_input("Username")
        email = st.text_input("Email")
        if st.button("Create"):
            response = requests.post(f"{BASE_URL}/users", json={"username": username, "email": email})
            st.write(response.json())

    elif choice == "Create Task":
        st.subheader("Create New Task")
        title = st.text_input("Title")
        description = st.text_area("Description")
        due_date = st.date_input("Due Date")
        user_id = st.number_input("User ID", min_value=1)
        if st.button("Create"):
            response = requests.post(f"{BASE_URL}/tasks", json={"title": title, "description": description, "due_date": due_date.isoformat(), "user_id": user_id})
            st.write(response.json())

    elif choice == "View Tasks":
        st.subheader("View Tasks")
        user_id = st.number_input("User ID", min_value=1)
        if st.button("View"):
            response = requests.get(f"{BASE_URL}/tasks/{user_id}")
            tasks = response.json()
            for task in tasks:
                st.write(f"Title: {task['title']}")
                st.write(f"Description: {task['description']}")
                st.write(f"Due Date: {task['due_date']}")
                st.write(f"Status: {task['status']}")
                st.write("---")

if __name__ == "__main__":
    main()
