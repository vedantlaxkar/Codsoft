import tkinter as tk
from tkinter import messagebox
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QListWidget, QListWidgetItem, QMessageBox, QDialog
import json
import os

class ContactBookTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.refresh_contacts()  # Load contacts when the application starts
        
        # Frames
        self.add_frame = tk.Frame(self.root)
        self.search_frame = tk.Frame(self.root)
        self.update_frame = tk.Frame(self.root)
        self.delete_frame = tk.Frame(self.root)
        
        self.current_frame = self.add_frame
        self.current_frame.pack()
        
        # Add Contact Page
        self.name_label = tk.Label(self.add_frame, text="Name:")
        self.name_entry = tk.Entry(self.add_frame)
        self.phone_label = tk.Label(self.add_frame, text="Phone Number:")
        self.phone_entry = tk.Entry(self.add_frame)
        self.email_label = tk.Label(self.add_frame, text="Email:")
        self.email_entry = tk.Entry(self.add_frame)
        self.address_label = tk.Label(self.add_frame, text="Address:")
        self.address_entry = tk.Entry(self.add_frame)
        self.add_button = tk.Button(self.add_frame, text="Add Contact", command=self.add_contact)
        self.search_button = tk.Button(self.add_frame, text="Search Contact", command=self.show_search_page)
        self.update_button = tk.Button(self.add_frame, text="Update Contact", command=self.show_update_page)
        self.delete_button = tk.Button(self.add_frame, text="Delete Contact", command=self.show_delete_page)
        
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.phone_label.grid(row=1, column=0)
        self.phone_entry.grid(row=1, column=1)
        self.email_label.grid(row=2, column=0)
        self.email_entry.grid(row=2, column=1)
        self.address_label.grid(row=3, column=0)
        self.address_entry.grid(row=3, column=1)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=5)
        self.search_button.grid(row=5, column=0, pady=5)
        self.update_button.grid(row=5, column=1, pady=5)
        self.delete_button.grid(row=6, column=0, columnspan=2, pady=5)
    
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if not name or not phone or not email or not address:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        self.save_contacts()
        messagebox.showinfo("Success", "Contact added successfully!")
        self.refresh_contacts()  # Refresh contacts after adding a new one
    
    def show_search_page(self):
        self.current_frame.pack_forget()
        self.current_frame = self.search_frame
        self.current_frame.pack()
        self.search_listbox.delete(0, tk.END)
        for name in self.contacts.keys():
            self.search_listbox.insert(tk.END, name)
        self.back_button = tk.Button(self.search_frame, text="Back", command=self.show_add_page)
        self.back_button.pack()
    
    def show_update_page(self):
        self.current_frame.pack_forget()
        self.current_frame = self.update_frame
        self.current_frame.pack()
        self.update_listbox.delete(0, tk.END)
        for name in self.contacts.keys():
            self.update_listbox.insert(tk.END, name)
        self.back_button = tk.Button(self.update_frame, text="Back", command=self.show_add_page)
        self.back_button.pack()
    
    def show_delete_page(self):
        self.current_frame.pack_forget()
        self.current_frame = self.delete_frame
        self.current_frame.pack()
        self.delete_listbox.delete(0, tk.END)
        for name in self.contacts.keys():
            self.delete_listbox.insert(tk.END, name)
        self.back_button = tk.Button(self.delete_frame, text="Back", command=self.show_add_page)
        self.back_button.pack()
    
    def show_add_page(self):
        self.current_frame.pack_forget()
        self.current_frame = self.add_frame
        self.current_frame.pack()
    
    def refresh_contacts(self):
        try:
            with open("contacts.json", "r") as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            self.contacts = {}
    
    def save_contacts(self):
        try:
            with open("contacts.json", "w") as f:
                json.dump(self.contacts, f)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving contacts: {e}")

class ContactBookQt(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contacts = {}
        self.setWindowTitle("Contact Book")
        self.setGeometry(100, 100, 400, 300)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.current_widget = None
        self.show_add_contact_page()
        self.refresh_contacts()  # Load contacts when the application starts
    
    def show_add_contact_page(self):
        self.clear_layout()
        self.current_widget = QWidget()
        layout = QVBoxLayout()
        name_label = QLabel("Name:")
        self.name_entry = QLineEdit()
        phone_label = QLabel("Phone Number:")
        self.phone_entry = QLineEdit()
        email_label = QLabel("Email:")
        self.email_entry = QLineEdit()
        address_label = QLabel("Address:")
        self.address_entry = QLineEdit()
        add_button = QPushButton("Add Contact")
        add_button.clicked.connect(self.add_contact)
        search_button = QPushButton("Search Contact")
        search_button.clicked.connect(self.show_search_page)
        update_button = QPushButton("Update Contact")
        update_button.clicked.connect(self.show_update_page)
        delete_button = QPushButton("Delete Contact")
        delete_button.clicked.connect(self.show_delete_page)
        
        layout.addWidget(name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(phone_label)
        layout.addWidget(self.phone_entry)
        layout.addWidget(email_label)
        layout.addWidget(self.email_entry)
        layout.addWidget(address_label)
        layout.addWidget(self.address_entry)
        layout.addWidget(add_button)
        layout.addWidget(search_button)
        layout.addWidget(update_button)
        layout.addWidget(delete_button)
        self.current_widget.setLayout(layout)
        self.layout.addWidget(self.current_widget)
    
    def add_contact(self):
        name = self.name_entry.text()
        phone = self.phone_entry.text()
        email = self.email_entry.text()
        address = self.address_entry.text()
        if not name or not phone or not email or not address:
            QMessageBox.critical(self, "Error", "Please fill in all fields.")
            return
        self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        self.save_contacts()
        QMessageBox.information(self, "Success", "Contact added successfully!")
        self.refresh_contacts()  # Refresh contacts after adding a new one
    
    def show_search_page(self):
        self.clear_layout()
        self.current_widget = QWidget()
        layout = QVBoxLayout()
        self.search_list = QListWidget()
        for name in self.contacts.keys():
            self.search_list.addItem(QListWidgetItem(name))
        self.search_list.itemClicked.connect(self.view_contact)
        layout.addWidget(self.search_list)
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.show_add_contact_page)
        layout.addWidget(back_button)
        self.current_widget.setLayout(layout)
        self.layout.addWidget(self.current_widget)
    
    def view_contact(self, item):
        name = item.text()
        contact = self.contacts[name]
        QMessageBox.information(self, "Contact Details", f"Name: {name}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}")
    
    def show_update_page(self):
        self.clear_layout()
        self.current_widget = QWidget()
        layout = QVBoxLayout()
        self.update_list = QListWidget()
        for name in self.contacts.keys():
            self.update_list.addItem(QListWidgetItem(name))
        self.update_list.itemClicked.connect(self.update_contact)
        layout.addWidget(self.update_list)
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.show_add_contact_page)
        layout.addWidget(back_button)
        self.current_widget.setLayout(layout)
        self.layout.addWidget(self.current_widget)
    
    def update_contact(self, item):
        name = item.text()
        contact = self.contacts[name]
        update_window = UpdateContactWindow(name, contact)
        if update_window.exec_() == QDialog.Accepted:
            new_name = update_window.name_entry.text()
            new_phone = update_window.phone_entry.text()
            new_email = update_window.email_entry.text()
            new_address = update_window.address_entry.text()
            del self.contacts[name]  # Remove the old contact entry
            self.contacts[new_name] = {"Phone": new_phone, "Email": new_email, "Address": new_address}  # Add the updated contact entry
            self.save_contacts()  # Save the updated contacts to file
            QMessageBox.information(self, "Success", "Contact updated successfully!")
            self.refresh_contacts()  # Refresh contacts after updating
    
    def show_delete_page(self):
        self.clear_layout()
        self.current_widget = QWidget()
        layout = QVBoxLayout()
        self.delete_list = QListWidget()
        for name in self.contacts.keys():
            self.delete_list.addItem(QListWidgetItem(name))
        self.delete_list.itemClicked.connect(self.delete_contact)
        layout.addWidget(self.delete_list)
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.show_add_contact_page)
        layout.addWidget(back_button)
        self.current_widget.setLayout(layout)
        self.layout.addWidget(self.current_widget)
    
    def delete_contact(self, item):
        name = item.text()
        reply = QMessageBox.question(self, 'Delete Contact', f"Are you sure you want to delete {name}?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            del self.contacts[name]
            self.save_contacts()
            QMessageBox.information(self, "Success", "Contact deleted successfully!")
            self.refresh_contacts()  # Refresh contacts after deleting
    
    def refresh_contacts(self):
        try:
            with open("contacts.json", "r") as f:
                self.contacts = json.load(f)
        except FileNotFoundError:
            self.contacts = {}
    
    def save_contacts(self):
        try:
            with open("contacts.json", "w") as f:
                json.dump(self.contacts, f)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while saving contacts: {e}")
    
    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

class UpdateContactWindow(QDialog):
    def __init__(self, name, contact):
        super().__init__()
        self.setWindowTitle("Update Contact")
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.name_label = QLabel("Name:")
        self.name_entry = QLineEdit(name)
        self.phone_label = QLabel("Phone Number:")
        self.phone_entry = QLineEdit(contact["Phone"])
        self.email_label = QLabel("Email:")
        self.email_entry = QLineEdit(contact["Email"])
        self.address_label = QLabel("Address:")
        self.address_entry = QLineEdit(contact["Address"])
        
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_entry)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.phone_entry)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_entry)
        layout.addWidget(self.address_label)
        layout.addWidget(self.address_entry)

        # Add buttons to accept or reject changes
        buttons_layout = QHBoxLayout()
        self.accept_button = QPushButton("Update")
        self.accept_button.clicked.connect(self.accept_changes)
        self.reject_button = QPushButton("Cancel")
        self.reject_button.clicked.connect(self.reject_changes)
        buttons_layout.addWidget(self.accept_button)
        buttons_layout.addWidget(self.reject_button)
        layout.addLayout(buttons_layout)

    def accept_changes(self):
        self.accept()

    def reject_changes(self):
        self.reject()

def main():
    root = tk.Tk()
    contact_book_tkinter = ContactBookTkinter(root)
    
    app = QApplication([])
    contact_book_qt = ContactBookQt()
    contact_book_qt.show()
    app.exec_()

if __name__ == "__main__":
    main()
