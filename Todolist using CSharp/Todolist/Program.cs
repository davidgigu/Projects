using System;
using System.Collections.Generic;

class Task
{
    public string Description { get; set; }
    public DateTime DueDate { get; set; }
    public bool IsCompleted { get; set; }
}

class TodoList
{
    private List<Task> tasks;

    public TodoList()
    {
        tasks = new List<Task>();
    }

    public void AddTask(Task task)
    {
        tasks.Add(task);
    }

    public void MarkTaskAsComplete(int index)
    {
        if (index >= 0 && index < tasks.Count)
        {
            tasks[index].IsCompleted = true;
        }
    }

    public void DeleteTask(int index)
    {
        if (index >= 0 && index < tasks.Count)
        {
            tasks.RemoveAt(index);
        }
    }

    public void DisplayTasks()
    {
        for (int i = 0; i < tasks.Count; i++)
        {
            Task task = tasks[i];
            Console.WriteLine($"{i + 1}. {task.Description} (Due: {task.DueDate.ToShortDateString()}) - {(task.IsCompleted ? "Completed" : "Incomplete")}");
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        TodoList todoList = new TodoList();

        while (true)
        {
            Console.WriteLine("Todo List Application");
            Console.WriteLine("1. Add Task");
            Console.WriteLine("2. Mark Task as Complete");
            Console.WriteLine("3. Delete Task");
            Console.WriteLine("4. View Tasks");
            Console.WriteLine("5. Exit");
            Console.Write("Enter your choice: ");
            int choice = Convert.ToInt32(Console.ReadLine());

            switch (choice)
            {
                case 1:
                    Console.Write("Enter task description: ");
                    string description = Console.ReadLine();
                    Console.Write("Enter due date (yyyy-mm-dd): ");
                    DateTime dueDate = DateTime.Parse(Console.ReadLine());
                    Task task = new Task
                    {
                        Description = description,
                        DueDate = dueDate
                    };
                    todoList.AddTask(task);
                    Console.WriteLine("Task added successfully.");
                    break;
                case 2:
                    Console.Write("Enter the index of the task to mark as complete: ");
                    int completeIndex = Convert.ToInt32(Console.ReadLine()) - 1;
                    todoList.MarkTaskAsComplete(completeIndex);
                    Console.WriteLine("Task marked as complete.");
                    break;
                case 3:
                    Console.Write("Enter the index of the task to delete: ");
                    int deleteIndex = Convert.ToInt32(Console.ReadLine()) - 1;
                    todoList.DeleteTask(deleteIndex);
                    Console.WriteLine("Task deleted.");
                    break;
                case 4:
                    Console.WriteLine("Tasks:");
                    todoList.DisplayTasks();
                    break;
                case 5:
                    Console.WriteLine("Exiting the application...");
                    Environment.Exit(0);
                    break;
                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
            }

            Console.WriteLine();
        }
    }
}
