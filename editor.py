import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter
import os
import ast
def compile_lines():
    content = text_area.get("1.0", "end-1c").split("\n")
    compiled_content = [line.strip() for line in content if line.strip()]
    output_area.delete("1.0", "end")
    output_area.insert("1.0", "[" + ", ".join([f'"{line}"' for line in compiled_content]) + "]")
    
def decompile():
    content = output_area.get("1.0", "end-1c")
    try:
        decompiled_content = ast.literal_eval(content)
        text_area.delete("1.0", "end")
        text_area.insert("1.0", "\n".join(decompiled_content))
    except ValueError:
        messagebox.showerror("Error", "Invalid format for decompilation.")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.grimbly"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete("1.0", "end")
            text_area.insert("1.0", content)
    
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".grimbly", filetypes=[("Grimbly files", "*.grimbly"), ("All files", "*.*")])
    if file_path:
        content = text_area.get("1.0", "end-1c").split("\n")
        compiled_content = [line.strip() for line in content if line.strip()]
        compiled_script = "[" + ", ".join([f'"{line}"' for line in compiled_content]) + "]"

        # Convert compiled script to binary data
        binary_data = compiled_script.encode()

        # Check if file already exists
        if not os.path.exists(file_path):
            with open(file_path, "wb") as file:  # Open the file in binary write mode
                file.write(binary_data)
        else:
            # If file exists, prompt user for confirmation before overwriting
            overwrite = messagebox.askyesno("Confirm Overwrite", "File already exists. Do you want to overwrite it?")
            if overwrite:
                with open(file_path, "wb") as file:  # Open the file in binary write mode
                    file.write(binary_data)
def new_file():
    text_area.delete("1.0", "end")

customtkinter.set_appearance_mode("System")
# Create the main window
root = tk.Tk()
root.title("Text Editor")
#Text area for editing
text_area = tk.Text(root)
text_area.pack(expand=True, fill="both")

# Compile button
compile_button = tk.Button(root, text="Compile", command=compile_lines)
compile_button.pack()
decompiled_button = tk.Button(root, text="Decompile", command=decompile)
decompiled_button.pack()
# Output area for compiled content
output_area = tk.Text(root)
output_area.pack(expand=True, fill="both")

# Menu bar
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="New File", command=new_file)  # New File button
file_menu.add_command(label="Decompile", command=decompile)  # Added decompile option
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)


root.mainloop()
