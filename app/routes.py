from flask import render_template, request, redirect, url_for, flash, Blueprint
from app.models import db, Task
from datetime import datetime
from app.forms import TaskForm


# Home page route
task = Blueprint('task', __name__)


@task.context_processor
def inject_data():
    completed_task_count = Task.query.filter_by(is_completed=True).count()
    uncompleted_task_count = Task.query.filter_by(is_completed=False).count()

    return {
        'data1': completed_task_count,
        'data2': uncompleted_task_count
    }


# Homepage route
@task.route('/')
def index():
    # tasks = Task.query.all()
    tasks = Task.query.order_by(Task.date_created.desc()).all()
    # Get completed task count from the database
    completed_task_count = Task.query.filter_by(is_completed=True).count()

    # Get uncompleted task count from the database
    uncompleted_task_count = Task.query.filter_by(is_completed=False).count()
    return render_template(
        'scheduler.html',
        tasks=tasks,
        completed_task_count=completed_task_count,
        uncompleted_task_count=uncompleted_task_count
        )


# Add task route
@task.route('/add_task', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        due_date = form.due_date.data
        new_task = Task(title=title, description=description,
                        due_date=due_date)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')

        return redirect(url_for('task.index'))

    return render_template('add_schedule.html', form=form)


# Mark task as completed route
@task.route('/complete_task/<int:task_id>', methods=['GET', 'POST'])
def complete_task(task_id):
    task = Task.query.get(task_id)

    if task:
        task.is_completed = True
        db.session.commit()
        flash('Task marked as completed.', 'success')
    else:
        flash('Task not found.', 'danger')

    return redirect(url_for('task.index'))


# Delete task route
@task.route('/delete_task/<int:task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)

    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully.', 'success')
    else:
        flash('Task not found.', 'danger')

    return redirect(url_for('task.index'))


# Edit task route
@task.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        flash('Task not found.', 'danger')
        return redirect(url_for('task.index'))

    form = TaskForm(obj=task)

    if request.method == 'POST' and form.validate():
        form.populate_obj(task)
        # Update task attributes manually
        # task.title = form.title.data
        # task.description = form.description.data
        # task.due_date = form.due_date.data
        db.session.commit()

        flash('Task edited successfully!', 'success')
        return redirect(url_for('task.index'))

    return render_template('edit_schedule.html', task=task, form=form)


# Specific date route
@task.route('/tasks/<date>', methods=['GET', 'POST'])
def display_tasks(date):
    # Convert the date string to a datetime object
    date_obj = datetime.strptime(date, '%Y-%m-%d')

    # Query the database for tasks on the specified date
    tasks = Task.query.filter(Task.due_date == date_obj).all()

    return render_template(
        'display_tasks.html',
        date=date_obj.strftime('%Y-%m-%d'),
        tasks=tasks
        )
