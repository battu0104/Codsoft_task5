import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")

        self.contacts = []

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.search_label = tk.Label(master, text="Search:")
        self.search_label.grid(row=6, column=0, padx=10, pady=5)
        self.search_entry = tk.Entry(master)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5)

        self.search_button = tk.Button(master, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            new_contact = Contact(name, phone, email, address)
            self.contacts.append(new_contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{contact.name}: {contact.phone}" for contact in self.contacts])
            messagebox.showinfo("Contact List", contact_list)
        else:
            messagebox.showinfo("Contact List", "contacts found.")

    def search_contact(self):
        search_term = self.search_entry.get().lower()
        results = [contact for contact in self.contacts if search_term in contact.name.lower() or search_term in contact.phone.lower()]

        if results:
            result_list = "\n".join([f"{contact.name}: {contact.phone}" for contact in results])
            messagebox.showinfo("Search Results", result_list)
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    contact_manager = ContactManager(root)
    root.mainloop()
