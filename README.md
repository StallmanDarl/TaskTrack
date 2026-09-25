# TaskTrack

TaskTrack is a simple Python task-management program that allows users to create, view, and manage a list of tasks through a text-based menu. Tasks can be entered through user input, displayed in the terminal, and saved to a text file so they can be loaded again when the program is restarted.

## Current Features

- Add new tasks
- View the current task list
- Prevent empty tasks from being added
- Save tasks to a text file
- Load previously saved tasks when the program starts
- Handle missing task files without crashing

## Requirements

- Python 3

## Project Files

- `tasktrack.py` — Contains the main program and functions for adding, viewing, loading, and saving tasks.
- `tasks.txt` — Stores the current tasks so they can be loaded when the program is started again.
- `.gitignore` — Lists files and folders that Git should ignore when tracking the project.

## Running the Program

Open a terminal or command prompt and navigate to the folder containing the TaskTrack project.

On Windows, run:

```text
py .\tasktrack.py