import sys
import tkinter as tk
from tkinter import messagebox
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QListWidget, QMessageBox

class ToDoListAppCombined(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do List")

        self.tasks_tk = []
        self.tasks_pyqt = []

        self.task_entry_tk = tk.Entry()
        self.add_button_tk = tk.Button(text="Add Task", command=self.add_task_tk)
        self.complete_button_tk = tk.Button(text="Complete Task", command=self.complete_task_tk)
        self.delete_button_tk = tk.Button(text="Delete Task", command=self.delete_task_tk)
        self.task_listbox_tk = tk.Listbox(selectmode=tk.SINGLE)

        self.task_entry_pyqt = QLineEdit()
        self.add_button_pyqt = QPushButton("Add Task")
        self.add_button_pyqt.clicked.connect(self.add_task_pyqt)
        self.complete_button_pyqt = QPushButton("Complete Task")
        self.complete_button_pyqt.clicked.connect(self.complete_task_pyqt)
        self.delete_button_pyqt = QPushButton("Delete Task")
        self.delete_button_pyqt.clicked.connect(self.delete_task_pyqt)
        self.task_listwidget_pyqt = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.task_entry_pyqt)
        layout.addWidget(self.add_button_pyqt)
        layout.addWidget(self.complete_button_pyqt)
        layout.addWidget(self.delete_button_pyqt)
        layout.addWidget(self.task_listwidget_pyqt)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.init_tkinter()
        self.load_tasks()

    def add_task_tk(self):
        task = self.task_entry_tk.get()
        if task:
            self.tasks_tk.append(task)
            self.task_listbox_tk.insert(tk.END, task)
            self.task_entry_tk.delete(0, tk.END)
            self.save_tasks()

    def complete_task_tk(self):
        selected_index = self.task_listbox_tk.curselection()
        if selected_index:
            task_index = selected_index[0]
            task = self.tasks_tk[task_index]
            self.tasks_tk[task_index] = task + " [Completed]"
            self.task_listbox_tk.delete(task_index)
            self.task_listbox_tk.insert(tk.END, self.tasks_tk[task_index])
            self.save_tasks()
        else:
            messagebox.showinfo("No Task Selected", "Please select a task to mark as completed.")

    def delete_task_tk(self):
        selected_index = self.task_listbox_tk.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.task_listbox_tk.delete(task_index)
            del self.tasks_tk[task_index]
            self.save_tasks()
        else:
            messagebox.showinfo("No Task Selected", "Please select a task to delete.")

    def add_task_pyqt(self):
        task = self.task_entry_pyqt.text()
        if task:
            self.tasks_pyqt.append(task)
            self.task_listwidget_pyqt.addItem(task)
            self.task_entry_pyqt.clear()
            self.save_tasks()

    def complete_task_pyqt(self):
        selected_items = self.task_listwidget_pyqt.selectedItems()
        if selected_items:
            item = selected_items[0]
            index = self.task_listwidget_pyqt.row(item)
            task = self.tasks_pyqt[index]
            self.tasks_pyqt[index] = task + " [Completed]"
            item.setText(self.tasks_pyqt[index])
            self.save_tasks()
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("No Task Selected")
            msg_box.setText("Please select a task to mark as completed.")
            msg_box.exec_()

    def delete_task_pyqt(self):
        selected_items = self.task_listwidget_pyqt.selectedItems()
        if selected_items:
            item = selected_items[0]
            index = self.task_listwidget_pyqt.row(item)
            del self.tasks_pyqt[index]
            self.task_listwidget_pyqt.takeItem(index)
            self.save_tasks()
        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("No Task Selected")
            msg_box.setText("Please select a task to delete.")
            msg_box.exec_()

    def init_tkinter(self):
        self.task_entry_tk.grid(row=0, column=0, padx=5, pady=5)
        self.add_button_tk.grid(row=0, column=1, padx=5, pady=5)
        self.complete_button_tk.grid(row=1, column=0, padx=5, pady=5)
        self.delete_button_tk.grid(row=1, column=1, padx=5, pady=5)
        self.task_listbox_tk.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for task in file:
                    self.add_task_tk()
                    self.add_task_pyqt()
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks_tk:
                file.write(task + "\n")
            for task in self.tasks_pyqt:
                file.write(task + "\n")

def main_combined():
    app = QApplication(sys.argv)
    window = ToDoListAppCombined()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main_combined()
