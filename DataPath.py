import os
from dotenv import load_dotenv

load_dotenv()

def create_file_paths_txt(folder_path):
    with open('file_paths.txt', 'w') as file:
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                file.write(os.path.join(root, filename) + '\n')

folder_path = os.getenv('FOLDER_PATH') # Replace os.getenv('FOLDER_PATH') with path/to/folder if not using dotenv
create_file_paths_txt(folder_path)
