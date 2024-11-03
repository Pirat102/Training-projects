import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/patry/Documents/pyth"
destination_dir = "C:/Users/patry/Desktop/Backup"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    print(today, dest_dir)
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in the {dest}")
        
        
schedule.every().day.at("10:17").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
