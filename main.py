import random
import string
import tkinter as tk
from tkinter import messagebox


class My_Frame(tk.Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent

		# Create and configure the length label and entry
		length_label = tk.Label(self, text="Password Length:")
		length_label.pack(pady=10)
		self.length_entry = tk.Entry(self)
		self.length_entry.pack(pady=10, padx=10)

		# Create and configure the generate button
		generate_button = tk.Button(self, text="Generate Password", command=self.generate_password)
		generate_button.pack(pady=10)

		# Create and configure the result label
		self.result_label = tk.Label(self, text="Generated Password: ")
		self.result_label.pack(pady=10, padx=10)


	def generate_password(self):

		try:
			# Get the current length
			password_length = int(self.length_entry.get())

		except ValueError:

			# Bring up messagebox when input data in not a number
			messagebox.showerror(title=None, message="Please ensure input is a number")
			self.length_entry.delete(0, tk.END)
			return

		# Get list of avaiable characters
		characters = string.ascii_letters + string.digits + string.punctuation

		# Generate the password
		password = ''.join(random.choice(characters) for _ in range(password_length))

		# Update the label with the generated password
		self.result_label.configure(text=f"Generated Password:\n{password}")

		# Empty entry box when done
		self.length_entry.delete(0, tk.END)

def main():

	# Create window and label it
	root = tk.Tk()
	root.title("Password Generator")

	myframe = My_Frame(root)
	myframe.pack(pady=10)

	# Run the window
	root.mainloop()


if __name__ == '__main__':
	main()
