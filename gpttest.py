import datetime

#test
# Function to get user input for tasks and deadlines
def get_tasks():
    tasks = []
    num_tasks = int(input("How many tasks do you have? "))
    print("\n \n \n")
    for i in range(num_tasks):
        task_name = input(f"Enter the name of task {i+1}: ")
        deadline_str = input(f"Enter the deadline for task {i+1} (in hours/days/date): ")
        tasks.append((task_name, deadline_str))
    return tasks

# Function to sort tasks based on deadlines
def sort_tasks(tasks):
    now = datetime.datetime.now()
    sorted_tasks = []
    for task in tasks:
        task_name = task[0]
        deadline_str = task[1]
        if 'hour' in deadline_str or 'hours' or 'hrs' or 'hr' in deadline_str:
            hours = int(deadline_str.split()[0])
            deadline = now + datetime.timedelta(hours=hours)
            sorted_tasks.append((task_name, deadline))
        elif 'day' in deadline_str or 'days' in deadline_str:
            days = int(deadline_str.split()[0])
            deadline = now + datetime.timedelta(days=days)
            sorted_tasks.append((task_name, deadline))
        else:
            try:
                deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d')
                sorted_tasks.append((task_name, deadline))
            except ValueError:
                print(f"Invalid deadline format for task '{task_name}'. Skipping task.")
    sorted_tasks.sort(key=lambda x: x[1]) # Sfort tasks based on deadline
    return sorted_tasks

# Function to display sorted tasks
def display_sorted_tasks(sorted_tasks):
    print("\nYour priorities are: ")
    for i, task in enumerate(sorted_tasks):
        print(f"{i+1}. Task: {task[0]}, Deadline: {task[1].strftime('%Y-%m-%d %H:%M:%S')}")

# Main program
if __name__ == "__main__":
    tasks = get_tasks()
    sorted_tasks = sort_tasks(tasks)
    display_sorted_tasks(sorted_tasks)
