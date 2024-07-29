import tkinter as tk
import os
import sys
import shutil
import subprocess


def get_filename():
    if getattr(sys, 'frozen', False):
        original_exe_path = sys.executable
    else:
        original_exe_path = __file__

    return original_exe_path


def change_game():
    original_exe_path = get_filename()

    new_name = entry.get()

    new_exe_path = os.path.join(os.path.dirname(original_exe_path), f'{new_name}.exe')

    try:
        shutil.move(original_exe_path, new_exe_path)
        print(f"File renamed to {new_exe_path}")

        subprocess.Popen([new_exe_path], shell=True)
        print(f"File {new_exe_path} executed")

        root.quit()

    except Exception as e:
        print(f"An error occurred: {e}")


root = tk.Tk()
root.geometry('350x50')
root.title(get_filename().split("\\")[-1][:-4])
root.resizable(False, False)

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Change Game", command=change_game)
button.pack()

root.mainloop()
