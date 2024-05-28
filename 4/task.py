import os
import time
from datetime import timedelta


def remove_elder_files(folder: str = 'some_junk', days: int = 1):
    expiration_date = time.time() - timedelta(days=days).total_seconds()
    path_to_folder = os.path.join(os.getcwd(), folder)
    files = os.listdir(path_to_folder)
    for file in files:
        file_path = os.path.join(path_to_folder, file)
        creation_date_of_file = os.stat(file_path).st_birthtime
        if creation_date_of_file < expiration_date:
            os.remove(file_path)
            print(f'{file_path} has been removed')


remove_elder_files()
