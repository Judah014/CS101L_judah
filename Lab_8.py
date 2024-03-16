# Function to display the menu options
def display_menu():
    print("Menu Options:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. View To-Do List")
    print("4. Prioritize Task")
    print("5. Remove Completed Tasks")
    print("6. Exit")

# Function to add a new task to the to-do list
def add_task(todo_list):
    task_description = input("Enter task description: ")
    todo_list.append({"description": task_description, "completed": False, "priority": None})
    print("Task added successfully.")

# Function to display the current to-do list
def display_todo_list(todo_list):
    if todo_list:
        print("To-Do List:")
        for index, task in enumerate(todo_list):
            print(f"{index + 1}. {task['description']} - {'Completed' if task['completed'] else 'Pending'} - Priority: {task['priority'] or 'None'}")
    else:
        print("The to-do list is empty.")

# Function to mark a task as completed
def mark_completed(todo_list):
    display_todo_list(todo_list)
    task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]["completed"] = True
        print("Task marked as completed successfully.")
    else:
        print("Invalid task index.")

# Function to prioritize a task
def prioritize_task(todo_list):
    display_todo_list(todo_list)
    task_index = int(input("Enter the index of the task to prioritize: ")) - 1
    if 0 <= task_index < len(todo_list):
        priority = input("Enter priority level (high, medium, low): ")
        if priority in ['high', 'medium', 'low']:
            todo_list[task_index]["priority"] = priority
            print("Task prioritized successfully.")
        else:
            print("Invalid priority level.")
    else:
        print("Invalid task index.")

# Function to remove completed tasks
def remove_completed_tasks(todo_list):
    completed_tasks = [task for task in todo_list if task["completed"]]
    if completed_tasks:
        for task in completed_tasks:
            todo_list.remove(task)
        print("Completed tasks removed successfully.")
        print("Removed tasks:")
        for task in completed_tasks:
            print(task["description"])
    else:
        print("There are no completed tasks to remove.")

# Main function to manage the to-do list
def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            mark_completed(todo_list)
        elif choice == '3':
            display_todo_list(todo_list)
        elif choice == '4':
            prioritize_task(todo_list)
        elif choice == '5':
            remove_completed_tasks(todo_list)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Call the main function
if __name__ == "__main__":
    main()
