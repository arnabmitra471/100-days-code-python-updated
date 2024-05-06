import os
def create_folders_and_files():
    base_dir = "C:/Users/User/Documents"
    folder_name = "100daysOfCodeStartToEnd"

    base_folder_path = os.path.join(base_dir,folder_name)
    os.makedirs(base_folder_path,exist_ok=True)

    for i in range(1,101):
        day_folder_name = f"Day_{i}"
        day_folder_path = os.path.join(base_folder_path,day_folder_name)
        os.makedirs(day_folder_path,exist_ok=True)

        file_path = os.path.join(day_folder_path,"main.py")
        with open(file_path,"w") as f:
            f.write("# This is main.py")
    print("Files and folders created successfully")

create_folders_and_files()
