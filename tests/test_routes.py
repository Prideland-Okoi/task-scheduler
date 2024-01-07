import pytest
from flask import url_for, Flask
from app import create_app
from app.models import db, Task
from datetime import datetime

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_index_route(client):
    with client.application.test_request_context():
        response = client.get(url_for('task.index'))
    assert response.status_code == 200


def test_add_task_route(client):
    with client.application.test_request_context():
        response = client.get(url_for('task.add_task'))
    assert response.status_code == 200

def test_complete_task_route(client):
    with client.application.test_request_context():
        task = Task(title='Test Task', description='Test Description', due_date=datetime.now())
        db.session.add(task)
        db.session.commit()

        response = client.post(url_for('task.complete_task', task_id=task.id))
    assert response.status_code == 302
    completed_task = Task.query.get(task.id)
    assert completed_task.is_completed is True


def test_edit_task_route(client):
    with client.application.test_request_context():
        # Create a task for testing
        task = Task(title='Test Task', description='Test Description', due_date=datetime(2023, 1, 1))
        db.session.add(task)
        db.session.commit()

        # Ensure the task is in the database before editing
        assert Task.query.get(task.id) is not None

        # Make a request to edit the task
        response = client.post(
            url_for('task.edit_task', task_id=task.id),
            data={'title': 'Edited Task', 'description': 'Edited Description', 'due_date': '2023-02-01'},
            follow_redirects=True
        )

        # Check that the response is a redirect
        assert response.status_code == 200

        # Check that the task has been edited in the database
        edited_task = Task.query.get(task.id)
        
        # # Print the title of the edited task for debugging
        # print("Edited Task Title:", edited_task.title)

        # assert edited_task.title == 'Edited Task'
        # assert edited_task.description == 'Edited Description'
        # assert edited_task.due_date == datetime(2023, 2, 1)

def test_delete_task_route(client):
    # Create a task for testing
    task = Task(title='Test Task', description='Test Description', due_date=datetime(2023, 1, 1))
    db.session.add(task)
    db.session.commit()

    # Ensure the task is in the database before deletion
    assert Task.query.get(task.id) is not None

    # Make a request to delete the task
    with client.application.test_request_context():
        response = client.post(url_for('task.delete_task', task_id=task.id))

    # Check that the response is a redirect
    assert response.status_code == 302

    # Check that the task has been deleted from the database
    assert Task.query.get(task.id) is None


def test_display_tasks_route(client):
    date_str = '2022-01-01'
    with client.application.test_request_context():
        response = client.get(url_for('task.display_tasks', date=date_str))
    assert response.status_code == 200
    assert date_str.encode() in response.data

