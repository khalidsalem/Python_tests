# Simple To-Do List Program

# This program helps you manage a to-do list by allowing you to add, view, and remove tasks.

# Initialize an empty to-do list
# This is where we will store the tasks.
to_do_list = []

# Function to show the menu of options
def show_menu():
    """
    Displays the list of actions the user can choose from:
    1. View the to-do list.
    2. Add a new task.
    3. Remove a task.
    4. Exit the program.
    """
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Function to display the current list of tasks
def view_tasks():
    """
    Shows all the tasks currently in the to-do list.
    If there are no tasks, it informs the user that the list is empty.
    """
    if len(to_do_list) == 0:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task}")  # Prints each task with a number for easy reference.

# Function to add a task to the list
def add_task():
    """
    Prompts the user to enter a task and adds it to the to-do list.
    """
    task = input("\nEnter the task you want to add: ")  # Get task from the user
    to_do_list.append(task)  # Add the task to the list
    print(f"Task '{task}' added.")  # Confirm that the task was added

# Function to remove a task from the list
def remove_task():
    """
    Shows the tasks and asks the user to enter the number of the task they want to remove.
    Removes the selected task from the list.
    """
    view_tasks()  # First, show the tasks so the user can choose from them
    if len(to_do_list) > 0:
        try:
            task_number = int(input("\nEnter the number of the task to remove: "))
            # Check if the entered number is valid
            if 1 <= task_number <= len(to_do_list):
                removed_task = to_do_list.pop(task_number - 1)  # Remove the selected task
                print(f"Task '{removed_task}' removed.")  # Confirm the task was removed
            else:
                print("Invalid task number.")  # Inform if the entered number is not in the range
        except ValueError:
            print("Please enter a valid number.")  # Error message if the input is not a number

# Main function to run the to-do list program
def main():
    """
    Runs the to-do list program. Displays the menu and performs the action chosen by the user.
    The program continues to run until the user selects 'Exit'.
    """
    while True:
        show_menu()  # Display the menu of options
        choice = input("\nEnter your choice (1-4): ")  # Get the user's menu choice
        
        if choice == '1':
            view_tasks()  # Show the current list of tasks
        elif choice == '2':
            add_task()  # Let the user add a new task
        elif choice == '3':
            remove_task()  # Let the user remove an existing task
        elif choice == '4':
            print("Exiting the program. Goodbye!")  # Exit the program
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please select a valid option.")  # Handle invalid inputs

# Start the program by calling the main function
if __name__ == "__main__":
    main()
