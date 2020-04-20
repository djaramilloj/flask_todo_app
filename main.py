from flask import  request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
import unittest
from app import create_app
from app.forms import LoginForm, TodoForm, DeleteTodoForm, UpdateTodoForm
from app.firestore_service import  delete_todo, get_todos, todo_put, update_todo, get_users
from flask_login import login_required, current_user

app = create_app()
    

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index(): 
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello_world():
    user_ip = session.get('user_ip') 
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()
    update_form = UpdateTodoForm()

    context = {'user_ip': user_ip, 'todos': get_todos(user_id=username), 'username': username, 'todo_form': todo_form, 'delete_form': delete_form, 'update_form': update_form}

    if todo_form.validate_on_submit():
        todo_put(user_id=username, descripcion=todo_form.descripcion.data)

        flash('Tu tarea se creó con exito')

        redirect(url_for('hello_world'))
 
    return render_template('hello.html', **context)



@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id

    delete_todo(user_id, todo_id)

    return redirect(url_for('hello_world'))



@app.route('/todos/update/<todo_id>/<int:done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id

    update_todo(user_id, todo_id, done)

    return redirect(url_for('hello_world'))




