import os

# Define paths
folder_path = r"C:\1\example_folder"
file_path = os.path.join(folder_path, "example.txt")

# Create the folder (if it doesn't already exist)
os.makedirs(folder_path, exist_ok=True)

# Create and write to the text file
with open(file_path, "w", encoding="utf-8") as file:
    file.write("This is a sample text file created by Python.")

print("Folder and file created successfully.")
