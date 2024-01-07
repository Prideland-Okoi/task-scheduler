# Task Scheduler Web App

This is a simple task scheduler web application built using Flask. Users can add, edit, mark as completed, and delete tasks. The application also provides statistics on completed and uncompleted tasks.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)
  - [Home Page](#home-page)
  - [Add Task](#add-task)
  - [Mark Task as Completed](#mark-task-as-completed)
  - [Delete Task](#delete-task)
  - [Edit Task](#edit-task)
  - [Display Tasks on Specific Date](#display-tasks-on-specific-date)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

4. Run the application:

   ```bash
   flask run
   ```

The application should be accessible at [http://localhost:5000/](http://localhost:5000/).

## Usage

- Navigate to [http://localhost:5000/](http://localhost:5000/) to access the home page.
- Add, edit, mark as completed, or delete tasks using the provided links and forms.
- View tasks on a specific date by navigating to the corresponding date route.

## Routes

### Home Page

- **Route:** `/`
- **Description:** Displays the list of tasks along with statistics on completed and uncompleted tasks.
- **Statistics:** The home page provides the count of completed and uncompleted tasks.

### Add Task

- **Route:** `/add_task`
- **Description:** Allows users to add a new task using a form.
- **Method:** GET (display form) and POST (submit form).
- **Form Fields:**
  - Title (task title)
  - Description (task description)
  - Due Date (task due date)

### Mark Task as Completed

- **Route:** `/complete_task/<int:task_id>`
- **Description:** Marks a specific task as completed.
- **Method:** GET (display confirmation) and POST (mark task as completed).

### Delete Task

- **Route:** `/delete_task/<int:task_id>`
- **Description:** Deletes a specific task.
- **Method:** GET (display confirmation) and POST (delete task).

### Edit Task

- **Route:** `/edit_task/<int:task_id>`
- **Description:** Allows users to edit an existing task using a form.
- **Method:** GET (display form) and POST (submit form).
- **Form Fields:** Same as the "Add Task" form.

### Display Tasks on Specific Date

- **Route:** `/tasks/<date>`
- **Description:** Displays tasks due on a specific date.
- **Method:** GET
- **Date Format:** `YYYY-MM-DD`

## Limitation of the Project/Tasks undone

- Absence of built-in authentication
- Inability to implement color changes on the calendar date when a cursor hovers over it

Feel free to explore and enhance the functionality as needed. If you encounter any issues or have suggestions, please open an issue on the GitHub repository.
