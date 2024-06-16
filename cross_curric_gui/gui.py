import tkinter as tk
from tkinter import ttk, filedialog
from config import Config
from main import main as generate_report

def submit():
    subject1 = subject1_var.get()
    subject2 = subject2_var.get()
    year_group = year_group_var.get()
    single_subject_mode = single_subject_mode_var.get()
    uploaded_files = file_list if file_list else None
    
    Config.update(subject1, subject2, year_group)
    
    if uploaded_files:
        generate_report(uploaded_files=uploaded_files)
    elif single_subject_mode:
        generate_report(single_subject_mode=True)
    else:
        generate_report(single_subject_mode=False)

def select_files():
    global file_list
    file_list = filedialog.askopenfilenames(filetypes=[("HTML files", "*.html")])
    files_label.config(text=f"Selected {len(file_list)} files")

# Create the main window
root = tk.Tk()
root.title("Curriculum Report Generator")

# Create and set the variables for the dropdowns
subject1_var = tk.StringVar(value=Config.SUBJECT1)
subject2_var = tk.StringVar(value=Config.SUBJECT2)
year_group_var = tk.StringVar(value=Config.YEAR_GROUP)
single_subject_mode_var = tk.BooleanVar()
file_list = []

# Create dropdown for subject1
subject1_label = ttk.Label(root, text="Subject 1:")
subject1_label.grid(column=0, row=0, padx=10, pady=5)
subject1_dropdown = ttk.Combobox(root, textvariable=subject1_var)
subject1_dropdown['values'] = ("Art", "Computing", "Citizenship", "Design and Technology", "English", "French", "Food and Nutrition", "Geography", "History", "Life Skills", "Maths", "Media Studies", "Music", "Physical Education", "Psychology", "PSHE", "Religious Education", "Science")
subject1_dropdown.grid(column=1, row=0, padx=10, pady=5)

# Create dropdown for subject2
subject2_label = ttk.Label(root, text="Subject 2:")
subject2_label.grid(column=0, row=1, padx=10, pady=5)
subject2_dropdown = ttk.Combobox(root, textvariable=subject2_var)
subject2_dropdown['values'] = ("Art", "Computing", "Citizenship", "Design and Technology", "English", "French", "Food and Nutrition", "Geography", "History", "Life Skills", "Maths", "Media Studies", "Music", "Physical Education", "Psychology", "PSHE", "Religious Education", "Science")
subject2_dropdown.grid(column=1, row=1, padx=10, pady=5)

# Create dropdown for year group
year_group_label = ttk.Label(root, text="Year Group:")
year_group_label.grid(column=0, row=2, padx=10, pady=5)
year_group_dropdown = ttk.Combobox(root, textvariable=year_group_var)
year_group_dropdown['values'] = ("Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Year 6", "Year 7", "Year 8", "Year 9", "Year 10", "Year 11", "Year 12", "Year 13")
year_group_dropdown.grid(column=1, row=2, padx=10, pady=5)

# Create checkbox for single subject mode
single_subject_mode_check = ttk.Checkbutton(root, text="Generate reports for all combinations with Subject 1", variable=single_subject_mode_var)
single_subject_mode_check.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

# Create file upload button
upload_button = ttk.Button(root, text="Upload HTML Files", command=select_files)
upload_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Label to show selected files
files_label = ttk.Label(root, text="")
files_label.grid(column=0, row=5, columnspan=2)

# Create submit button
submit_button = ttk.Button(root, text="Generate Report", command=submit)
submit_button.grid(column=0, row=6, columnspan=2, padx=10, pady=10)
# Start the GUI event loop
root.mainloop()
