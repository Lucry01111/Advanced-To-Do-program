import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt

class ToDoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.geometry("600x500") 
        self.master.configure(bg="#1c1c1c") 

        self.tasks = []

        self.frame = tk.Frame(self.master, bg="#1c1c1c")
        self.frame.pack(pady=20)

        self.task_listbox = tk.Listbox(self.frame, width=70, height=15, selectmode=tk.SINGLE, bg="#2e2e2e", fg="#00ff00", font=("Courier New", 12))
        self.task_listbox.pack(side=tk.LEFT)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.button_frame = tk.Frame(self.master, bg="#1c1c1c")
        self.button_frame.pack(pady=20)

        self.add_task_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, bg="#00ff00", fg="#1c1c1c", font=("Courier New", 12))
        self.add_task_button.pack(side=tk.LEFT, padx=10)

        self.complete_task_button = tk.Button(self.button_frame, text="Complete Task", command=self.complete_task, bg="#00ff00", fg="#1c1c1c", font=("Courier New", 12))
        self.complete_task_button.pack(side=tk.LEFT, padx=10)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, bg="#00ff00", fg="#1c1c1c", font=("Courier New", 12))
        self.delete_task_button.pack(side=tk.LEFT, padx=10)

        self.plot_button = tk.Button(self.button_frame, text="Task Distribution", command=self.show_distribution, bg="#00ff00", fg="#1c1c1c", font=("Courier New", 12))
        self.plot_button.pack(side=tk.LEFT, padx=10)

    def add_task(self):
        task = simpledialog.askstring("Input", "Enter the task:", parent=self.master)
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            messagebox.showinfo("Success", f"Task '{task}' added.", parent=self.master)

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = True
            self.update_task_listbox()
            messagebox.showinfo("Success", f"Task '{self.tasks[selected_index]['task']}' completed.", parent=self.master)
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to complete.", parent=self.master)

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            removed_task = self.tasks.pop(selected_index)
            self.update_task_listbox()
            messagebox.showinfo("Success", f"Task '{removed_task['task']}' deleted.", parent=self.master)
        except IndexError:
            messagebox.showwarning("Warning", "Select a task to delete.", parent=self.master)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  
        for task in self.tasks:
            status = "✔️" if task["completed"] else "❌"
            self.task_listbox.insert(tk.END, f"{task['task']} [{status}]")

    def show_distribution(self):
        if not self.tasks:
            messagebox.showwarning("Warning", "No tasks available to show distribution.", parent=self.master)
            return

        completed_count = sum(1 for task in self.tasks if task["completed"])
        uncompleted_count = len(self.tasks) - completed_count

        labels = ['Completed', 'Uncompleted']
        sizes = [completed_count, uncompleted_count]
        colors = ['#00ff00', '#d3d3d3'] 

        plt.figure(figsize=(8, 6), facecolor="white") 
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title('Task Distribution', color="#00ff00")
        plt.axis('equal')  
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()