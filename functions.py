"""
Writing a program that schedules a break every
2hrs
Steps/analysis:
- the program keeps track of time
- waits every 2hrs without doing anything
- open browser to play music
- to repaeat these steps 3 times we need to use a loop
"""

import os
import time
import webbrowser

total_breaks = 3
break_count = 0
while break_count < total_breaks:
    time.sleep(2 * 60 * 60)
    webbrowser.open("https://www.youtube.com/watch?v=y9sUgP9vnJ4")
    break_count += 1

"""
Abstraction - the concept of hiding details in programming.
We can see this by the use of sleep and open functions in the modules time,
we don't even need to know how they work.
"""


def rename_files():
    """
    Steps:
    - get the files you want to rename from the folder.
    - for each file rename it.
    """
    file_list = os.listdir("path to folder with files")
    os.getcwd()  # returns the current working directory for the program
    os.chdir("path to folder with files")  # changes the working directory.
    # rename
    # translate function translates a string and removes the strings not required.
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

    os.chdir()  # change path to the original path.
